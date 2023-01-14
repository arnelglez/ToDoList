# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PySide6 import QtCore, QtGui, QtWidgets



class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(430, 270)
        Login.setMinimumSize(QtCore.QSize(430, 270))
        Login.setMaximumSize(QtCore.QSize(430, 270))        

        #########    Center Windows      #####
        qr = Login.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)        
        Login.move(qr.topLeft())     
        #######################################
        
        self.editUsername = QtWidgets.QLineEdit(Login)
        self.editUsername.setGeometry(QtCore.QRect(144, 70, 220, 27))
        self.editUsername.setObjectName("editUsername")
        self.editPassword = QtWidgets.QLineEdit(Login)
        self.editPassword.setGeometry(QtCore.QRect(144, 120, 220, 27))
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.editPassword.setObjectName("editPassword")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(60, 74, 101, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(60, 124, 91, 19))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Login)
        self.groupBox.setGeometry(QtCore.QRect(1, 1, 428, 268))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.buttonAccept = QtWidgets.QPushButton(self.groupBox)
        self.buttonAccept.setGeometry(QtCore.QRect(110, 190, 88, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.generals.resource_path("../img/accept.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.buttonAccept.setIcon(icon)
        self.buttonAccept.setObjectName("buttonAccept")
        self.buttonCancel = QtWidgets.QPushButton(self.groupBox)
        self.buttonCancel.setGeometry(QtCore.QRect(240, 190, 88, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.generals.resource_path("../img/cancel.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.buttonCancel.setIcon(icon1)
        self.buttonCancel.setObjectName("buttonCancel")
        self.groupBox.raise_()
        self.editUsername.raise_()
        self.editPassword.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        
        self.editUsername.setText('aglez')
        self.editPassword.setText('Pepe123++')
        
        self.buttonAccept.clicked.connect(self.login)
        self.buttonCancel.clicked.connect(self.close_windows)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Username: "))
        self.label_2.setText(_translate("Login", "Password:"))
        self.buttonAccept.setText(_translate("Login", "Accept"))
        self.buttonCancel.setText(_translate("Login", "Cancel"))