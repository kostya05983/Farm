from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import *

from admin.Settings import Settings
from admin.View.ViewWidget import ViewWidget


class UserGuideView(ViewWidget):
    background_color = "#505052"
    Text_Functions = """
    Программа предоставляет следующие функциии:
    1)Редактирование Севооборота( новый севооборот составляется на 5 лет).
    2)Редактирование списка техники и добавление новой техники.
    3)Редактирование списка нарядов и добавление нового наряда.
    Сочетания горячих клавиш:
    1-9 переключение между окнами.
    esc - выход из программы.
    + - добавление элемента.
    r - обновление таблицы.
    """

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.init_gui()
        self.init_main_layout()
        self.show_guide()

    def show_guide(self):
        self.init_header("Список функций")
        self.init_body(self.Text_Functions)

    def init_header(self, text):
        label = QLabel()
        label.setStyleSheet("color: #FFFFFF;"
                            "font-size:24px")
        label.setText(text)
        self.v_layout.addWidget(label, 0, Qt.AlignCenter)

    def init_body(self, text):
        label = QLabel()
        label.setStyleSheet("color: #FFFFFF;"
                            "font-size:16px")
        label.setText(text)
        self.v_layout.addWidget(label)
