# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertUsersUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InsertUsers(object):
    def setupUi(self, InsertUsers):
        InsertUsers.setObjectName("InsertUsers")
        InsertUsers.resize(390, 324)
        self.NameLabel = QtWidgets.QLabel(InsertUsers)
        self.NameLabel.setGeometry(QtCore.QRect(66, 30, 55, 16))
        self.NameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NameLabel.setObjectName("NameLabel")
        self.SexLabel = QtWidgets.QLabel(InsertUsers)
        self.SexLabel.setGeometry(QtCore.QRect(66, 60, 55, 16))
        self.SexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SexLabel.setObjectName("SexLabel")
        self.RegionLabel = QtWidgets.QLabel(InsertUsers)
        self.RegionLabel.setGeometry(QtCore.QRect(66, 90, 55, 16))
        self.RegionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RegionLabel.setObjectName("RegionLabel")
        self.EmailLabel = QtWidgets.QLabel(InsertUsers)
        self.EmailLabel.setGeometry(QtCore.QRect(66, 120, 55, 16))
        self.EmailLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.PasswordLabel = QtWidgets.QLabel(InsertUsers)
        self.PasswordLabel.setGeometry(QtCore.QRect(66, 150, 55, 16))
        self.PasswordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.CompetitionLabel = QtWidgets.QLabel(InsertUsers)
        self.CompetitionLabel.setGeometry(QtCore.QRect(20, 210, 101, 20))
        self.CompetitionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CompetitionLabel.setObjectName("CompetitionLabel")
        self.NameEdit = QtWidgets.QLineEdit(InsertUsers)
        self.NameEdit.setGeometry(QtCore.QRect(140, 30, 113, 22))
        self.NameEdit.setObjectName("NameEdit")
        self.RegionEdit = QtWidgets.QLineEdit(InsertUsers)
        self.RegionEdit.setGeometry(QtCore.QRect(140, 90, 113, 22))
        self.RegionEdit.setObjectName("RegionEdit")
        self.EmailEdit = QtWidgets.QLineEdit(InsertUsers)
        self.EmailEdit.setGeometry(QtCore.QRect(140, 120, 113, 22))
        self.EmailEdit.setObjectName("EmailEdit")
        self.PasswordEdit = QtWidgets.QLineEdit(InsertUsers)
        self.PasswordEdit.setGeometry(QtCore.QRect(140, 150, 113, 22))
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.CompetenceComboBox = QtWidgets.QComboBox(InsertUsers)
        self.CompetenceComboBox.setGeometry(QtCore.QRect(140, 210, 73, 22))
        self.CompetenceComboBox.setObjectName("CompetenceComboBox")
        self.MaleRadioButton = QtWidgets.QRadioButton(InsertUsers)
        self.MaleRadioButton.setGeometry(QtCore.QRect(140, 60, 95, 20))
        self.MaleRadioButton.setObjectName("MaleRadioButton")
        self.FemaleRadioButton = QtWidgets.QRadioButton(InsertUsers)
        self.FemaleRadioButton.setGeometry(QtCore.QRect(236, 60, 95, 20))
        self.FemaleRadioButton.setObjectName("FemaleRadioButton")
        self.InsertButton = QtWidgets.QPushButton(InsertUsers)
        self.InsertButton.setGeometry(QtCore.QRect(260, 270, 93, 28))
        self.InsertButton.setObjectName("InsertButton")
        self.BirthLabel = QtWidgets.QLabel(InsertUsers)
        self.BirthLabel.setGeometry(QtCore.QRect(10, 180, 111, 20))
        self.BirthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BirthLabel.setObjectName("BirthLabel")
        self.BirthEdit = QtWidgets.QDateEdit(InsertUsers)
        self.BirthEdit.setGeometry(QtCore.QRect(140, 180, 110, 22))
        self.BirthEdit.setObjectName("BirthEdit")
        self.ErrorLabel = QtWidgets.QLabel(InsertUsers)
        self.ErrorLabel.setGeometry(QtCore.QRect(10, 250, 55, 16))
        self.ErrorLabel.setText("")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.retranslateUi(InsertUsers)
        QtCore.QMetaObject.connectSlotsByName(InsertUsers)

    def retranslateUi(self, InsertUsers):
        _translate = QtCore.QCoreApplication.translate
        InsertUsers.setWindowTitle(_translate("InsertUsers", "Dialog"))
        self.NameLabel.setText(_translate("InsertUsers", "ФИО"))
        self.SexLabel.setText(_translate("InsertUsers", "Пол"))
        self.RegionLabel.setText(_translate("InsertUsers", "Регион"))
        self.EmailLabel.setText(_translate("InsertUsers", "Email"))
        self.PasswordLabel.setText(_translate("InsertUsers", "Пароль"))
        self.CompetitionLabel.setText(_translate("InsertUsers", "Компетенция"))
        self.MaleRadioButton.setText(_translate("InsertUsers", "Мужской"))
        self.FemaleRadioButton.setText(_translate("InsertUsers", "Женский"))
        self.InsertButton.setText(_translate("InsertUsers", "Добавить"))
        self.BirthLabel.setText(_translate("InsertUsers", "Дата рождения"))

