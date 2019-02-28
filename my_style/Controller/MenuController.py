from PyQt5.QtCore import pyqtSlot


class MenuController(object):

    def __init__(self, view):
        self.view = view

    def show_shop_view(self, event):
        self.view.show_another_view(0)

    def show_technique_view(self, event):
        self.view.show_another_view(2)

    def show_graph_yield_view(self, event):
        self.view.show_another_view(3)

    def show_plan_crop_rotation_view(self, event):
        self.view.show_another_view(4)

    def show_treaty_view(self, event):
        self.view.show_another_view(5)

    def show_rig_view(self, event):
        self.view.show_another_view(6)
