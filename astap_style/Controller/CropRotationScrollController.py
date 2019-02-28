from admin.View.AddCropRotationView import AddCropRotationView


class CropRotationScrollController(object):

    def __init__(self, view):
        self.view = view

    def trigger_button(self):
        add_rig_view = AddCropRotationView(self.view.widget.update_view)
        add_rig_view.setModal(True)
        add_rig_view.setWindowTitle("Добавление договора")
        add_rig_view.exec_()