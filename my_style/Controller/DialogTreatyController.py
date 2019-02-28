from admin.View.ErrorDialogView import ErrorDialogView


class DialogTreatyController(object):
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_to_db(self):
        if self.model.valid_phone_number(self.view.phone_number.text()) == 1:
            if self.view.delivery_condition.text() \
                    or self.view.payment_condition.text() \
                    or self.view.name.text() \
                    or self.view.requisites.text() \
                    or self.view.email.text() \
                    or self.view.head.text() \
                    or self.view.post_address.text() \
                    or self.view.legal_address.text() \
                    or self.view.site.text():
                self.model.insert_treaty(self.view.delivery_condition.text(), self.view.payment_condition.text(),
                                         self.view.name.text(), self.view.requisites.text(), self.view.email.text(),
                                         self.view.head.text(), self.view.post_address.text(),
                                         self.view.legal_address.text(),
                                         self.view.site.text(), self.view.phone_number.text(), self.view.session_id)
                self.view.close_window()
            else:
                error_dialog = ErrorDialogView("Не все поля зхаполнены")
                error_dialog.setModal(True)
                error_dialog.setWindowTitle("Ошибка")
                error_dialog.exec_()
        else:
            error_dialog = ErrorDialogView("Неверный телефонный номер")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
