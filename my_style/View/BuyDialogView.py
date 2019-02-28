import os
from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import *

from admin.Controller.BuyDialogController import BuyDialogController
from admin.Model.BuyDialogModel import BuyDialogModel


class BuyDialogView(QDialog):
    HEIGHT = 140
    WIDTH = 430

    def __init__(self, id, name, price, session_id):
        super(BuyDialogView, self).__init__()
        self.id = id
        self.name = name
        self.price = price
        self.session_id = session_id
        self.amount_line = QLineEdit()
        self.model = BuyDialogModel()
        self.controller = BuyDialogController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.label_price = QLabel("%s руб" % str(price))
        self.init_gui()
        self.init_main_layout()
        self.init_input_forms()

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

    def init_input_forms(self):
        self.init_amount_form()
        self.init_price_form()
        self.init_ok_button()

    def init_amount_form(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Количество")
        h_layout.addWidget(label)
        self.amount_line.setText("1")
        self.amount_line.setMaximumWidth(200)
        self.amount_line.setStyleSheet("background-color:#888888")
        self.amount_line.keyReleaseEvent = self.controller.key_amount_form_event
        h_layout.addWidget(self.amount_line)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def init_price_form(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Цена")
        h_layout.addWidget(label)
        h_layout.addWidget(self.label_price)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def update_price(self, price):
        self.label_price.setText("%s руб" % str(price))

    def init_ok_button(self):
        icon = QIcon(os.getcwd() + "/icons/ok_icon.png")
        add_button = QPushButton(icon, "")
        add_button.setIconSize(QSize(40, 40))
        add_button.setFlat(True)
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))

    def close_window(self):
        self.update()
        self.close()
