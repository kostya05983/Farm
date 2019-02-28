from admin.Model.Regex import validate_number
from admin.View.ErrorDialogView import ErrorDialogView


class AddLocationController(object):

    def __init__(self, model, view):
        self.view = view
        self.model = model

    def add_to_db(self):
        if not self.view.width.text() and not self.view.height.text():
            error_dialog = ErrorDialogView("Поля не могут быть пустыми")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return
        if validate_number(self.view.width.text()) and validate_number(self.view.height.text()):
            self.model.insert_culture(self.view.width.text(), self.view.height.text())
            self.view.close_window()
        else:
            error_dialog = ErrorDialogView("Длина и ширина должны быть числом")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
