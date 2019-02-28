from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QPushButton

from admin.Controller.AddLocationController import AddLocationController
from admin.Model.AddLocationModel import AddLocationModel
from admin.View.QDialogView import QDialogView


class AddLocationView(QDialogView):
    HEIGHT = 130
    WIDTH = 430

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddLocationModel()
        self.v_layout = QVBoxLayout()
        self.controller = AddLocationController(self.model, self)
        self.width = QLineEdit()
        self.height = QLineEdit()
        self.init_gui()
        self.init_main_layout()
        self.init_input_form()
        self.init_ok_button()

    def init_input_form(self):
        self.add_input_line("Ширина участка метров", self.width)
        self.add_input_line("Длина участка в метрах", self.height)

    def init_ok_button(self):
        add_button = QPushButton("Выполнить")
        add_button.setStyleSheet("margin-top:10px;"
                                 "font-size:16px")
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))
