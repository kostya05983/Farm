from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLineEdit, QComboBox, QWidget, QHBoxLayout, QLabel

from admin.Controller.AddUserController import AddUserController
from admin.Model.AddUserModel import AddUserModel
from admin.View.QDialogView import QDialogView


class AddUserView(QDialogView):
    WIDTH = 430
    HEIGHT = 170

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddUserModel()
        self.controller = AddUserController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.login = QLineEdit()
        self.password = QLineEdit()
        self.role = QComboBox()
        self.init_gui()
        self.init_main_layout()
        self.init_inputs_form()
        self.init_ok_button()

    def init_inputs_form(self):
        self.add_input_line("Логин", self.login)
        self.add_input_password("Пароль", self.password)
        self.add_combo_box("Роль", self.model.roles, self.role)

    def add_input_password(self, str, line):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel(str)
        h_layout.addWidget(label)
        line.setMaximumWidth(200)
        line.setEchoMode(QLineEdit.Password)
        line.setStyleSheet("background-color: #888888")
        h_layout.addWidget(line)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def init_ok_button(self):
        add_button = QPushButton("Выполнить")
        add_button.setStyleSheet("margin-top:10px;"
                                 "font-size:16px")
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))
