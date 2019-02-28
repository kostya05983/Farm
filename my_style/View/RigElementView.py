from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import *


class RigElementView(QWidget):
    WIDTH = 1600
    HEIGHT = 50

    def __init__(self, time_work, name, production_date, capital_date, next_repair, width, height):
        super().__init__()
        self.time_work = time_work
        self.name = name
        self.production_date = production_date
        self.capital_date = capital_date
        self.next_repair = next_repair
        self.width = width
        self.height = height
        self.h_layout = QHBoxLayout()
        self.init_main_layout()
        self.init_gui()
        self.show_labels()

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

    def show_labels(self):
        self.add_label(str(self.time_work))
        self.add_label(self.name)
        self.add_label(str(self.production_date))
        self.add_label(str(self.capital_date))
        self.add_label(str(self.next_repair))
        self.add_label(str(self.width))
        self.add_label(str(self.height))

    def add_label(self, str):
        label = QLabel(str)
        label.setAlignment(Qt.AlignCenter)
        label.setMinimumHeight(self.HEIGHT)
        self.h_layout.addWidget(label)
