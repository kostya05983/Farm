import sys

from PyQt5.QtWidgets import QApplication, QStackedWidget

from admin.Model.ShopModel import ShopModel
from admin.View.GraphYieldView import GraphYieldView
from admin.View.LoginView import LoginView
from admin.View.MenuView import MenuView
from admin.View.PlanCropRotationView import PlanCropRotationView
from admin.View.RigView import RigView
from admin.View.ScrollView import ScrollView
from admin.View.ShopView import ShopView
from admin.View.TechniqueView import TechniqueView
from admin.View.TreatyView import TreatyView

app = QApplication(sys.argv)
model = ShopModel()

qStackedWidget = QStackedWidget()

shopView = ShopView()
shop_scroll_view = ScrollView(shopView, 0)
shop_scroll_view.stacked_widgets = qStackedWidget
qStackedWidget.addWidget(shop_scroll_view)

menu_view = MenuView()
menu_view.stacked_widgets = qStackedWidget
qStackedWidget.addWidget(menu_view)

technique_view = TechniqueView()
technique_scroll_view = ScrollView(technique_view, 2)
technique_scroll_view.stacked_widgets = qStackedWidget
qStackedWidget.addWidget(technique_scroll_view)

graph_yield_view = GraphYieldView()
graph_yield_scroll_view = ScrollView(graph_yield_view, 3)
graph_yield_scroll_view.stacked_widgets = qStackedWidget
qStackedWidget.addWidget(graph_yield_scroll_view)

plan_crop_rotation = PlanCropRotationView()
plan_crop_rotation_scroll_view = ScrollView(plan_crop_rotation, 4)
plan_crop_rotation_scroll_view.stacked_widgets = qStackedWidget
qStackedWidget.addWidget(plan_crop_rotation_scroll_view)

treaty = TreatyView()
treaty_scroll_view = ScrollView(treaty, 5)
treaty_scroll_view.stacked_widgets = qStackedWidget
qStackedWidget.addWidget(treaty_scroll_view)

rig = RigView()
rig_scroll_view = ScrollView(rig, 6)
rig_scroll_view.stacked_widgets = qStackedWidget
qStackedWidget.addWidget(rig_scroll_view)

qStackedWidget.setGeometry(0, 0, 1200, 800)
qStackedWidget.setWindowTitle("Магазин")

loginView = LoginView()
loginView.stacked_widgets = qStackedWidget
loginView.setWindowTitle("Вход")
loginView.show()

sys.exit(app.exec_())
