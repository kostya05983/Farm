import os
from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel, QComboBox, QDialog, QPushButton

from admin.Controller.AddCropRotationController import AddCropRotationController
from admin.Model.AddCropRotationModel import AddCropRotationModel
from PyQt5.QtCore import *


class AddCropRotationView(QDialog):
    HEIGHT = 780
    WIDTH = 430
    stacked_widgets = None

    def __init__(self):
        super().__init__()
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
        self.init_start_year()
        strs_label = ["Первый год", "Второй год", "Третий год", "Четвертый год", "Пятый год"]
        for i in range(5):
            self.add_label(strs_label[i])
            self.init_combo_box("Выберите культуру", self.culture_combo_box[i], self.model.get_cultures)
            self.init_combo_box("Выберите землю", self.location_combo_box[i], self.model.get_locations)
            self.add_amount_seed("Введите количество посева", self.amount_seed[i])
        self.init_ok_button()

    def add_label(self, label_str):
        label = QLabel(label_str)
        label.setAlignment(Qt.AlignCenter)
        self.v_layout.addWidget(label)

    def add_amount_seed(self, label, line):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel(label)
        h_layout.addWidget(label)
        h_layout.addWidget(line)
        widget.setLayout(h_layout)
        line.setStyleSheet("background-color:#888888")
        line.setMaximumWidth(200)
        self.v_layout.addWidget(widget)

    def init_start_year(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Введите первый год пятилетки")
        h_layout.addWidget(label)
        h_layout.addWidget(self.start_year)
        self.start_year.setStyleSheet("background-color:#888888")
        self.start_year.setMaximumWidth(200)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def init_combo_box(self, label_str, combo_box, items_fun):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel(label_str)
        h_layout.addWidget(label)
        cultures = items_fun()
        for (id, name) in cultures:
            combo_box.addItem(name, id)

        h_layout.addWidget(combo_box)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def init_ok_button(self):
        icon = QIcon(os.getcwd() + "/icons/ok_icon.png")
        add_button = QPushButton(icon, "")
        add_button.setIconSize(QSize(40, 40))
        add_button.setFlat(True)
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))

    def close_window(self):
        self.close()
