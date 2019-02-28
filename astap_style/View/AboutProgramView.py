from PyQt5.QtWidgets import QVBoxLayout, QLabel

from admin.Controller.AboutProgramController import AboutProgramController
from admin.View.QDialogView import QDialogView


class AboutProgramView(QDialogView):
    background_color = "#505052"
    Text = """
    Версия 1.0
    Создано Shadow Crop
    """
    HEIGHT = 80
    WIDTH = 400

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.controller = AboutProgramController(self)
        self.init_gui()
        self.init_main_layout()
        self.init_body(self.Text)

    def init_body(self, text):
        label = QLabel()
        label.setStyleSheet("color: #FFFFFF;"
                            "font-size:16px")
        label.setText(text)
        self.v_layout.addWidget(label)
