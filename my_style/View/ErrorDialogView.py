from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import *


class ErrorDialogView(QDialog):
    HEIGHT = 50
    WIDTH = 430

    def __init__(self, text):
        super(ErrorDialogView, self).__init__()
        self.text = text
        self.v_layout = QVBoxLayout()
        self.init_gui()
        self.init_main_layout()
        self.init_label()

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color: #424A52;"
                           "color:#FFFFFF")

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.v_layout.setSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)

    def init_label(self):
        label = QLabel(self.text)
        label.setStyleSheet("font-size:24px")
        self.v_layout.addWidget(label, 0, Qt.AlignCenter)
