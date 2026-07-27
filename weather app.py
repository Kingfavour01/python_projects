import sys
import requests
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 300, 400, 450)
        self.setStyleSheet("background-color: #1e1e2e;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.title_label = QLabel("Weather App")
        self.title_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.title_label.setStyleSheet("color: #cba6f7;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name...")
        self.city_input.setFont(QFont("Arial", 14))
        self.city_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #585b70;
                border-radius: 8px;
                color: #cdd6f4;
                background-color: #313244;
            }
            QLineEdit:focus {
                border-color: #cba6f7;
            }
        """)

        self.search_btn = QPushButton("Search")
        self.search_btn.setFont(QFont("Arial", 14))
        self.search_btn.setStyleSheet("""
            QPushButton {
                padding: 10px;
                background-color: #cba6f7;
                color: #1e1e2e;
                border: none;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #b4befe;
            }
        """)
        self.search_btn.clicked.connect(self.get_weather)

        self.result_label = QLabel()
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setStyleSheet("color: #cdd6f4; padding: 10px;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.city_input)
        input_layout.addWidget(self.search_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addSpacing(20)
        layout.addLayout(input_layout)
        layout.addSpacing(20)
        layout.addWidget(self.result_label)
        layout.addStretch()
        central_widget.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Error", "Please enter a city name.")
            return

        try:
            api_key = "YOUR_API_KEY"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url, timeout=10)

            if response.status_code == 404:
                self.result_label.setText(f"City '{city}' not found.")
                return
            elif response.status_code != 200:
                self.result_label.setText(f"API error (status {response.status_code}).")
                return

            data = response.json()
            temp_k = data["main"]["temp"]
            temp_f = (temp_k - 273.15) * 9 / 5 + 32
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].title()
            wind = data["wind"]["speed"]
            country = data["sys"]["country"]

            self.result_label.setText(
                f"{city.title()}, {country}\n\n"
                f"Temperature: {temp_f:.1f} °F\n"
                f"Condition: {description}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind} m/s"
            )
        except requests.ConnectionError:
            self.result_label.setText("No internet connection.")
        except Exception as e:
            self.result_label.setText(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather = WeatherApp()
    weather.show()
    sys.exit(app.exec_())
