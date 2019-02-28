from PyQt5.QtCore import Qt


class AboutProgramController(object):

    def __init__(self, view):
        super(AboutProgramController, self).__init__()
        self.view = view

    def key_input(self, event):
        if event.key() == Qt.Key_Escape:
            self.view.close_window()
            return
