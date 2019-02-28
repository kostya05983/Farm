from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QPushButton

from admin.Controller.AddCultureController import AddCultureController
from admin.Model.AddCultureModel import AddCultureModel
from admin.View.QDialogView import QDialogView


class AddCultureView(QDialogView):
    HEIGHT = 130
    WIDTH = 430

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddCultureModel()
        self.v_layout = QVBoxLayout()
        self.controller = AddCultureController(self.model, self)
        self.culture = QLineEdit()
        self.amount = QLineEdit()
        self.price = QLineEdit()
        self.init_gui()
        self.init_main_layout()
        self.init_input_form()
        self.init_ok_button()

    def init_input_form(self):
        self.add_input_line("Название культуры", self.culture)
        self.add_input_line("Количество культуры на складе кг", self.amount)
        self.add_input_line("Ценна за единицу в рублях", self.price)

    def init_ok_button(self):
        add_button = QPushButton("Выполнить")
        add_button.setStyleSheet("margin-top:10px;"
                                 "font-size:16px")
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))
