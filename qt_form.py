from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtWidgets import QPushButton
import numpy as np
import cv2 as cv

class AdjustDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.msg = "Hello world!"
        self.lbl = QLabel(self.msg)

        self.cmd = QPushButton("Click")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lbl)
        self.layout.addWidget(self.cmd)

        self.cmd.clicked.connect(self.load_img)
    
    @QtCore.Slot()
    def load_img(self):
        self.read_frame = cv.imread("jam4.jpg")
        cv.imshow("OpenCV", self.read_frame)

if __name__ == "__main__":
    app = QApplication([])
    form = AdjustDialog()
    form.resize(300,300)
    form.show()

    app.exec_()
