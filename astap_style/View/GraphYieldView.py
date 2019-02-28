from PyQt5.QtChart import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy

from admin.Controller.GraphYieldController import GraphYieldController
from admin.Model.GraphYieldModel import GraphYieldModel
from admin.Settings import Settings


class GraphYieldView(QWidget):
    chart_views = None

    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.model = GraphYieldModel()
        self.controller = GraphYieldController(self, self.model)
        self.init_main_layout()
        self.init_gui()
        self.init_graphs()

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)

    def init_gui(self):
        self.setMinimumWidth(Settings.WIDTH.value)
        self.setMinimumHeight(Settings.HEIGHT.value + 1800)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(self.v_layout)

    def init_graphs(self):
        years = self.model.get_all_years()
        self.setMinimumHeight(len(years) * 800)
        self.chart_views = []
        for year in years:
            pairs = self.model.get_pairs_by_year(year)
            series = QBarSeries()
            for pair in pairs:
                q_bar_set = QBarSet(pair[0])
                q_bar_set.append(pair[1])
                series.append(q_bar_set)
            chart = QChart()
            axis_y = QValueAxis()
            axis_y.setTickCount(10)
            axis_y.setVisible(True)
            chart.addAxis(axis_y, Qt.AlignLeft)
            chart.addSeries(series)
            series.attachAxis(axis_y)
            chart.setTitle("Отчет за %s год" % year)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart_view = QChartView(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)
            self.chart_views.append(chart_view)
            self.v_layout.addWidget(chart_view, 0)
