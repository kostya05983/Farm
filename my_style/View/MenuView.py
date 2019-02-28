import os

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel

from admin.Controller.MenuController import MenuController


class MenuView(QWidget):
    HEIGHT = 1080
    WIDTH = 1600
    isLogin = True
    name = "kostya05983"

    stacked_widgets = None

    def __init__(self):
        super().__init__()
        self.h_layout = QHBoxLayout(self)
        self.controller = MenuController(self)
        self.init_gui()
        self.setLayout(self.h_layout)
        self.h_layout.setAlignment(Qt.AlignLeft)
        self.init_buttons()
        self.left_menu_layout = None

    def init_gui(self):
        self.h_layout.setDirection(QHBoxLayout.LeftToRight)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        widget = QWidget()
        widget.setFixedSize(QSize(self.WIDTH, self.HEIGHT))
        widget.setStyleSheet("background-color: #000000")
        self.add_block()

    def add_block(self):
        widget = QWidget()
        widget.setBaseSize(QSize(600, self.HEIGHT))
        widget.setMinimumWidth(400)
        v_layout = QVBoxLayout()
        v_layout.setDirection(QVBoxLayout.TopToBottom)
        widget.setLayout(v_layout)
        widget.setStyleSheet("background-color: #424A52;")
        self.h_layout.addWidget(widget)
        self.left_menu_layout = v_layout
        self.left_menu_layout.setSpacing(0)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setAlignment(Qt.AlignTop)

    def init_buttons(self):
        if self.isLogin:
            self.init_header_login()
            self.init_product_button()
            self.init_plan_button()
            self.init_graph_button()
            self.init_deal_button()
            self.init_technique_button()
            self.init_rig_button()
        else:
            self.init_product_button()

    def init_header_login(self):
        label = QLabel("Вы вошли как " + self.name)
        label.setStyleSheet("color: #FFFFFF;"
                            "font-size: 20px;"
                            "margin-left:10px;"
                            "margin-top:20px")
        self.left_menu_layout.addWidget(label, 0, Qt.AlignTop)

    def init_product_button(self):
        qwidget = QWidget()
        layout = QHBoxLayout()
        qwidget.setLayout(layout)

        qwidget.setStyleSheet("margin-left:15px")

        wheat_icon = QIcon(os.getcwd() + "/icons/wheat.png")
        wheat_button = QPushButton(wheat_icon, "")
        wheat_button.setIconSize(QSize(40, 40))
        wheat_button.setFlat(True)

        label = QLabel("Продукты")
        label.setStyleSheet("color:#FFFFFF;"
                            "font-size:18px;"
                            "margin-left:5px")
        layout.addWidget(wheat_button)
        layout.addWidget(label)
        self.left_menu_layout.addWidget(qwidget, 0, Qt.AlignLeft)
        qwidget.mouseReleaseEvent = self.controller.show_shop_view

    def init_plan_button(self):
        qwidget = QWidget()
        layout = QHBoxLayout()
        qwidget.setLayout(layout)

        qwidget.setStyleSheet("margin-left:15px")

        plan_icon = QIcon(os.getcwd() + "/icons/plan.png")
        plan_button = QPushButton(plan_icon, "")
        plan_button.setIconSize(QSize(30, 30))
        plan_button.setFlat(True)

        label = QLabel("План Севооборота")
        label.setStyleSheet("color: #FFFFFF;"
                            "font-size:18px;"
                            "margin-left:14px")
        layout.addWidget(plan_button)
        layout.addWidget(label)
        self.left_menu_layout.addWidget(qwidget, 0, Qt.AlignLeft)
        qwidget.mouseReleaseEvent = self.controller.show_plan_crop_rotation_view

    def init_graph_button(self):
        qwidget = QWidget()
        layout = QHBoxLayout()
        qwidget.setLayout(layout)
        qwidget.setStyleSheet("margin-left:15px")

        graph_icon = QIcon(os.getcwd() + "/icons/graph.png")
        graph_button = QPushButton(graph_icon, "")
        graph_button.setIconSize(QSize(30, 30))
        graph_button.setFlat(True)

        label = QLabel("График урожайности")
        label.setStyleSheet("color:#FFFFFF;"
                            "font-size:18px;"
                            "margin-left:15px")
        layout.addWidget(graph_button)
        layout.addWidget(label)
        self.left_menu_layout.addWidget(qwidget, 0, Qt.AlignLeft)
        qwidget.mouseReleaseEvent = self.controller.show_graph_yield_view

    def init_deal_button(self):
        qwidget = QWidget()
        layout = QHBoxLayout()
        qwidget.setLayout(layout)
        qwidget.setStyleSheet("margin-left:15px")

        deal_icon = QIcon(os.getcwd() + "/icons/document.png")
        deal_button = QPushButton(deal_icon, "")
        deal_button.setIconSize(QSize(40, 40))
        deal_button.setFlat(True)

        label = QLabel("Договор на поставку")
        label.setStyleSheet("color:#FFFFFF;"
                            "font-size: 18px;"
                            "margin-left:5px")

        layout.addWidget(deal_button)
        layout.addWidget(label)
        self.left_menu_layout.addWidget(qwidget, 0, Qt.AlignLeft)
        qwidget.mouseReleaseEvent = self.controller.show_treaty_view

    def init_technique_button(self):
        qwidget = QWidget()
        layout = QHBoxLayout()
        qwidget.setLayout(layout)
        qwidget.setStyleSheet("margin-left:15px")

        technique_icon = QIcon(os.getcwd() + "/icons/combine.png")
        technique_button = QPushButton(technique_icon, "")
        technique_button.setIconSize(QSize(30, 30))
        technique_button.setFlat(True)

        label = QLabel("Техника на ремонте")
        label.setStyleSheet("color:#FFFFFF;"
                            "font-size:18px;"
                            "margin-left:15px")

        layout.addWidget(technique_button)
        layout.addWidget(label)
        qwidget.mouseReleaseEvent = self.controller.show_technique_view
        self.left_menu_layout.addWidget(qwidget, 0, Qt.AlignLeft)

    def init_rig_button(self):
        qwidget = QWidget()
        layout = QHBoxLayout()
        qwidget.setLayout(layout)
        qwidget.setStyleSheet("margin-left:15px")

        rig_icon = QIcon(os.getcwd() + "/icons/time.png")
        rig_button = QPushButton(rig_icon, "")
        rig_button.setIconSize(QSize(30, 30))
        rig_button.setFlat(True)

        label = QLabel("Наряды")
        label.setStyleSheet("color: #FFFFFF;"
                            "font-size:18px;"
                            "margin-left:15px")

        layout.addWidget(rig_button)
        layout.addWidget(label)
        self.left_menu_layout.addWidget(qwidget, 0, Qt.AlignLeft)
        qwidget.mouseReleaseEvent = self.controller.show_rig_view

    def show_another_view(self, number):
        self.stacked_widgets.widget(1).hide()
        self.stacked_widgets.widget(number).show()
        self.stacked_widgets.setWindowTitle(self.get_title(number))

    def get_title(self, number):
        return {
            0: "Магазин",
            1: "Меню",
            2: "Техника",
            3: "График урожайности",
            4: "Севооборот",
            5: "Договора",
            6: "Наряды"

        }.get(number, 1)
