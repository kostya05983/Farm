import os
from functools import partial
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import *

from admin.Controller.RigController import RigController
from admin.Model.RigModel import RigModel


class RigView(QWidget):
    HEIGHT = 1080
    WIDTH = 1600

    def __init__(self):
        super().__init__()
        self.model = RigModel()
        self.controller = RigController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.init_gui()
        self.init_main_layout()
        self.show_labels()
        self.controller.show_rigs()
        self.init_add_button()
        self.show()

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)
        self.setContentsMargins(0, 0, 0, 0)

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.v_layout.setSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)

    def show_rigs(self):
        for view in self.model.get_rigs():
            self.v_layout.addWidget(view)

    def show_labels(self):
        widget = QWidget()
        layout = QHBoxLayout()
        self.add_label(layout, "Время работы")
        self.add_label(layout, "Имя")
        self.add_label(layout, "Произведена")
        self.add_label(layout, "Дата ремонта")
        self.add_label(layout, "Дата починки")
        self.add_label(layout, "Длина участка")
        self.add_label(layout, "Ширина участка")
        widget.setLayout(layout)

        widget.setStyleSheet("background-color: #424A52;"
                             "color: #FFFFFF;"
                             "text-align:center;")
        self.v_layout.addWidget(widget)

    def show_nothing(self):
        label = QLabel("Ничего не найдено")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size:20px;")
        self.v_layout.addWidget(label)

    def add_label(self, layout, str):
        label = QLabel(str)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    def init_add_button(self):
        icon = QIcon(os.getcwd() + "/icons/add_icon.png")
        add_button = QPushButton(icon, "")
        add_button.setIconSize(QSize(40, 40))
        add_button.setFlat(True)
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.show_add_rig_view))

    def update_view(self):
        self.clear_layout()
        self.show_labels()
        self.controller.show_rigs()
        self.init_add_button()
        self.update()

    def clear_layout(self):
        for i in reversed(range(self.v_layout.count())):
            self.v_layout.itemAt(i).widget().setParent(None)
