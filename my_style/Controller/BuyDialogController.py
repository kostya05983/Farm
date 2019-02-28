from admin.View.ErrorDialogView import ErrorDialogView


class BuyDialogController(object):
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def key_amount_form_event(self, event):
        if self.model.validate_amount(self.view.amount_line.text()) == 1:
            self.view.update_price(int(self.view.amount_line.text()) * self.view.price)

    def add_to_db(self):
        if self.model.validate_amount(self.view.amount_line.text()) == 1:
            self.model.insert_to_db(self.view.id, self.view.amount_line.text(), self.view.session_id)
            self.view.close_window()
        else:
            error_dialog = ErrorDialogView("Проверьте количество")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
