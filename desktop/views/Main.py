# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 461)
        

        #########    Center Windows      #####
        qr = Ui_MainWindow.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        Ui_MainWindow.move(qr.topLeft())
        #######################################
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 24))
        self.menubar.setObjectName("menubar")
        self.menuTasks = QtWidgets.QMenu(self.menubar)
        self.menuTasks.setObjectName("menuTasks")
        self.menuUsers = QtWidgets.QMenu(self.menubar)
        self.menuUsers.setObjectName("menuUsers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)
        self.actionNew_Task = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/newTask.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew_Task.setIcon(icon)
        self.actionNew_Task.setObjectName("actionNew_Task")
        self.actionUpdate_Task = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/editTask.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUpdate_Task.setIcon(icon1)
        self.actionUpdate_Task.setObjectName("actionUpdate_Task")
        self.actionDelete = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/deleteTask.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDelete.setIcon(icon2)
        self.actionDelete.setObjectName("actionDelete")
        self.actionCreate = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/createUser.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate.setIcon(icon3)
        self.actionCreate.setObjectName("actionCreate")
        self.actionReset_Password = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../img/resetPass.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionReset_Password.setIcon(icon4)
        self.actionReset_Password.setObjectName("actionReset_Password")
        self.actionExit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../img/logout.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.menuTasks.addAction(self.actionNew_Task)
        self.menuTasks.addAction(self.actionUpdate_Task)
        self.menuTasks.addAction(self.actionDelete)
        self.menuUsers.addAction(self.actionCreate)
        self.menuUsers.addAction(self.actionReset_Password)
        self.menuUsers.addSeparator()
        self.menuUsers.addAction(self.actionExit)
        self.menubar.addAction(self.menuTasks.menuAction())
        self.menubar.addAction(self.menuUsers.menuAction())
        self.toolBar.addAction(self.actionNew_Task)
        self.toolBar.addAction(self.actionUpdate_Task)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar_2.addAction(self.actionCreate)
        self.toolBar_2.addAction(self.actionReset_Password)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo"))
        self.menuTasks.setTitle(_translate("MainWindow", "Tasks"))
        self.menuUsers.setTitle(_translate("MainWindow", "Users"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Task"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "Users"))
        self.actionNew_Task.setText(_translate("MainWindow", "New"))
        self.actionUpdate_Task.setText(_translate("MainWindow", "Update"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionReset_Password.setText(_translate("MainWindow", "Reset Password"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
