from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QAbstractItemView, \
    QTableView

from admin.Settings import Settings
from admin.Controller.PlanCropRotationController import PlanCropRotationController
from admin.Model.PlanCropRotationModel import PlanCropRotationModel
from PyQt5.QtCore import *

from admin.View.ViewWidget import ViewWidget


class PlanCropRotationView(ViewWidget):
    year = None

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.q_line_edit = QLineEdit()
        self.model = PlanCropRotationModel(self)
        self.table = QTableView()
        self.controller = PlanCropRotationController(self, self.model)
        self.init_gui()
        self.init_main_layout()
        self.init_input_form()

    def init_input_form(self):
        label = QLabel()
        label.setText("Введите год")
        label.setStyleSheet("font-size:20px;"
                            "color:#FFFFFF")
        self.v_layout.addWidget(label, 0, Qt.AlignCenter)
        self.q_line_edit.setMaximumWidth(100)
        self.q_line_edit.setStyleSheet("text-align:center;"
                                       "color: #FFFFFF")
        self.q_line_edit.keyReleaseEvent = self.controller.key_input_form_event
        self.v_layout.addWidget(self.q_line_edit, 0, Qt.AlignCenter)

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

    def show_nothing(self):
        label = QLabel("Ничего не найдено")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size:20px;"
                            "color: #FFFFFF;"
                            "background-color:#505052")
        self.v_layout.addWidget(label)

    def update_view(self):
        self.clear_layout()
        if self.year is not None:
            self.model.update(self.year)
            self.init_input_form()
            self.show_table()
        else:
            self.init_input_form()

    def clear_layout(self):
        for i in reversed(range(self.v_layout.count())):
            self.v_layout.itemAt(i).widget().setParent(None)
