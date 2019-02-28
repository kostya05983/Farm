from admin.View.ErrorDialogView import ErrorDialogView

from admin.View.MenuView import MenuView


class LoginController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def check(self):
        if self.model.check(self.view.login.text(), self.view.password.text()) == 1:
            self.view.close_window()
            roles = self.model.selectRoles(self.view.login.text())
            view = MenuView(roles)
            view.setWindowTitle("Меню")
            view.show()
        else:
            error_dialog = ErrorDialogView("Логин или пароль неверны")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
