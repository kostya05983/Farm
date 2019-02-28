from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QWidget, QHBoxLayout, QLabel


class QDialogView(QDialog):

    def init_gui(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setLayout(self.v_layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color: #424A52;"
                           "color:#FFFFFF")

    def init_main_layout(self):
        self.v_layout.setAlignment(Qt.AlignTop)
        self.v_layout.setDirection(QVBoxLayout.TopToBottom)
        self.v_layout.setSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)

    def add_input_line(self, str, line):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel(str)
        h_layout.addWidget(label)
        line.setMaximumWidth(200)
        line.setStyleSheet("background-color: #888888")
        h_layout.addWidget(line)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def add_combo_box(self, str, init_data, combo_box):
        widget = QWidget()
        h_layout = QHBoxLayout()
        label = QLabel(str)
        h_layout.addWidget(label)

        data = init_data()
        for (id, text) in data:
            combo_box.addItem(text, id)
        combo_box.setStyleSheet("background-color: #888888")
        h_layout.addWidget(combo_box)
        widget.setLayout(h_layout)
        self.v_layout.addWidget(widget)

    def close_window(self):
        self.update()
        self.close()
