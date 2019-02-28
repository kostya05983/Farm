from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QLineEdit, \
    QPushButton, QDateEdit

from admin.Controller.AddRigConrtoller import AddRigController
from admin.Model.AddRigModel import AddRigModel
from admin.View.CommonFunctions import add_date
from admin.View.QDialogView import QDialogView


class AddRigView(QDialogView):
    HEIGHT = 250
    WIDTH = 430

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddRigModel()
        self.controller = AddRigController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.technique_combo_box = QComboBox()
        self.location_combo_box = QComboBox()
        self.user_combo_box = QComboBox()
        self.time_line = QLineEdit()
        self.date = QDateEdit()
        self.init_gui()
        self.init_main_layout()
        self.init_inputs_forms()

    def init_inputs_forms(self):
        self.add_combo_box("Техника", self.model.get_technique, self.technique_combo_box)
        self.add_combo_box("Участок", self.model.get_locations, self.location_combo_box)
        self.add_combo_box("Назначена", self.model.get_users, self.user_combo_box)
        self.add_input_line("Время работы в часах", self.time_line)
        add_date("Дата", self.date, self.v_layout)
        self.init_ok_button()

    def init_ok_button(self):
        add_button = QPushButton("Выполнить")
        add_button.setStyleSheet("margin-top:10px;"
                                 "font-size:16px")
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))
