# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 319)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.textBrowser)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.formLayout_3)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Объём выборки (10,50,100)"))
        self.label_2.setText(_translate("Form", "Значения альфы (0.01,0.05,0.1)"))
        self.label_3.setText(_translate("Form", "Значение диспесии (1)"))
        self.label_4.setText(_translate("Form", "Квантиль нормального рспределения"))
        self.label_5.setText(_translate("Form", "Квантиль распредеение Стьюдента"))
        self.label_6.setText(_translate("Form", "Квантиль порядка 1-α/2 для распределения Пирсона с n-1"))
        self.label_7.setText(_translate("Form", "Квантиль порядка α/2 для распределения Пирсона с n-1"))
        self.label_8.setText(_translate("Form", "Доверительный интервал при известной дисперисии"))
        self.label_9.setText(_translate("Form", "Доверительный интервал при неизвестной дисперисии"))
        self.label_10.setText(_translate("Form", "Доверительный интервал дисперисии"))
        self.pushButton.setText(_translate("Form", "Расчёт"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())