# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package.ui'
#
# Created: Fri Apr 24 14:18:40 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(857, 612)
        self.packBtn = QtGui.QPushButton(Dialog)
        self.packBtn.setGeometry(QtCore.QRect(540, 540, 75, 23))
        self.packBtn.setObjectName(_fromUtf8("packBtn"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(420, 80, 411, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.selectKeystore = QtGui.QPushButton(self.groupBox)
        self.selectKeystore.setGeometry(QtCore.QRect(360, 20, 41, 23))
        self.selectKeystore.setObjectName(_fromUtf8("selectKeystore"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 251, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 47, 251, 20))
        self.lineEdit_10.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(90, 72, 251, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 75, 41, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 100, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_12.setGeometry(QtCore.QRect(90, 96, 251, 20))
        self.lineEdit_12.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 10, 411, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 30, 281, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.selectApk = QtGui.QPushButton(self.groupBox_2)
        self.selectApk.setGeometry(QtCore.QRect(360, 30, 31, 23))
        self.selectApk.setObjectName(_fromUtf8("selectApk"))
        self.openfile = QtGui.QPushButton(Dialog)
        self.openfile.setGeometry(QtCore.QRect(650, 540, 75, 23))
        self.openfile.setObjectName(_fromUtf8("openfile"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(420, 230, 421, 80))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox.setGeometry(QtCore.QRect(20, 22, 71, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_14 = QtGui.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_13.setGeometry(QtCore.QRect(70, 48, 281, 20))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.groupBox_6 = QtGui.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 10, 391, 591))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.listWidget = QtGui.QListWidget(self.groupBox_6)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 371, 521))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(190, 30, 161, 20))
        self.label.setStyleSheet(_fromUtf8("rgb(255, 0, 0)"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.selectKeystore, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.selectApk, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.packBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.packBtn.setText(_translate("Dialog", "打包", None))
        self.groupBox.setTitle(_translate("Dialog", "签名", None))
        self.label_2.setText(_translate("Dialog", "keystore文件", None))
        self.selectKeystore.setText(_translate("Dialog", "...", None))
        self.label_3.setText(_translate("Dialog", "keystore密码", None))
        self.label_12.setText(_translate("Dialog", "alias", None))
        self.label_13.setText(_translate("Dialog", "alias密码", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Apk", None))
        self.label_4.setText(_translate("Dialog", "apk文件", None))
        self.selectApk.setText(_translate("Dialog", "...", None))
        self.openfile.setText(_translate("Dialog", "文件所在目录", None))
        self.groupBox_5.setTitle(_translate("Dialog", "TalkingData", None))
        self.checkBox.setText(_translate("Dialog", "Enable", None))
        self.label_14.setText(_translate("Dialog", "appId", None))
        self.groupBox_6.setTitle(_translate("Dialog", "渠道选择", None))
        self.listWidget.setSortingEnabled(True)
        self.pushButton_2.setText(_translate("Dialog", "全选", None))
        self.pushButton_3.setText(_translate("Dialog", "全取消", None))
        self.label.setText(_translate("Dialog", "(双击渠道进行参数配置)", None))

