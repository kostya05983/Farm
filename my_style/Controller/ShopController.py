from PyQt5.QtCore import pyqtSlot

from admin.View.DialogTreatyView import DialogTreatyView


class ShopController(object):

    def __init__(self, view, model, session_id):
        self.view = view
        self.model = model
        self.session_id = session_id

    @pyqtSlot(int)
    def change_layout(self, type_good):
        if type_good == 3:
            if len(self.model.get_goods(self.session_id)) == 0:
                self.view.update_view_shop_nothing()
            else:
                self.view.update_view_shop()

        else:
            self.view.update_view_grid(type_good)

    def delete_from_cart(self, id):
        self.model.delete_from_cart(id)
        self.change_layout(3)

    def show_deal_treaty(self, session_id):
        dialogTreaty = DialogTreatyView(session_id)
        dialogTreaty.setModal(True)
        dialogTreaty.setWindowTitle("Ввод договора на поставку")
        dialogTreaty.exec_()
