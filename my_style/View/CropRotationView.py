import os
from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class CropRotationView(QWidget):
    WIDTH = 1600
    HEIGHT = 50

    def __init__(self, length, width, name_seed, amount_seed, amount_collected):
        super().__init__()
        self.length = length
        self.width = width
        self.name_seed = name_seed
        self.amount_seed = amount_seed
        self.amount_collected = amount_collected
        self.h_layout = QHBoxLayout()
        self.init_gui()
        self.init_main_layout()
        self.add_labels()

    def init_main_layout(self):
        self.h_layout.setAlignment(Qt.AlignTop)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(0)
        self.h_layout.setDirection(QHBoxLayout.LeftToRight)

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.h_layout)
        self.setStyleSheet("background-color: #424A52;"
                           "color:#FFFFFF;"
                           "text-align:center;"
                           "border: 1px outset #000000;")

    def add_labels(self):
        self.add_label(str(self.length))
        self.add_label(str(self.width))
        self.add_label(self.name_seed)
        self.add_label(str(self.amount_seed))
        self.add_label(str(self.amount_collected))

    def add_label(self, str):
        label = QLabel(str)
        label.setAlignment(Qt.AlignCenter)
        label.setMinimumHeight(self.HEIGHT)
        self.h_layout.addWidget(label)


