from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QComboBox, QPushButton

from admin.Controller.AddCropRotationController import AddCropRotationController
from admin.Model.AddCropRotationModel import AddCropRotationModel
from admin.View.QDialogView import QDialogView


class AddCropRotationView(QDialogView):
    HEIGHT = 780
    WIDTH = 430

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddCropRotationModel()
        self.controller = AddCropRotationController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.start_year = QLineEdit()
        self.culture_combo_box = [QComboBox(), QComboBox(), QComboBox(), QComboBox(), QComboBox()]
        self.location_combo_box = [QComboBox(), QComboBox(), QComboBox(), QComboBox(), QComboBox()]
        self.amount_seed = [QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit()]
        self.init_gui()
        self.init_main_layout()
        self.init_input_forms()

    def init_input_forms(self):
        self.add_input_line("Введите первый год пятилетки", self.start_year)
        strs_label = ["Первый год", "Второй год", "Третий год", "Четвертый год", "Пятый год"]
        for i in range(5):
            self.add_label(strs_label[i])
            self.add_combo_box("Выберите культуру", self.model.get_cultures, self.culture_combo_box[i])
            self.add_combo_box("Выберите землю", self.model.get_locations, self.location_combo_box[i], )
            self.add_input_line("Введите количество посева", self.amount_seed[i])
        self.init_ok_button()

    def add_label(self, label_str):
        label = QLabel(label_str)
        label.setAlignment(Qt.AlignCenter)
        self.v_layout.addWidget(label)

    def init_ok_button(self):
        add_button = QPushButton("Выполнить")
        add_button.setStyleSheet("margin-top:10px;"
                                 "font-size:16px")
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))
