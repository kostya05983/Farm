import os
from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolButton

from admin.Controller.ProductController import ProductController


class ProductView(QWidget):

    def __init__(self, id_sql, name, path, price, session_id):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.id_sql = id_sql
        self.name = name
        self.path = path
        self.price = price
        self.session_id = session_id
        self.controller = ProductController(self)
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
        button.clicked.connect(
            partial(self.controller.show_dialog, self.id_sql, self.name, self.price, self.session_id))
        self.v_layout.addWidget(button)

    def add_name(self):
        label = QLabel(self.name)
        self.v_layout.addWidget(label, 0, Qt.AlignBottom)
