# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChannelSplashUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(498, 369)
        Form.setStyleSheet(_fromUtf8("QToolButton[objectName=\"closetoolButton\"] {\n"
"border:0px;\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:hover {\n"
"image:url(:/images/close_hover.png);\n"
"}\n"
"QToolButton[objectName=\"closetoolButton\"]:pressed {\n"
"image:url(:/images/close_pressed.png);\n"
"}\n"
"\n"
"QWidget[objectName=\"widget\"]{\n"
"background-image: url(:/images/funcell_bg.png);\n"
"}\n"
"QPushButton[objectName=\"pushButton\"]{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton[objectName=\"pushButton_2\"]{\n"
"background-color: rgb(0, 165, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox[objectName=\"checkBox\"]{\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"QWidget[objectName=\"Form\"]{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget[objectName=\"listWidget\"]{\n"
"background-color:transparent;\n"
"border:0px;\n"
"}\n"
"\n"
""))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 501, 80))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 151, 31))
        self.label.setLineWidth(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.closetoolButton = QtGui.QToolButton(self.widget)
        self.closetoolButton.setGeometry(QtCore.QRect(470, 0, 27, 22))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/close_normal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closetoolButton.setIcon(icon)
        self.closetoolButton.setIconSize(QtCore.QSize(27, 22))
        self.closetoolButton.setObjectName(_fromUtf8("closetoolButton"))
        self.line = QtGui.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 77, 500, 2))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, 80, 501, 291))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(220, 110, 45, 45))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/loading1.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_2 = QtGui.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 501, 291))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">渠道闪屏预览<br/></span></p></body></html>", None))
        self.closetoolButton.setText(_translate("Form", "...", None))

import res_rc
