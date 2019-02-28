from admin.Model.Regex import validate_time
from admin.View.ErrorDialogView import ErrorDialogView


class AddRigController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_to_db(self):
        if self.view.technique_combo_box.currentData() is None or \
                self.view.location_combo_box.currentData() is None or self.view.user_combo_box.currentData() is None \
                or not self.view.time_line.text() or not self.view.date.text():
            error_dialog = ErrorDialogView("Поля не могут быть пустыми")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return

        if validate_time(self.view.time_line.text()) == 1:
            self.model.insert_to_rig(self.view.technique_combo_box.currentData(),
                                     self.view.location_combo_box.currentData(),
                                     self.view.user_combo_box.currentData(),
                                     self.view.time_line.text(),
                                     self.view.date.text())
            self.view.close_window()
        else:
            error_dialog = ErrorDialogView("Проверьте время")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
