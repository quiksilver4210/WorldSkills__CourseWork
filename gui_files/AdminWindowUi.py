# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(783, 570)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 10, 761, 481))
        self.MainFrame.setAutoFillBackground(True)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.MenuLabel = QtWidgets.QLabel(self.MainFrame)
        self.MenuLabel.setGeometry(QtCore.QRect(240, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.GreetLabel = QtWidgets.QLabel(self.MainFrame)
        self.GreetLabel.setGeometry(QtCore.QRect(280, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GreetLabel.setFont(font)
        self.GreetLabel.setObjectName("GreetLabel")
        self.ManagingChampionshipsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingChampionshipsButton.setGeometry(QtCore.QRect(250, 100, 221, 101))
        self.ManagingChampionshipsButton.setObjectName("ManagingChampionshipsButton")
        self.ManagingCompetitorsButton = QtWidgets.QPushButton(self.MainFrame)
        self.ManagingCompetitorsButton.setGeometry(QtCore.QRect(250, 230, 221, 101))
        self.ManagingCompetitorsButton.setObjectName("ManagingCompetitorsButton")
        self.ManageChempionshipsFrame = QtWidgets.QFrame(self.centralwidget)
        self.ManageChempionshipsFrame.setGeometry(QtCore.QRect(19, 9, 761, 481))
        self.ManageChempionshipsFrame.setAutoFillBackground(True)
        self.ManageChempionshipsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ManageChempionshipsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ManageChempionshipsFrame.setObjectName("ManageChempionshipsFrame")
        self.ExpertButton = QtWidgets.QPushButton(self.ManageChempionshipsFrame)
        self.ExpertButton.setGeometry(QtCore.QRect(190, 100, 181, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.ExpertButton.setPalette(palette)
        self.ExpertButton.setObjectName("ExpertButton")
        self.CoordinatorButton = QtWidgets.QPushButton(self.ManageChempionshipsFrame)
        self.CoordinatorButton.setGeometry(QtCore.QRect(400, 100, 181, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.CoordinatorButton.setPalette(palette)
        self.CoordinatorButton.setObjectName("CoordinatorButton")
        self.ChempionshipsTable = QtWidgets.QTableWidget(self.ManageChempionshipsFrame)
        self.ChempionshipsTable.setGeometry(QtCore.QRect(70, 210, 631, 261))
        self.ChempionshipsTable.setObjectName("ChempionshipsTable")
        self.ChempionshipsTable.setColumnCount(0)
        self.ChempionshipsTable.setRowCount(0)
        self.ChempionshipsLabel = QtWidgets.QLabel(self.ManageChempionshipsFrame)
        self.ChempionshipsLabel.setGeometry(QtCore.QRect(70, 180, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ChempionshipsLabel.setFont(font)
        self.ChempionshipsLabel.setObjectName("ChempionshipsLabel")
        self.ChBackButton = QtWidgets.QPushButton(self.ManageChempionshipsFrame)
        self.ChBackButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.ChBackButton.setObjectName("ChBackButton")
        self.CompetitorFrame = QtWidgets.QFrame(self.centralwidget)
        self.CompetitorFrame.setGeometry(QtCore.QRect(19, 9, 761, 481))
        self.CompetitorFrame.setAutoFillBackground(True)
        self.CompetitorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CompetitorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CompetitorFrame.setObjectName("CompetitorFrame")
        self.CompetitorTable = QtWidgets.QTableWidget(self.CompetitorFrame)
        self.CompetitorTable.setGeometry(QtCore.QRect(60, 210, 641, 261))
        self.CompetitorTable.setObjectName("CompetitorTable")
        self.CompetitorTable.setColumnCount(0)
        self.CompetitorTable.setRowCount(0)
        self.CompetitorLabel = QtWidgets.QLabel(self.CompetitorFrame)
        self.CompetitorLabel.setGeometry(QtCore.QRect(60, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.CompetitorLabel.setFont(font)
        self.CompetitorLabel.setObjectName("CompetitorLabel")
        self.InsertButton = QtWidgets.QPushButton(self.CompetitorFrame)
        self.InsertButton.setGeometry(QtCore.QRect(470, 120, 191, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.InsertButton.setPalette(palette)
        self.InsertButton.setObjectName("InsertButton")
        self.CompetitionComboBox = QtWidgets.QComboBox(self.CompetitorFrame)
        self.CompetitionComboBox.setGeometry(QtCore.QRect(150, 81, 111, 31))
        self.CompetitionComboBox.setObjectName("CompetitionComboBox")
        self.CompetitionLabel = QtWidgets.QLabel(self.CompetitorFrame)
        self.CompetitionLabel.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.CompetitionLabel.setObjectName("CompetitionLabel")
        self.SearchButton = QtWidgets.QPushButton(self.CompetitorFrame)
        self.SearchButton.setGeometry(QtCore.QRect(150, 120, 111, 31))
        self.SearchButton.setObjectName("SearchButton")
        self.CoBackButton = QtWidgets.QPushButton(self.CompetitorFrame)
        self.CoBackButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.CoBackButton.setObjectName("CoBackButton")
        self.ThisChempionshipsLabel = QtWidgets.QLabel(self.centralwidget)
        self.ThisChempionshipsLabel.setGeometry(QtCore.QRect(20, 500, 141, 16))
        self.ThisChempionshipsLabel.setObjectName("ThisChempionshipsLabel")
        self.NameChempionshipsLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameChempionshipsLabel.setGeometry(QtCore.QRect(170, 500, 221, 16))
        self.NameChempionshipsLabel.setObjectName("NameChempionshipsLabel")
        self.ThisChempionshipsLabel.raise_()
        self.NameChempionshipsLabel.raise_()
        self.CompetitorFrame.raise_()
        self.MainFrame.raise_()
        self.ManageChempionshipsFrame.raise_()
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)
        self.LogoutAction = QtWidgets.QAction(AdminWindow)
        self.LogoutAction.setObjectName("LogoutAction")
        self.menu.addAction(self.LogoutAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "MainWindow"))
        self.MenuLabel.setText(_translate("AdminWindow", "Меню администратора"))
        self.GreetLabel.setText(_translate("AdminWindow", "Доброе утро, Имя"))
        self.ManagingChampionshipsButton.setText(_translate("AdminWindow", "Управление чемпионатами"))
        self.ManagingCompetitorsButton.setText(_translate("AdminWindow", "Управление участниками"))
        self.ExpertButton.setText(_translate("AdminWindow", "Привязать эксперта\n"
" к чемпионату"))
        self.CoordinatorButton.setText(_translate("AdminWindow", "Привязать координатора\n"
" к чемпионату"))
        self.ChempionshipsLabel.setText(_translate("AdminWindow", "Список чемпионатов:"))
        self.ChBackButton.setText(_translate("AdminWindow", "Назад"))
        self.CompetitorLabel.setText(_translate("AdminWindow", "Список участников:"))
        self.InsertButton.setText(_translate("AdminWindow", "Добавить участника"))
        self.CompetitionLabel.setText(_translate("AdminWindow", "Компетенция"))
        self.SearchButton.setText(_translate("AdminWindow", "Показать"))
        self.CoBackButton.setText(_translate("AdminWindow", "Назад"))
        self.ThisChempionshipsLabel.setText(_translate("AdminWindow", "Текущий чемпионат:"))
        self.NameChempionshipsLabel.setText(_translate("AdminWindow", "название"))
        self.menu.setTitle(_translate("AdminWindow", "Профиль"))
        self.LogoutAction.setText(_translate("AdminWindow", "Выйти"))

