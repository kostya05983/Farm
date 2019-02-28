import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QProgressDialog, QLayout
from qtpy import QtCore

from admin.Controller.MenuController import MenuViewController
from admin.Model.MenuModel import EmptyViewModel
from admin.Settings import Settings
from admin.View.Roles import Roles


class MenuView(QMainWindow):
    refresh = None
    add = None
    remove = None
    export = None

    def __init__(self, roles):
        self.roles = roles
        super().__init__()
        self.model = EmptyViewModel()
        self.controller = MenuViewController(self, self.model)
        self.init_menu_bar()
        self.init_tool_bar()
        self.init_gui()
        self.keyReleaseEvent = self.controller.key_input

    def init_menu_bar(self):
        menuBar = self.menuBar()
        for role in self.roles:
            if role == Roles.CropRotation.value:
                crop_menu = menuBar.addMenu("Севооборот")
                data = crop_menu.addAction("Данные")
                data.triggered.connect(self.controller.show_plan_crop_rotation_view)

                graphs = crop_menu.addAction("Графики")
                graphs.triggered.connect(self.controller.show_graph_yieldView)
            elif role == Roles.Deals.value:
                deal_menu = menuBar.addAction("Договора")
                deal_menu.triggered.connect(self.controller.show_treaty_view)
            elif role == Roles.Techniques.value:
                techniques = menuBar.addAction("Техника")
                techniques.triggered.connect(self.controller.show_technique_view)
            elif role == Roles.Rig.value:
                rig_menu = menuBar.addAction("Наряды")
                rig_menu.triggered.connect(self.controller.show_rig_view)
            elif role == Roles.Dictionaries.value:
                dictionaries = menuBar.addMenu("Справочники")

                culture = dictionaries.addAction("Культуры")
                culture.triggered.connect(self.controller.show_culture)

                locations = dictionaries.addAction("Участки")
                locations.triggered.connect(self.controller.show_locations)

        users = menuBar.addAction("Пользователи")
        users.triggered.connect(self.controller.show_users)

        about_menu = menuBar.addMenu("Справка")
        about_program = about_menu.addAction("О программе")
        about_program.triggered.connect(self.controller.show_about_program)

        user_guide = about_menu.addAction("Руководство пользователя")
        user_guide.triggered.connect(self.controller.show_user_guide)
        menuBar.setStyleSheet("background-color: #3c4041;"
                              "color:#f0f4f7")

    def init_tool_bar(self):
        tb = self.addToolBar("Table")
        self.refresh = QAction(QIcon(os.getcwd() + "/icons/refresh.png"), "refresh", self)
        tb.addAction(self.refresh)
        self.add = QAction(QIcon(os.getcwd() + "/icons/add.png"), "add", self)
        tb.addAction(self.add)
        self.remove = QAction(QIcon(os.getcwd() + "/icons/remove.png"), "remove", self)
        tb.addAction(self.remove)
        tb.setStyleSheet("background-color: #3c4041;"
                         "color: #ffffff")
        self.export = QAction(QIcon(os.getcwd() + "/icons/export.png"), "Экспорт", self)
        tb.addAction(self.export)

    def init_gui(self):
        self.setGeometry(0, 0, Settings.WIDTH.value, Settings.HEIGHT.value)
        self.setStyleSheet("background-color:#505052")

    def close_window(self):
        self.close()
