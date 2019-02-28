from admin.View.ErrorDialogView import ErrorDialogView


class AddCropRotationController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_to_db(self):
        if self.model.validate_number(self.view.start_year.text()) == 1:
            for i in range(5):
                if self.model.validate_number(self.view.amount_seed[i].text()) != 1:
                    return
            for i in range(5):
                self.model.insert_crop_rotation(self.view.location_combo_box[i].currentData(),
                                                self.view.culture_combo_box[i].currentData(),
                                                int(self.view.amount_seed[i].text()),
                                                int(self.view.start_year.text()) + i)
            self.view.close_window()
        else:
            error_dialog = ErrorDialogView("Проверьте год")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
