from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QWidget, QLabel, QPushButton, QComboBox, \
    QCalendarWidget, QDateEdit

from admin.Controller.AddTreatyController import AddTreatyController
from admin.Model.AddTreatyModel import AddTreatyModel
from admin.View.CommonFunctions import add_date
from admin.View.QDialogView import QDialogView


class AddTreatyView(QDialogView):
    WIDTH = 430
    HEIGHT = 580

    def __init__(self, update):
        super().__init__()
        self.update = update
        self.model = AddTreatyModel()
        self.controller = AddTreatyController(self, self.model)
        self.v_layout = QVBoxLayout()
        self.delivery_date = QDateEdit()
        self.delivery_condition = QLineEdit()
        self.payment_condition = QLineEdit()
        self.culture_name = QComboBox()
        self.culture_amount = QLineEdit()
        self.organization_name = QLineEdit()
        self.requisites = QLineEdit()
        self.email = QLineEdit()
        self.head = QLineEdit()
        self.post_address = QLineEdit()
        self.legal_address = QLineEdit()
        self.site = QLineEdit()
        self.phone_number = QLineEdit()
        self.init_gui()
        self.init_main_layout()
        self.init_inputs_forms()

    def init_inputs_forms(self):
        add_date("Дата доставки", self.delivery_date, self.v_layout)
        self.add_input_line("Условия доставки", self.delivery_condition)
        self.add_input_line("Условие оплаты", self.payment_condition)
        self.add_combo_box("Название культуры", self.model.get_cultures, self.culture_name)
        self.add_input_line("Количество культуры", self.culture_amount)
        self.add_input_line("Имя организации", self.organization_name)
        self.add_input_line("Реквизиты", self.requisites)
        self.add_input_line("email", self.email)
        self.add_input_line("Глава", self.head)
        self.add_input_line("Почтовый адресс", self.post_address)
        self.add_input_line("Юридический адресс", self.legal_address)
        self.add_input_line("Сайт", self.site)
        self.add_input_line("Телефонный номер", self.phone_number)
        self.init_ok_button()

    def init_ok_button(self):
        add_button = QPushButton("Выполнить")
        add_button.setStyleSheet("margin-top:10px;"
                                 "font-size:16px")
        self.v_layout.addWidget(add_button, 0, Qt.AlignCenter)
        add_button.clicked.connect(partial(self.controller.add_to_db))
