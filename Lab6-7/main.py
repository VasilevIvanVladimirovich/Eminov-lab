import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from forms import Ui_Form

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

ui.lineEdit_7.setReadOnly(1)
ui.lineEdit_8.setReadOnly(1)
ui.lineEdit_9.setReadOnly(1)
ui.lineEdit_10.setReadOnly(1)
ui.lineEdit_11.setReadOnly(1)
ui.lineEdit_12.setReadOnly(1)

def on_click():
    N_1=int(ui.lineEdit_3.text())
    mu_1=float(ui.lineEdit.text())
    sigma2=float(ui.lineEdit_2.text())
    N_2=int(ui.lineEdit_5.text())
    mu_2=float(ui.lineEdit_4.text())
    alpha=float(ui.lineEdit_6.text())





ui.pushButton.clicked.connect(on_click)







    sys.exit(app.exec_())
