import os
import uuid
from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel

from admin.Controller.ShopController import ShopController
from admin.Model.ShopModel import ShopModel


class ShopView(QWidget):
    HEIGHT = 1080
    WIDTH = 1600
    stacked_widgets = None
    session_id = None

    def __init__(self):
        super().__init__()
        self.model = ShopModel()
        self.session_id = uuid.uuid1()
        self.controller = ShopController(self, self.model, self.session_id)
        self.grid_layout = None
        self.v_layout = QVBoxLayout()
        self.init_header()
        self.init_gui()
        self.init_main_layout()
        self.init_grid(0)

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setStyleSheet("background-color:#F2F2F2")
        self.setLayout(self.v_layout)

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)

    def init_header(self):
        qwidget = QWidget()
        qwidget.setFixedSize(QSize(self.WIDTH, 60))
        qwidget.setStyleSheet("background-color:#424A52;")
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setAlignment(Qt.AlignLeft)
        qwidget.setLayout(horizontal_layout)

        self.init_wheat(horizontal_layout)
        self.init_cucumber(horizontal_layout)
        self.init_cart(horizontal_layout)
        self.v_layout.addWidget(qwidget)

    def init_wheat(self, horizontal_layout):
        wheat_icon = QIcon(os.getcwd() + "/icons/wheat.png")
        wheat_button = QPushButton(wheat_icon, "Зерновые")
        wheat_button.setIconSize(QSize(40, 40))
        wheat_button.setFlat(True)
        wheat_button.setStyleSheet("margin-left:100px;"
                                   "color:#FFFFFF;"
                                   "font-size:22px")
        wheat_button.clicked.connect(partial(self.controller.change_layout, 0))
        horizontal_layout.addWidget(wheat_button)

    def init_cucumber(self, horizontal_layout):
        cucumber_icon = QIcon(os.getcwd() + "/icons/cucumber.png")
        cucumber_button = QPushButton(cucumber_icon, "Овощи", self)
        cucumber_button.setIconSize(QSize(30, 30))
        cucumber_button.setFlat(True)
        cucumber_button.setStyleSheet("color:#FFFFFF;"
                                      "font-size:22px")
        cucumber_button.clicked.connect(partial(self.controller.change_layout, 1))
        horizontal_layout.addWidget(cucumber_button)

    def init_cart(self, horizontal_layout):
        cart_icon = QIcon(os.getcwd() + "/icons/cart.png")
        cart_button = QPushButton(cart_icon, "")
        cart_button.setIconSize(QSize(40, 40))
        cart_button.setFlat(True)
        cart_button.setStyleSheet("margin-left:1000px")
        cart_button.clicked.connect(partial(self.controller.change_layout, 3))
        horizontal_layout.addWidget(cart_button)

    def init_grid(self, type):
        qwidget = QWidget()
        qwidget.setStyleSheet("margin-left:20px")
        products_list = self.model.get_products(type, self.session_id)

        grid_layout = QGridLayout()
        qwidget.setLayout(grid_layout)

        for i in range(len(products_list)):
            grid_layout.addWidget(products_list[i], i // 4, i % 4)
        self.grid_layout = grid_layout
        self.v_layout.addWidget(qwidget, 0)

    def update_view_grid(self, type):
        self.clear_layout()
        self.init_header()
        self.init_grid(type)

    def update_view_shop(self):
        self.clear_layout()
        self.init_header()
        self.init_amount_goods_label()
        self.init_goods()
        self.init_sum()

    def update_view_shop_nothing(self):
        self.clear_layout()
        self.init_header()
        self.show_nothing()

    def show_nothing(self):
        label = QLabel("В вашей корзине ничего нет")
        label.setStyleSheet("font-size:24px")
        self.v_layout.addWidget(label, 0, Qt.AlignCenter | Qt.AlignTop)

    def init_amount_goods_label(self):
        label = QLabel("Количество товаров %s" % str(len(self.model.get_goods(self.session_id))))
        label.setStyleSheet("font-size: 24px")
        self.v_layout.addWidget(label, 0, Qt.AlignCenter | Qt.AlignTop)

    def init_sum(self):
        widget = QWidget()
        h_layout = QHBoxLayout()
        h_layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Сумма %s рублей" % self.model.get_sum(self.session_id))
        label.setStyleSheet("font-size:24px")
        h_layout.addWidget(label, 0, Qt.AlignCenter)
        h_layout.setContentsMargins(0, 0, 0, 0)
        self.init_ok_button(h_layout)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget, 24, Qt.AlignTop | Qt.AlignCenter)

    def init_ok_button(self, horizontal_layout):
        cart_icon = QIcon(os.getcwd() + "/icons/ok_black.png")
        ok_button = QPushButton(cart_icon, "")
        ok_button.setIconSize(QSize(30, 30))
        ok_button.setFlat(True)
        ok_button.setStyleSheet("margin-left:300px;"
                                "border:0px;"
                                "margin-left:0px;")
        ok_button.clicked.connect(partial(self.controller.show_deal_treaty, self.session_id))
        horizontal_layout.addWidget(ok_button, 0, Qt.AlignLeft)

    def init_goods(self):
        goods = self.model.get_goods(self.session_id)
        widget = QWidget()
        widget.setStyleSheet("border: 1px outset black")
        v_layout = QVBoxLayout()
        for (id, name, amount, price) in goods:
            row_widget = QWidget()
            row_widget.setStyleSheet("background-color: #424a52;"
                                     "color:#FFFFFF;"
                                     "text-align:center;")
            h_layout = QHBoxLayout()
            name = QLabel(name)
            name.setStyleSheet("border:0 px;")
            amount = QLabel("Количество %d кг" % amount)
            amount.setStyleSheet("border: 0 px;")
            price = QLabel("Цена %d руб" % price)
            price.setStyleSheet("border:0 px;")
            h_layout.addWidget(name)
            h_layout.addWidget(amount)
            h_layout.addWidget(price)
            self.init_delete_button(h_layout, id)
            row_widget.setLayout(h_layout)
            v_layout.setSpacing(0)
            v_layout.setContentsMargins(0, 0, 0, 0)
            v_layout.addWidget(row_widget, 0, Qt.AlignTop)
        widget.setLayout(v_layout)
        self.v_layout.addWidget(widget, 2, Qt.AlignTop)

    def init_delete_button(self, horizontal_layout, id):
        cart_icon = QIcon(os.getcwd() + "/icons/delete.png")
        delete_button = QPushButton(cart_icon, "")
        delete_button.setIconSize(QSize(30, 30))
        delete_button.setFlat(True)
        delete_button.setStyleSheet("margin-left:300px;"
                                    "border:0px;")
        delete_button.clicked.connect(partial(self.controller.delete_from_cart, id))
        horizontal_layout.addWidget(delete_button)

    def clear_layout(self):
        for i in reversed(range(self.v_layout.count())):
            self.v_layout.itemAt(i).widget().setParent(None)
