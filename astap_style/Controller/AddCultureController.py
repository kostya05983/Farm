from admin.Model.Regex import validate_number
from admin.View.ErrorDialogView import ErrorDialogView


class AddCultureController(object):

    def __init__(self, model, view):
        self.view = view
        self.model = model

    def add_to_db(self):
        if not self.view.amount.text() and not self.view.culture.text() and not self.view.price.text():
            error_dialog = ErrorDialogView("Поля не могут быть пустыми")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return
        if validate_number(self.view.amount.text()) and validate_number(self.view.price.text()):
            self.model.insert_culture(self.view.culture.text(), self.view.amount.text(),self.view.price.text())
            self.view.close_window()
        else:
            error_dialog = ErrorDialogView("Проверьте количество и ценну")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
