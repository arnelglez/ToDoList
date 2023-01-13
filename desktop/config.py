import os
import sys
from ent.entLogin import eLogin

from PySide6 import  QtWidgets, QtGui

_eLogin = eLogin()


class GeneralsFuntions:

    def resource_path(self, relative_path):
        relative = relative_path[3:]
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative)
    
    def information_message(self, type, title, sMensaje):
    
        msg = QtWidgets.QMessageBox()
        if type == 'information':
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        elif type == 'error':
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setText(sMensaje)
        msg.setWindowTitle(title)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("../img/Accept.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        aceptar = msg.addButton('Accept', QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        aceptar.setIcon(icon)
        # Ejecuta el MessageBox
        msg.exec()
