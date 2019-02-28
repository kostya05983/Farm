from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QAbstractItemView

from admin.Controller.CreateUserController import CreateUserController
from admin.Model.CreateUserModel import CreateUserModel
from admin.Settings import Settings
from admin.View.ViewWidget import ViewWidget


class CreateUserView(ViewWidget):

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.model = CreateUserModel(self)
        self.controller = CreateUserController(self.model, self)
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