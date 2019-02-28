from functools import partial

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel, QPushButton, QDialog

from PyQt5.QtCore import *

from admin.Controller.LoginController import LoginController
from admin.Model.LoginModel import LoginModel
from admin.View.QDialogView import QDialogView


class LoginView(QDialogView):
    WIDTH = 400
    HEIGHT = 120

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.model = LoginModel()
        self.controller = LoginController(self, self.model)
        self.init_main_layout()
        self.init_gui()
        self.login = QLineEdit()
        self.password = QLineEdit()
        self.init_input_forms()
        self.init_ok_button()

    def init_input_forms(self):
        self.init_login()
        self.init_password()

    def init_login(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Логин")
        h_layout.addWidget(label)
        self.login.setStyleSheet("margin-left:10 px")
        h_layout.addWidget(self.login)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget, 0, Qt.AlignCenter)

    def init_password(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Пароль")
        h_layout.addWidget(label)
        self.password.setEchoMode(QLineEdit.Password)
        h_layout.addWidget(self.password)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget, 0, Qt.AlignCenter)

    def init_ok_button(self):
        ok_button = QPushButton("Войти")
        ok_button.setIconSize(QSize(30, 30))
        ok_button.setStyleSheet("margin-top:10px;"
                                "font-size:16px")
        ok_button.clicked.connect(partial(self.controller.check))
        self.v_layout.addWidget(ok_button, 0, Qt.AlignCenter)

    def close_window(self):
        self.close()
