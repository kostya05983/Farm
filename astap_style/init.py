import sys

from PyQt5.QtWidgets import QApplication

from admin.View.LoginView import LoginView
from admin.View.MenuView import MenuView

app = QApplication(sys.argv)
loginView = LoginView()
loginView.setWindowTitle("Вход")
loginView.show()
# menuView = MenuView([0, 1, 2, 3, 4])
# menuView.show()
sys.exit(app.exec_())
