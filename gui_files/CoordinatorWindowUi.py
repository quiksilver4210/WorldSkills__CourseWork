# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CoordinatorWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CoordinatorWindow(object):
    def setupUi(self, CoordinatorWindow):
        CoordinatorWindow.setObjectName("CoordinatorWindow")
        CoordinatorWindow.resize(795, 630)
        self.centralwidget = QtWidgets.QWidget(CoordinatorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 501))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.GreetLabel = QtWidgets.QLabel(self.MainFrame)
        self.GreetLabel.setGeometry(QtCore.QRect(280, 50, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GreetLabel.setFont(font)
        self.GreetLabel.setObjectName("GreetLabel")
        self.MenuLabel = QtWidgets.QLabel(self.MainFrame)
        self.MenuLabel.setGeometry(QtCore.QRect(270, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.ManagingVolunteersButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingVolunteersButton.setGeometry(QtCore.QRect(250, 230, 231, 121))
        self.ManagingVolunteersButton.setObjectName("ManagingVolunteersButton")
        self.ManagingSponsorsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingSponsorsButton.setGeometry(QtCore.QRect(250, 90, 231, 121))
        self.ManagingSponsorsButton.setObjectName("ManagingSponsorsButton")
        self.VolunteersFrame = QtWidgets.QFrame(self.centralwidget)
        self.VolunteersFrame.setGeometry(QtCore.QRect(19, 9, 761, 501))
        self.VolunteersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VolunteersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VolunteersFrame.setObjectName("VolunteersFrame")
        self.ManagingVolunteersLabel = QtWidgets.QLabel(self.VolunteersFrame)
        self.ManagingVolunteersLabel.setGeometry(QtCore.QRect(210, 70, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ManagingVolunteersLabel.setFont(font)
        self.ManagingVolunteersLabel.setObjectName("ManagingVolunteersLabel")
        self.CompetenceLabel = QtWidgets.QLabel(self.VolunteersFrame)
        self.CompetenceLabel.setGeometry(QtCore.QRect(70, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CompetenceLabel.setFont(font)
        self.CompetenceLabel.setObjectName("CompetenceLabel")
        self.CompetenceComboBox = QtWidgets.QComboBox(self.VolunteersFrame)
        self.CompetenceComboBox.setGeometry(QtCore.QRect(190, 130, 73, 22))
        self.CompetenceComboBox.setObjectName("CompetenceComboBox")
        self.SearchButton = QtWidgets.QPushButton(self.VolunteersFrame)
        self.SearchButton.setGeometry(QtCore.QRect(70, 160, 93, 28))
        self.SearchButton.setObjectName("SearchButton")
        self.InsertButton = QtWidgets.QPushButton(self.VolunteersFrame)
        self.InsertButton.setGeometry(QtCore.QRect(470, 120, 161, 41))
        self.InsertButton.setObjectName("InsertButton")
        self.DistributeButton = QtWidgets.QPushButton(self.VolunteersFrame)
        self.DistributeButton.setGeometry(QtCore.QRect(470, 170, 161, 41))
        self.DistributeButton.setObjectName("DistributeButton")
        self.NumVolunteersLabel = QtWidgets.QLabel(self.VolunteersFrame)
        self.NumVolunteersLabel.setGeometry(QtCore.QRect(260, 230, 111, 16))
        self.NumVolunteersLabel.setObjectName("NumVolunteersLabel")
        self.InfoNumVolunteersLabel = QtWidgets.QLabel(self.VolunteersFrame)
        self.InfoNumVolunteersLabel.setGeometry(QtCore.QRect(380, 230, 55, 16))
        self.InfoNumVolunteersLabel.setObjectName("InfoNumVolunteersLabel")
        self.VolunteersTable = QtWidgets.QTableWidget(self.VolunteersFrame)
        self.VolunteersTable.setGeometry(QtCore.QRect(85, 260, 551, 231))
        self.VolunteersTable.setObjectName("VolunteersTable")
        self.VolunteersTable.setColumnCount(0)
        self.VolunteersTable.setRowCount(0)
        self.BackButton = QtWidgets.QPushButton(self.VolunteersFrame)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 91, 31))
        self.BackButton.setObjectName("BackButton")
        self.ThisChempionshipsLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.ThisChempionshipsLabel_2.setGeometry(QtCore.QRect(20, 520, 141, 16))
        self.ThisChempionshipsLabel_2.setObjectName("ThisChempionshipsLabel_2")
        self.NameChempionshipsLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.NameChempionshipsLabel_2.setGeometry(QtCore.QRect(150, 520, 81, 16))
        self.NameChempionshipsLabel_2.setObjectName("NameChempionshipsLabel_2")
        self.VolunteersFrame.raise_()
        self.ThisChempionshipsLabel_2.raise_()
        self.NameChempionshipsLabel_2.raise_()
        self.MainFrame.raise_()
        CoordinatorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CoordinatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        CoordinatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CoordinatorWindow)
        self.statusbar.setObjectName("statusbar")
        CoordinatorWindow.setStatusBar(self.statusbar)
        self.LogoutAction = QtWidgets.QAction(CoordinatorWindow)
        self.LogoutAction.setObjectName("LogoutAction")
        self.menu.addAction(self.LogoutAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(CoordinatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CoordinatorWindow)

    def retranslateUi(self, CoordinatorWindow):
        _translate = QtCore.QCoreApplication.translate
        CoordinatorWindow.setWindowTitle(_translate("CoordinatorWindow", "MainWindow"))
        self.GreetLabel.setText(_translate("CoordinatorWindow", "Доброе утро, Имя"))
        self.MenuLabel.setText(_translate("CoordinatorWindow", "Меню координатора"))
        self.ManagingVolunteersButton.setText(_translate("CoordinatorWindow", "Управление волонтерами"))
        self.ManagingSponsorsButton.setText(_translate("CoordinatorWindow", "Управление спонсорами"))
        self.ManagingVolunteersLabel.setText(_translate("CoordinatorWindow", "Управление волонтерами"))
        self.CompetenceLabel.setText(_translate("CoordinatorWindow", "Компетенция"))
        self.SearchButton.setText(_translate("CoordinatorWindow", "Показать"))
        self.InsertButton.setText(_translate("CoordinatorWindow", "Добавить волонтеров"))
        self.DistributeButton.setText(_translate("CoordinatorWindow", "Распределить волонтеров"))
        self.NumVolunteersLabel.setText(_translate("CoordinatorWindow", "Всего волонтеров:"))
        self.InfoNumVolunteersLabel.setText(_translate("CoordinatorWindow", "1"))
        self.BackButton.setText(_translate("CoordinatorWindow", "Назад"))
        self.ThisChempionshipsLabel_2.setText(_translate("CoordinatorWindow", "Текущий чемпионат:"))
        self.NameChempionshipsLabel_2.setText(_translate("CoordinatorWindow", "название"))
        self.menu.setTitle(_translate("CoordinatorWindow", "Профиль"))
        self.LogoutAction.setText(_translate("CoordinatorWindow", "Выйти"))

