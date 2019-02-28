from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import *


class TreatyElementView(QWidget):
    WIDTH = 1600
    HEIGHT = 50

    def __init__(self, delivery_date, delivery_condition, payment_condition, culture_name, organization_name,
                 requisites, email, head, post_address, legal_address, site):
        super().__init__()
        self.delivery_date = delivery_date
        self.delivery_condition = delivery_condition
        self.payment_condition = payment_condition
        self.culture_name = culture_name
        self.organization_name = organization_name
        self.requisites = requisites
        self.email = email
        self.head = head
        self.post_address = post_address
        self.legal_address = legal_address
        self.site = site
        self.h_layout = QHBoxLayout()
        self.init_gui()
        self.init_main_layout()
        self.add_labels()

    def init_main_layout(self):
        self.h_layout.setAlignment(Qt.AlignTop)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(0)
        self.h_layout.setDirection(QHBoxLayout.LeftToRight)

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.h_layout)
        self.setStyleSheet("background-color: #424A52;"
                           "color:#FFFFFF;"
                           "text-align:center;"
                           "border: 1px outset #000000;")

    def add_labels(self):
        self.add_label(str(self.delivery_date))
        self.add_label(self.delivery_condition)
        self.add_label(self.payment_condition)
        self.add_label(self.culture_name)
        self.add_label(self.organization_name)
        self.add_label(self.requisites)
        self.add_label(self.email)
        self.add_label(self.head)
        self.add_label(self.post_address)
        self.add_label(self.legal_address)
        self.add_label(self.site)

    def add_label(self, str):
        label = QLabel(str)
        label.setAlignment(Qt.AlignCenter)
        label.setMinimumHeight(self.HEIGHT)
        self.h_layout.addWidget(label)
