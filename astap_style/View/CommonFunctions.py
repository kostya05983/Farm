from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


def add_date(str, dateEdit, layout):
    widget = QWidget()
    h_layout = QHBoxLayout()
    label = QLabel(str)
    h_layout.addWidget(label)
    dateEdit.setWindowFlag(Qt.Popup)
    dateEdit.setCalendarPopup(True)
    format = QTextCharFormat()
    format.setBackground(QBrush(QColor("#888888")))
    dateEdit.calendarWidget().setWeekdayTextFormat(Qt.DayOfWeek.Monday, format)
    dateEdit.calendarWidget().setWeekdayTextFormat(Qt.DayOfWeek.Tuesday, format)
    dateEdit.calendarWidget().setWeekdayTextFormat(Qt.DayOfWeek.Wednesday, format)
    dateEdit.calendarWidget().setWeekdayTextFormat(Qt.DayOfWeek.Thursday, format)
    dateEdit.calendarWidget().setWeekdayTextFormat(Qt.DayOfWeek.Friday, format)
    dateEdit.calendarWidget().setWeekdayTextFormat(Qt.DayOfWeek.Saturday, format)
    dateEdit.calendarWidget().setWeekdayTextFormat(Qt.DayOfWeek.Sunday, format)
    dateEdit.setStyleSheet("background-color:#888888;")
    h_layout.addWidget(dateEdit)
    widget.setLayout(h_layout)
    layout.addWidget(widget)