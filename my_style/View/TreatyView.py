from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import *

from admin.Controller.TreatyController import TreatyController
from admin.Model.TreatyModel import TreatyModel


class TreatyView(QWidget):
    HEIGHT = 1080
    WIDTH = 1600

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.model = TreatyModel()
        self.controller = TreatyController(self, self.model)
        self.init_gui()
        self.init_main_layout()
        self.show_labels()
        self.show_treaties()

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)
        self.setContentsMargins(0, 0, 0, 0)

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.v_layout.setSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)

    def show_labels(self):
        widget = QWidget()
        layout = QHBoxLayout()
        self.add_label(layout, "Дата доставки")
        self.add_label(layout, "Условие доставки")
        self.add_label(layout, "Условие оплаты")
        self.add_label(layout, "Название культуры")
        self.add_label(layout, "Имя организации")
        self.add_label(layout, "Реквизиты")
        self.add_label(layout, "Email")
        self.add_label(layout, "Глава")
        self.add_label(layout, "Почтовый адресс")
        self.add_label(layout, "Юридический адресс")
        self.add_label(layout, "Сайт")
        widget.setLayout(layout)
        widget.setStyleSheet("background-color:#424a52;"
                             "color:#FFFFFF;")
        self.v_layout.addWidget(widget)

    def show_treaties(self):
        result = self.model.get_treaties()
        if len(result) != 0:
            for view in result:
                self.v_layout.addWidget(view)
        else:
            self.show_nothing()

    def add_label(self, layout, str):
        label = QLabel(str)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    def show_nothing(self):
        label = QLabel("Ничего не найдено")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size:20px;")
        self.v_layout.addWidget(label)
