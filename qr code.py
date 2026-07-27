import sys
import qrcode
from io import BytesIO
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QLineEdit, QVBoxLayout, QHBoxLayout, QWidget,
                             QFileDialog)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class QRCodeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(700, 300, 400, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.title_label = QLabel("QR Code Generator")
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter text or URL...")
        self.text_input.setFont(QFont("Arial", 12))
        self.text_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #aaa;
                border-radius: 5px;
            }
        """)

        self.generate_btn = QPushButton("Generate QR Code")
        self.generate_btn.setFont(QFont("Arial", 12))
        self.generate_btn.setStyleSheet("""
            QPushButton {
                padding: 10px;
                background-color: #2d2d2d;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #444;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_qr)

        self.save_btn = QPushButton("Save as PNG")
        self.save_btn.setFont(QFont("Arial", 12))
        self.save_btn.clicked.connect(self.save_qr)
        self.save_btn.setEnabled(False)

        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setMinimumSize(300, 300)
        self.qr_label.setStyleSheet("border: 1px dashed #ccc;")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.generate_btn)
        btn_layout.addWidget(self.save_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addSpacing(10)
        layout.addWidget(self.text_input)
        layout.addLayout(btn_layout)
        layout.addSpacing(10)
        layout.addWidget(self.qr_label)
        layout.addStretch()
        central_widget.setLayout(layout)

        self.current_qr = None

    def generate_qr(self):
        text = self.text_input.text().strip()
        if not text:
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        self.current_qr = img

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        self.qr_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.save_btn.setEnabled(True)

    def save_qr(self):
        if self.current_qr:
            path, _ = QFileDialog.getSaveFileName(
                self, "Save QR Code", "qr_code.png", "PNG Files (*.png)"
            )
            if path:
                self.current_qr.save(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeGenerator()
    window.show()
    sys.exit(app.exec_())
