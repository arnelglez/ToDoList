import sys
import config

from config import GeneralsFuntions

from mod.modLogin import mLogin

from controls.Main import *
from views.Login import Ui_Login

from PySide6 import QtWidgets

class Login(QtWidgets.QMainWindow, Ui_Login):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Login.__init__(self)
        
        self.generals = GeneralsFuntions()
        
        self.setupUi(self)

    def login(self):
        user = self.editUsername.text().lower() 
        passwd = self.editPassword.text()

        response, config._eLogin = mLogin().login(user, passwd)

        if response != '':     
            self.generals.information_message("information", 
                                "User Error",
                                response)

            self.editUsername.clear()
            self.editPassword.clear()
        else:
    

            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Main()
            self.ui.setupUi(self.MainWindow) 
            self.MainWindow.show()
                 

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = Ui_Login()
    windows.show()
    sys.exit(app.exec_())