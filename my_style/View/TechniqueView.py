from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from admin.Controller.TechniqueController import TechniqueController
from admin.Model.TechniqueModel import TechniqueModel


class TechniqueView(QWidget):
    HEIGHT = 1080
    WIDTH = 1600
    isLogin = True
    name = "kostya05983"

    stacked_widgets = None

    def __init__(self):
        super().__init__()
        self.model = TechniqueModel()
        self.controller = TechniqueController(self)
        self.v_layout = QVBoxLayout()
        self.grid_layout = None
        self.init_main_layout()
        self.init_gui()
        self.init_grid_technique()

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.setContentsMargins(0, 0, 0, 0)

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)

    def init_grid_technique(self):
        qwidget = QWidget()
        qwidget.setStyleSheet("margin-left:20px")
        technique_list = self.model.get_technique()

        grid_layout = QGridLayout()
        qwidget.setLayout(grid_layout)

        for i in range(len(technique_list)):
            grid_layout.addWidget(technique_list[i], i // 4, i % 4)
        self.grid_layout = grid_layout
        self.v_layout.addWidget(qwidget, 0)

