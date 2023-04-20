import sys
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class mainWidget(QWidget):
    def __init__(self, msg):
        super().__init__()
        self.label = QLabel(msg)
        self.button = QPushButton("click")
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWidget("msg")
    window.show()
    window2 =mainWidget("msg2")
    window2.show()
    app.exec()
    print("hello world")