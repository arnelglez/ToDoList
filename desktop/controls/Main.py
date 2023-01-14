import sys
import config

from config import GeneralsFuntions

from mod.modLogin import mLogin

from controls.Main import *
from views.Main import Ui_MainWindow

from PySide6 import QtWidgets

class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.generals = GeneralsFuntions()        
        
        self.setupUi(self)

                 

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = Main()
    windows.show()
    sys.exit(app.exec())