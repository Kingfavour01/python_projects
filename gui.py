import sys

from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QLabel,
                             QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.resize(400, 300)
        self.setGeometry(0,0, 500, 500)
        self.setWindowIcon(QIcon("image"))
        #label = QLabel("hello", self)
        #label.setFont(QFont("Arial",40))
        #label.setGeometry(0, 0 ,500,100)
        #label.setStyleSheet("color: #246596;"
                            #"background-color:#c255bb;"
                            #"font-weight: semi bold;"
                            #"font-style: italic;"
                            #"text-decoration: underline; ")
        #label1 = QLabel(self)
        #label1.setGeometry(0,0,500 ,100)
        # pixmap = QPixmap("image.jpg")
        #label1.setPixmap(pixmap)
        #label.setScaledContents(True)
        #label.setGeometry(0,0,label.width(),label.height())
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignHCenter)
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignCenter)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        label1 = QLabel("#1",self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red; ")
        label2.setStyleSheet("background-color: blue; ")
        label3.setStyleSheet("background-color: green; ")
        label4.setStyleSheet("background-color: gold; ")
        label5.setStyleSheet("background-color: silver; ")


        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)


        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
