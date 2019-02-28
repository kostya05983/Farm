class ScrollController(object):

    def __init__(self, view):
        self.view = view

    def show_menu(self, event):
        self.view.show_menu()
