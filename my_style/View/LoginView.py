import os
from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel, QPushButton

from PyQt5.QtCore import *

from admin.Controller.LoginController import LoginController
from admin.Model.LoginModel import LoginModel


class LoginView(QWidget):
    WIDTH = 400
    HEIGHT = 130

    stacked_widgets = None

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

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.v_layout.setSpacing(0)

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)
        self.setStyleSheet("background-color:#424A52;"
                           "color:#FFFFFF")

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
        ok_icon = QIcon(os.getcwd() + "/icons/ok_icon.png")
        ok_button = QPushButton(ok_icon, "")
        ok_button.setIconSize(QSize(30, 30))
        ok_button.setFlat(True)
        ok_button.clicked.connect(partial(self.controller.check))
        self.v_layout.addWidget(ok_button, 0, Qt.AlignCenter)

    def show_stacked_widgets(self):
        # self.stacked_widgets.setParent(None)
        self.stacked_widgets.widget(1).show()
        self.stacked_widgets.show()

    def close_window(self):
        self.close()
