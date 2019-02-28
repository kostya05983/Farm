from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QComboBox, QPushButton, QDateEdit

from admin.Controller.AddTechniqueController import AddTechniqueController
from admin.Model.AddTechniqueModel import AddTechniqueModel
from admin.View.CommonFunctions import add_date
from admin.View.QDialogView import QDialogView


class AddTechniqueView(QDialogView):
    WIDTH = 430
    HEIGHT = 270

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddTechniqueModel()
        self.controller = AddTechniqueController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.name = QLineEdit()
        self.production_date = QDateEdit()
        self.capital_date = QDateEdit()
        self.next_repair = QDateEdit()
        self.state = QComboBox()
        self.init_gui()
        self.init_main_layout()
        self.init_inputs_forms()
        self.init_ok_button()

    def init_inputs_forms(self):
        self.add_input_line("Название техники", self.name)
        add_date("Дата производства", self.production_date, self.v_layout)
        add_date("Дата капитального ремонта", self.capital_date, self.v_layout)
        add_date("Дата следующего ремонта", self.next_repair, self.v_layout)
        self.add_combo_box("Состояние", self.model.data_state, self.state)

    def init_ok_button(self):
        add_button = QPushButton("Выполнить")
        add_button.setStyleSheet("margin-top:10px;"
                                 "font-size:16px")
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))
