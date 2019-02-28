import os
from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QPushButton, QScrollArea
from PyQt5.QtCore import *

from admin.Controller.ScrollController import ScrollController


class ScrollView(QScrollArea):
    WIDTH = 1600
    HEIGHT = 1080
    stacked_widgets = None

    def __init__(self, widget, id):
        super().__init__()
        self.widget = widget
        self.id = id
        self.setWidget(widget)
        self.v_layout = QVBoxLayout()
        self.controller = ScrollController(self)
        self.setFrameShape(QFrame.NoFrame)
        self.init_gui()
        self.init_menu_button()

    def init_gui(self):
        self.setMinimumWidth(1600)
        self.setMinimumHeight(800)
        self.setContentsMargins(0, 0, 0, 0)

    def init_menu_button(self):
        icon = QIcon(os.getcwd() + "/icons/menu.png")
        menu_button = QPushButton(icon, "")
        menu_button.setParent(self)
        menu_button.setIconSize(QSize(40, 40))
        menu_button.setFlat(True)
        menu_button.setStyleSheet("margin-left:20px;"
                                  "margin-top:720px;"
                                  "margin-bottom:20px")
        menu_button.clicked.connect(partial(self.controller.show_menu))
        self.v_layout.addWidget(menu_button, 0, Qt.AlignBottom)

    def show_menu(self):
        self.stacked_widgets.widget(self.id).hide()
        self.stacked_widgets.widget(1).show()
        self.stacked_widgets.setWindowTitle("Меню")
