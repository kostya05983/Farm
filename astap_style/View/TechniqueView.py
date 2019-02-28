from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTableView, QAbstractItemView

from admin.Controller.TechniqueController import TechniqueController
from admin.Model.TechniqueModel import TechniqueModel
from admin.Settings import Settings
from admin.View.ViewWidget import ViewWidget


class TechniqueView(ViewWidget):
    isLogin = True
    name = "kostya05983"

    stacked_widgets = None

    def __init__(self):
        super().__init__()
        self.model = TechniqueModel(self)
        self.controller = TechniqueController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.table = QTableView()
        self.grid_layout = None
        self.init_main_layout()
        self.init_gui()
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
        for i in range(4):
            self.table.setColumnWidth(i, 240)
        self.table.keyReleaseEvent = self.controller.key_input
        self.table.setModel(self.model)
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.v_layout.addWidget(self.table)

    def update_view(self):
        self.model.get_technique()
        self.clear_layout()
        self.show_table()

