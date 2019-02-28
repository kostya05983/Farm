from admin.View.ErrorDialogView import ErrorDialogView


class LoginController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def check(self):
        if self.model.check(self.view.login.text(), self.view.password.text()) == 1:
            self.view.close_window()
            self.view.show_stacked_widgets()
        else:
            error_dialog = ErrorDialogView("Логин или пароль неверны")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
