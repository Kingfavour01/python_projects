import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont


class Stopwatch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")
        self.setGeometry(700, 300, 400, 300)

        self.elapsed_ms = 0
        self.running = False

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.time_label = QLabel("00:00.00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont("Arial", 50))
        self.time_label.setStyleSheet("""
            QLabel {
                color: #333;
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.reset_btn = QPushButton("Reset")

        for btn in (self.start_btn, self.stop_btn, self.reset_btn):
            btn.setFont(QFont("Arial", 14))

        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        btn_layout.addWidget(self.reset_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addLayout(btn_layout)
        central_widget.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.setInterval(10)

    def update_time(self):
        self.elapsed_ms += 10
        minutes = self.elapsed_ms // 60000
        seconds = (self.elapsed_ms % 60000) // 1000
        centiseconds = (self.elapsed_ms % 1000) // 10
        self.time_label.setText(f"{minutes:02d}:{seconds:02d}.{centiseconds:02d}")

    def start(self):
        if not self.running:
            self.running = True
            self.timer.start()

    def stop(self):
        if self.running:
            self.running = False
            self.timer.stop()

    def reset(self):
        self.running = False
        self.timer.stop()
        self.elapsed_ms = 0
        self.time_label.setText("00:00.00")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
