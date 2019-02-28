from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QAbstractItemView

from admin.Controller.TreatyController import TreatyController
from admin.Model.TreatyModel import TreatyModel
from admin.Settings import Settings
from admin.View.ViewWidget import ViewWidget


class TreatyView(ViewWidget):
    WIDTH = Settings.WIDTH.value+600

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.table = QTableView()
        self.model = TreatyModel(self)
        self.controller = TreatyController(self, self.model)
        self.init_gui()
        self.init_main_layout()
        self.show_table()

    def show_table(self):
        self.table.setStyleSheet("selection-background-color: #0f5b8d;"
                                 "background-color: #505052;"
                                 "color: #f0f4f7;"
                                 "font-size:14px;"
                                 "gridline-color:#324148;"
                                 "text-align:center;")
        self.table.horizontalHeader().setStyleSheet("background-color:#3b3b3d")
        self.table.keyReleaseEvent = self.controller.key_input
        self.table.setModel(self.model)
        for i in range(12):
            self.table.setColumnWidth(i, 240)
        self.table.setModel(self.model)
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.v_layout.addWidget(self.table)

    def update_view(self):
        self.model.get_treaties()
        self.clear_layout()
        self.show_table()
