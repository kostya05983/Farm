import os
from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QHBoxLayout, QLabel, QDialog, QLineEdit, \
    QPushButton

from admin.Controller.AddRigConrtoller import AddRigController
from admin.Model.AddRigModel import AddRigModel
from PyQt5.QtCore import *


class AddRigView(QDialog):
    HEIGHT = 190
    WIDTH = 430
    stacked_widgets = None

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddRigModel()
        self.controller = AddRigController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.technique_combo_box = QComboBox()
        self.location_combo_box = QComboBox()
        self.time_line = QLineEdit()
        self.init_gui()
        self.init_main_layout()
        self.init_inputs_forms()

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

    def init_inputs_forms(self):
        self.add_technique_combo_box()
        self.add_location_combo_box()
        self.init_input_time_work()
        self.init_ok_button()

    def add_technique_combo_box(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Техника")
        h_layout.addWidget(label)

        techniques = self.model.get_technique()
        for (id, text) in techniques:
            self.technique_combo_box.addItem(text, id)
        h_layout.addWidget(self.technique_combo_box)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def add_location_combo_box(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Участок")
        h_layout.addWidget(label)

        locations = self.model.get_locations()
        for (id, text) in locations:
            self.location_combo_box.addItem(text, id)
        h_layout.addWidget(self.location_combo_box)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def init_input_time_work(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel("Время работы")
        h_layout.addWidget(label)
        self.time_line.setMaximumWidth(200)
        self.time_line.setStyleSheet("background-color:#888888")
        h_layout.addWidget(self.time_line)
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
        self.update()
        self.close()
