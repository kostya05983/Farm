import os
from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel, QVBoxLayout, QDialog, QPushButton
from PyQt5.QtCore import *

from admin.Controller.DialogTreatyController import DialogTreatyController
from admin.Model.DialogTreatyModel import DialogTreatyModel


class DialogTreatyView(QDialog):
    HEIGHT = 460
    WIDTH = 330

    def __init__(self, session_id):
        super().__init__()
        self.session_id = session_id
        self.model = DialogTreatyModel()
        self.controller = DialogTreatyController(self, self.model)
        self.h_layout = QHBoxLayout()
        self.delivery_condition = QLineEdit()
        self.payment_condition = QLineEdit()
        self.name = QLineEdit()
        self.requisites = QLineEdit()
        self.email = QLineEdit()
        self.head = QLineEdit()
        self.post_address = QLineEdit()
        self.legal_address = QLineEdit()
        self.site = QLineEdit()
        self.phone_number = QLineEdit()
        self.v_layout = QVBoxLayout()
        self.init_main_layout()
        self.init_gui()
        self.init_input()

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setSpacing(0)
        self.v_layout.setDirection(QHBoxLayout.TopToBottom)

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)
        self.setStyleSheet("background-color: #424a52;")

    def init_input(self):
        self.add_form("Название организации", self.name)
        self.add_form("Условия доставки", self.delivery_condition)
        self.add_form("Условия оплаты", self.payment_condition)
        self.add_form("Реквизиты", self.requisites)
        self.add_form("email", self.email)
        self.add_form("Генеральный директор", self.head)
        self.add_form("Почтовый адресс", self.post_address)
        self.add_form("Юридический адресс", self.legal_address)
        self.add_form("Сайт", self.site)
        self.add_form("Телефонный номер", self.phone_number)
        self.init_ok_button()

    def init_ok_button(self):
        ok_icon = QIcon(os.getcwd() + "/icons/ok_icon.png")
        ok_button = QPushButton(ok_icon, "")
        ok_button.setIconSize(QSize(30, 30))
        ok_button.setFlat(True)
        ok_button.clicked.connect(partial(self.controller.add_to_db))
        self.v_layout.addWidget(ok_button, 0, Qt.AlignCenter)

    def add_form(self, str, line):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel(str)
        h_layout.addWidget(label)
        line.setMaximumWidth(100)
        line.setStyleSheet("background-color:#888888")
        h_layout.addWidget(line)
        widget.setLayout(h_layout)
        widget.setStyleSheet("background-color: #424a52;"
                             "color:#FFFFFF;"
                             "text-align:center;")
        self.v_layout.addWidget(widget)

    def close_window(self):
        self.close()
