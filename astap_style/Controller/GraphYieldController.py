class GraphYieldController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def export(self):
        self.model.export(self.view.chart_views)

    def key_input(self, event):
        if event.key() == Qt.Key_E:
            self.model.export()
