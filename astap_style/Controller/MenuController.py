from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressBar

from admin.View.AboutProgramView import AboutProgramView
from admin.View.CreateUserView import CreateUserView
from admin.View.CultureView import CultureView
from admin.View.ErrorDialogView import ErrorDialogView
from admin.View.GraphYieldView import GraphYieldView
from admin.View.LocationView import LocationView
from admin.View.PlanCropRotationView import PlanCropRotationView
from admin.View.RigView import RigView
from admin.View.ScrollView import ScrollView
from admin.View.TechniqueView import TechniqueView
from admin.View.TreatyView import TreatyView
from admin.View.UserGuideView import UserGuideView


class MenuViewController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def no_table_selected(self):
        error_dialog = ErrorDialogView("Ни одной таблицы не выбрано")
        error_dialog.setModal(True)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.exec_()

    def show_graph_yieldView(self):
        self.view.setWindowTitle("Севооборот")
        view = GraphYieldView()
        scrolView = ScrollView(view)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.controller.export)
        self.view.setCentralWidget(scrolView)

    def show_rig_view(self):
        view = RigView()
        self.view.setWindowTitle("Наряды")
        self.view.refresh.triggered.disconnect()
        self.view.refresh.triggered.connect(view.update_view)
        self.view.add.triggered.disconnect()
        self.view.add.triggered.connect(view.controller.add_rig_view)
        self.view.remove.triggered.disconnect()
        self.view.remove.triggered.connect(view.controller.remove_row)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.model.export)
        self.view.setCentralWidget(view)

    def show_technique_view(self):
        view = TechniqueView()
        self.view.setWindowTitle("Техника")
        self.view.refresh.triggered.disconnect()
        self.view.refresh.triggered.connect(view.update_view)
        self.view.add.triggered.disconnect()
        self.view.add.triggered.connect(view.controller.add_techhnique)
        self.view.remove.triggered.disconnect()
        self.view.remove.triggered.connect(view.controller.remove_row)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.model.export)
        self.view.setCentralWidget(view)

    def show_treaty_view(self):
        view = TreatyView()
        self.view.setWindowTitle("Договора")
        self.view.refresh.triggered.disconnect()
        self.view.refresh.triggered.connect(view.update_view)
        self.view.add.triggered.disconnect()
        self.view.add.triggered.connect(view.controller.add_treaty)
        self.view.remove.triggered.disconnect()
        self.view.remove.triggered.connect(view.controller.remove_row)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.model.export)
        self.view.setCentralWidget(view)

    def show_plan_crop_rotation_view(self):
        view = PlanCropRotationView()
        self.view.setWindowTitle("Севооборот")
        self.view.refresh.triggered.disconnect()
        self.view.refresh.triggered.connect(view.update_view)
        self.view.add.triggered.disconnect()
        self.view.add.triggered.connect(view.controller.add_crop_rotation_view)
        self.view.remove.triggered.disconnect()
        self.view.remove.triggered.connect(view.controller.remove_row)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.model.export)
        self.view.setCentralWidget(view)

    def show_about_program(self):
        view = AboutProgramView()
        view.setModal(True)
        view.setWindowTitle("О программе")
        view.exec_()
        view.show()

    def show_culture(self):
        view = CultureView()
        self.view.setWindowTitle("Культуры")
        self.view.refresh.triggered.disconnect()
        self.view.refresh.triggered.connect(view.update_view)
        self.view.add.triggered.disconnect()
        self.view.add.triggered.connect(view.controller.add_culture)
        self.view.remove.triggered.disconnect()
        self.view.remove.triggered.connect(view.controller.remove_row)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.model.export)
        self.view.setCentralWidget(view)

    def show_locations(self):
        view = LocationView()
        self.view.setWindowTitle("Участки")
        self.view.refresh.triggered.disconnect()
        self.view.refresh.triggered.connect(view.update_view)
        self.view.add.triggered.disconnect()
        self.view.add.triggered.connect(view.controller.add_location)
        self.view.remove.triggered.disconnect()
        self.view.remove.triggered.connect(view.controller.remove_row)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.model.export)
        self.view.setCentralWidget(view)

    def show_users(self):
        view = CreateUserView()
        self.view.setWindowTitle("Пользователи")
        self.view.refresh.triggered.disconnect()
        self.view.refresh.triggered.connect(view.update_view)
        self.view.add.triggered.disconnect()
        self.view.add.triggered.connect(view.controller.add_user)
        self.view.remove.triggered.disconnect()
        self.view.remove.triggered.connect(view.controller.remove_row)
        self.view.export.triggered.disconnect()
        self.view.export.triggered.connect(view.model.export)
        self.view.setCentralWidget(view)

    def key_input(self, event):
        if event.key() == Qt.Key_1:
            self.show_plan_crop_rotation_view()
            return
        if event.key() == Qt.Key_2:
            self.show_graph_yieldView()
            return
        if event.key() == Qt.Key_3:
            self.show_treaty_view()
            return
        if event.key() == Qt.Key_4:
            self.show_technique_view()
            return
        if event.key() == Qt.Key_5:
            self.show_rig_view()
            return
        if event.key() == Qt.Key_6:
            self.show_about_program()
            return
        if event.key() == Qt.Key_7:
            self.show_user_guide()
            return
        if event.key() == Qt.Key_8:
            self.show_culture()
            return
        if event.key() == Qt.Key_9:
            self.show_locations()
            return
        if event.key() == Qt.Key_Escape:
            self.view.close_window()

    def exit(self):
        self.view.close()
        from admin.View.LoginView import LoginView
        loginView = LoginView()
        loginView.setWindowTitle("Вход")
        loginView.show()

    def show_user_guide(self):
        self.view.setWindowTitle("О программе")
        view = UserGuideView()
        scroll_view = ScrollView(view)
        self.view.setCentralWidget(scroll_view)
