from admin.Model.Regex import validate_date, validate_email, validate_requisites, validate_phone_number
from admin.View.ErrorDialogView import ErrorDialogView


class AddTreatyController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_to_db(self):
        if not self.view.delivery_date.text() \
                or not self.view.payment_condition.text() \
                or not self.view.culture_amount.text() \
                or not self.view.organization_name.text() \
                or not self.view.requisites.text() \
                or not self.view.email.text() \
                or not self.view.head.text() \
                or not self.view.post_address.text() \
                or not self.view.legal_address.text() \
                or not self.view.site.text():
            error_dialog = ErrorDialogView("Имя не может быть пустым")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return
        if not validate_phone_number(self.view.phone_number.text()):
            error_dialog = ErrorDialogView("Неверный формат телефонного номера")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return
        if not validate_email(self.view.email.text()):
            error_dialog = ErrorDialogView("Проверьте email")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return
        if not validate_requisites(self.view.requisites.text()):
            error_dialog = ErrorDialogView("Реквизиты должны быть числом")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return

        self.model.insert_to_treaty(self.view.delivery_date.text(),
                                    self.view.delivery_condition.text(),
                                    self.view.payment_condition.text(),
                                    self.view.culture_name.currentData(),
                                    self.view.culture_amount.text(),
                                    self.view.organization_name.text(),
                                    self.view.requisites.text(),
                                    self.view.email.text(),
                                    self.view.head.text(),
                                    self.view.post_address.text(),
                                    self.view.legal_address.text(),
                                    self.view.site.text(),
                                    self.view.phone_number.text())
        self.view.close_window()
