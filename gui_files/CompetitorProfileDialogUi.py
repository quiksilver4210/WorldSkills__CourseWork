# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompetitorProfileDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CompetitorProfileDialog(object):
    def setupUi(self, CompetitorProfileDialog):
        CompetitorProfileDialog.setObjectName("CompetitorProfileDialog")
        CompetitorProfileDialog.resize(629, 292)
        self.ProfileLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.ProfileLabel.setGeometry(QtCore.QRect(230, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProfileLabel.setFont(font)
        self.ProfileLabel.setObjectName("ProfileLabel")
        self.NameLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.NameLabel.setGeometry(QtCore.QRect(50, 70, 55, 16))
        self.NameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NameLabel.setObjectName("NameLabel")
        self.SexLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.SexLabel.setGeometry(QtCore.QRect(50, 100, 55, 16))
        self.SexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SexLabel.setObjectName("SexLabel")
        self.BirthLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.BirthLabel.setGeometry(QtCore.QRect(4, 130, 101, 20))
        self.BirthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BirthLabel.setObjectName("BirthLabel")
        self.CountryLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.CountryLabel.setGeometry(QtCore.QRect(50, 190, 55, 16))
        self.CountryLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CountryLabel.setObjectName("CountryLabel")
        self.IdLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.IdLabel.setGeometry(QtCore.QRect(50, 160, 55, 16))
        self.IdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IdLabel.setObjectName("IdLabel")
        self.PhoneLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.PhoneLabel.setGeometry(QtCore.QRect(50, 220, 55, 16))
        self.PhoneLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.EmailLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.EmailLabel.setGeometry(QtCore.QRect(50, 250, 55, 16))
        self.EmailLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.InfoNameLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.InfoNameLabel.setGeometry(QtCore.QRect(130, 70, 201, 20))
        self.InfoNameLabel.setText("")
        self.InfoNameLabel.setObjectName("InfoNameLabel")
        self.InfoSexLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.InfoSexLabel.setGeometry(QtCore.QRect(130, 100, 201, 20))
        self.InfoSexLabel.setText("")
        self.InfoSexLabel.setObjectName("InfoSexLabel")
        self.InfoPhoneLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.InfoPhoneLabel.setGeometry(QtCore.QRect(130, 220, 201, 20))
        self.InfoPhoneLabel.setText("")
        self.InfoPhoneLabel.setObjectName("InfoPhoneLabel")
        self.InfoBirthLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.InfoBirthLabel.setGeometry(QtCore.QRect(130, 130, 201, 20))
        self.InfoBirthLabel.setText("")
        self.InfoBirthLabel.setObjectName("InfoBirthLabel")
        self.InfoIdLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.InfoIdLabel.setGeometry(QtCore.QRect(130, 160, 201, 20))
        self.InfoIdLabel.setText("")
        self.InfoIdLabel.setObjectName("InfoIdLabel")
        self.InfoCountryLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.InfoCountryLabel.setGeometry(QtCore.QRect(130, 190, 201, 20))
        self.InfoCountryLabel.setText("")
        self.InfoCountryLabel.setObjectName("InfoCountryLabel")
        self.InfoEmailLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.InfoEmailLabel.setGeometry(QtCore.QRect(130, 250, 201, 20))
        self.InfoEmailLabel.setText("")
        self.InfoEmailLabel.setObjectName("InfoEmailLabel")
        self.NewPasswordLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.NewPasswordLabel.setGeometry(QtCore.QRect(410, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewPasswordLabel.setFont(font)
        self.NewPasswordLabel.setObjectName("NewPasswordLabel")
        self.EnterPasswordLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.EnterPasswordLabel.setGeometry(QtCore.QRect(390, 80, 161, 20))
        self.EnterPasswordLabel.setObjectName("EnterPasswordLabel")
        self.NewPasswordEdit = QtWidgets.QLineEdit(CompetitorProfileDialog)
        self.NewPasswordEdit.setGeometry(QtCore.QRect(390, 110, 201, 22))
        self.NewPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPasswordEdit.setObjectName("NewPasswordEdit")
        self.RepeatNewPasswordEdit = QtWidgets.QLineEdit(CompetitorProfileDialog)
        self.RepeatNewPasswordEdit.setGeometry(QtCore.QRect(390, 170, 201, 22))
        self.RepeatNewPasswordEdit.setText("")
        self.RepeatNewPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RepeatNewPasswordEdit.setObjectName("RepeatNewPasswordEdit")
        self.RepeatPasswordLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.RepeatPasswordLabel.setGeometry(QtCore.QRect(390, 140, 181, 20))
        self.RepeatPasswordLabel.setObjectName("RepeatPasswordLabel")
        self.PasswordCheckBox = QtWidgets.QCheckBox(CompetitorProfileDialog)
        self.PasswordCheckBox.setGeometry(QtCore.QRect(390, 200, 161, 20))
        self.PasswordCheckBox.setObjectName("PasswordCheckBox")
        self.SaveButton = QtWidgets.QPushButton(CompetitorProfileDialog)
        self.SaveButton.setGeometry(QtCore.QRect(400, 260, 81, 28))
        self.SaveButton.setObjectName("SaveButton")
        self.ExitButton = QtWidgets.QPushButton(CompetitorProfileDialog)
        self.ExitButton.setGeometry(QtCore.QRect(500, 260, 81, 28))
        self.ExitButton.setObjectName("ExitButton")
        self.ErrorLabel = QtWidgets.QLabel(CompetitorProfileDialog)
        self.ErrorLabel.setGeometry(QtCore.QRect(324, 230, 141, 20))
        self.ErrorLabel.setText("")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.retranslateUi(CompetitorProfileDialog)
        QtCore.QMetaObject.connectSlotsByName(CompetitorProfileDialog)

    def retranslateUi(self, CompetitorProfileDialog):
        _translate = QtCore.QCoreApplication.translate
        CompetitorProfileDialog.setWindowTitle(_translate("CompetitorProfileDialog", "Dialog"))
        self.ProfileLabel.setText(_translate("CompetitorProfileDialog", "Мой профиль"))
        self.NameLabel.setText(_translate("CompetitorProfileDialog", "Имя"))
        self.SexLabel.setText(_translate("CompetitorProfileDialog", "Пол"))
        self.BirthLabel.setText(_translate("CompetitorProfileDialog", "Дата рождения"))
        self.CountryLabel.setText(_translate("CompetitorProfileDialog", "Страна"))
        self.IdLabel.setText(_translate("CompetitorProfileDialog", "ID"))
        self.PhoneLabel.setText(_translate("CompetitorProfileDialog", "Телефон"))
        self.EmailLabel.setText(_translate("CompetitorProfileDialog", "Email"))
        self.NewPasswordLabel.setText(_translate("CompetitorProfileDialog", "Смена пароля"))
        self.EnterPasswordLabel.setText(_translate("CompetitorProfileDialog", "Введите новый пароль:"))
        self.RepeatPasswordLabel.setText(_translate("CompetitorProfileDialog", "Повторите новый пароль:"))
        self.PasswordCheckBox.setText(_translate("CompetitorProfileDialog", "Показать пароль"))
        self.SaveButton.setText(_translate("CompetitorProfileDialog", "Сохранить"))
        self.ExitButton.setText(_translate("CompetitorProfileDialog", "Выход"))

