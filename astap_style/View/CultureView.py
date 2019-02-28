from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QAbstractItemView, QTableView

from admin.Controller.CultureController import CultureController
from admin.Model.CultureModel import CultureModel
from admin.Settings import Settings
from admin.View.ViewWidget import ViewWidget


class CultureView(ViewWidget):

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.model = CultureModel(self)
        self.controller = CultureController(self.model, self)
        self.init_gui()
        self.init_main_layout()
        self.table = QTableView()
        self.show_table()

    def show_table(self):
        self.table.setStyleSheet("selection-background-color: #0f5b8d;"
                                 "background-color: #505052;"
                                 "color: #f0f4f7;"
                                 "font-size:14px;"
                                 "gridline-color:#324148;"
                                 "text-align:center;")
        self.table.horizontalHeader().setStyleSheet("background-color:#3b3b3d")
        self.table.setModel(self.model)
        self.table.keyReleaseEvent = self.controller.key_input
        for i in range(4):
            self.table.setColumnWidth(i, 240)
        self.table.setModel(self.model)
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.v_layout.addWidget(self.table)

    def update_view(self):
        self.model.update()
        self.clear_layout()
        self.show_table()