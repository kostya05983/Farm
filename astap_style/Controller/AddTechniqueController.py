from admin.Model.Regex import validate_date
from admin.View.ErrorDialogView import ErrorDialogView


class AddTechniqueController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_to_db(self):
        if not self.view.name.text():
            error_dialog = ErrorDialogView("Поля не могут быть пустыми")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return

        self.model.insert_to_technique(self.view.name.text(),
                                       self.view.production_date.text(),
                                       self.view.capital_date.text(),
                                       self.view.next_repair.text(),
                                       self.view.state.currentData())
        self.view.close_window()

