from PyQt5.QtWidgets import QVBoxLayout, QTableView, QAbstractItemView

from admin.Controller.RigController import RigController
from admin.Model.RigModel import RigModel
from admin.View.ViewWidget import ViewWidget


class RigView(ViewWidget):

    def __init__(self):
        super().__init__()
        self.model = RigModel(self)
        self.controller = RigController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.table = QTableView()
        self.init_gui()
        self.init_main_layout()
        self.show_table()
        self.show()

    def show_rigs(self):
        for view in self.model.get_rigs():
            self.v_layout.addWidget(view)

    def show_table(self):
        self.table = QTableView()
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
            self.table.setColumnWidth(i, 200)
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.v_layout.addWidget(self.table)

    def update_view(self):
        self.model.update_rigs()
        self.clear_layout()
        self.show_table()
