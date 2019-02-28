from admin.View.ErrorDialogView import ErrorDialogView


class AddUserController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_to_db(self):
        if not self.view.login.text() and self.view.password.text():
            error_dialog = ErrorDialogView("Имя не может быть пустым")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return

        self.model.insert_to_users(self.view.login.text(), self.view.password.text(), self.view.role.currentData())
        self.view.close_window()
