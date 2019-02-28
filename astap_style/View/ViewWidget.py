from abc import ABC

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from admin.Settings import Settings


class ViewWidget(QWidget):
    background_color = "#424A52"
    WIDTH = Settings.WIDTH.value
    HEIGHT = Settings.HEIGHT.value

    def __init__(self):
        super(ViewWidget, self).__init__()
        self.v_layout = QVBoxLayout()

    def init_gui(self):
        self.setGeometry(0, 0, Settings.WIDTH.value, Settings.HEIGHT.value)
        self.setLayout(self.v_layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color: %s;"
                           "color:#FFFFFF" % self.background_color)

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.v_layout.setSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)

    def clear_layout(self):
        for i in reversed(range(self.v_layout.count())):
            self.v_layout.itemAt(i).widget().setParent(None)
