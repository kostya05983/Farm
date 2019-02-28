import os
from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout

from admin.Controller.PlanCropRotationController import PlanCropRotationController
from admin.Model.PlanCropRotationModel import PlanCropRotationModel


class PlanCropRotationView(QWidget):
    WIDTH = 1600
    HEIGHT = 1080

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.q_line_edit = QLineEdit()
        self.model = PlanCropRotationModel()
        self.controller = PlanCropRotationController(self, self.model)
        self.init_gui()
        self.init_main_layout()
        self.init_input_form()
        self.init_add_button()

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.v_layout.setSpacing(0)

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)

    def init_input_form(self):
        label = QLabel()
        label.setText("Введите год")
        label.setStyleSheet("font-size:20px")
        self.v_layout.addWidget(label, 0, Qt.AlignCenter)
        self.q_line_edit.setMaximumWidth(100)
        self.q_line_edit.setStyleSheet("text-align:center;")
        self.q_line_edit.keyReleaseEvent = self.controller.key_input_form_event
        self.v_layout.addWidget(self.q_line_edit, 0, Qt.AlignCenter)

    def show_labels(self):
        result = QWidget()
        result.setStyleSheet("background-color: #424a52;"
                             "color:#FFFFFF;"
                             "text-align:center;")
        up_layout = QHBoxLayout()
        self.add_label(up_layout, "Длина")
        self.add_label(up_layout, "Ширина")
        self.add_label(up_layout, "Название посева")
        self.add_label(up_layout, "Засеяно")
        self.add_label(up_layout, "Собрано")
        result.setLayout(up_layout)
        self.v_layout.addWidget(result)

    def add_label(self, layout, name):
        label = QLabel(name)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    def show_crop_rotation(self):
        crop_rotation_data = self.model.get_crop_rotation()
        for crop_view in crop_rotation_data:
            self.v_layout.addWidget(crop_view)

    def clear(self):
        for i in reversed(range(self.v_layout.count())):
            self.v_layout.itemAt(i).widget().setParent(None)

    def show_nothing(self):
        label = QLabel("Ничего не найдено")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size:20px;")
        self.v_layout.addWidget(label)

    def init_add_button(self):
        icon = QIcon(os.getcwd() + "/icons/add_icon.png")
        add_button = QPushButton(icon, "")
        add_button.setIconSize(QSize(40, 40))
        add_button.setFlat(True)
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.show_add_crop_rotation_view))

