from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QFrame
from admin.Settings import Settings


class ScrollView(QScrollArea):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWidget(widget)
        self.v_layout = QVBoxLayout()
        self.setFrameShape(QFrame.NoFrame)
        self.init_gui()

    def init_gui(self):
        self.setMinimumWidth(Settings.WIDTH.value)
        self.setMinimumHeight(Settings.HEIGHT.value)
        self.setWidgetResizable(True)
        self.setContentsMargins(0, 0, 0, 0)
