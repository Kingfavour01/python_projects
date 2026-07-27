import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont


class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700, 300, 500, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 60))
        self.label.setStyleSheet("""
            QLabel {
                color: #00ff00;
                background-color: black;
                border: 2px solid #00ff00;
                border-radius: 10px;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        central_widget.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        self.update_clock()

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
