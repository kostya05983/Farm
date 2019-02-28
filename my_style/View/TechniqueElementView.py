import os
from PyQt5.QtCore import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolButton, QLabel


class TechniqueElementView(QWidget):

    def __init__(self, id_sql, name, path):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.id_sql = id_sql
        self.name = name
        self.path = path
        self.init_gui()

    def init_gui(self):
        self.setLayout(self.v_layout)
        self.layout().setAlignment(Qt.AlignTop)
        self.add_picture()

    def add_picture(self):
        picture = QIcon(os.getcwd() + self.path)
        button = QToolButton()
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setIcon(picture)
        button.setStyleSheet("border:0px;"
                             "font-size:16px")
        button.setText(self.name)
        button.setIconSize(QSize(320, 270))
        self.v_layout.addWidget(button)

    def add_name(self):
        label = QLabel(self.name)
        self.v_layout.addWidget(label, 0, Qt.AlignBottom)