from admin.View.BuyDialogView import BuyDialogView


class ProductController(object):
    def __init__(self, view):
        self.view = view

    def show_dialog(self, id, name, price,session_id):
        buy_dialog_view = BuyDialogView(id, name, price,session_id)
        buy_dialog_view.setModal(True)
        buy_dialog_view.setWindowTitle("Добавить в корзину")
        buy_dialog_view.exec_()
