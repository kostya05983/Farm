from admin.View.AddRigView import AddRigView


class RigController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def show_rigs(self):
        self.model.update_rigs()
        if len(self.model.get_rigs()) != 0:
            self.view.show_rigs()
        else:
            self.view.show_nothing()

    def show_add_rig_view(self):
        add_rig_view = AddRigView(self.view.update_view)
        add_rig_view.setModal(True)
        add_rig_view.setWindowTitle("Ввод наряда")
        add_rig_view.exec_()
