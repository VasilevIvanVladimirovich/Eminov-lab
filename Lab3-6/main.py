import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from form import Ui_Form

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
ui.lineEdit_13.setReadOnly(1)
ui.lineEdit_14.setReadOnly(1)
ui.lineEdit_15.setReadOnly(1)
ui.lineEdit_17.setReadOnly(1)

def on_click():
        N = int(ui.lineEdit_3.text())
        mu = float(ui.lineEdit.text())
        sigma2 = float(ui.lineEdit_2.text())

        alpha = float(ui.lineEdit_4.text())
        mu_check = float(ui.lineEdit_5.text())
        dispersion_check = float(ui.lineEdit_6.text())

        row = np.random.normal(size=N, loc=mu, scale=sigma2 ** .5)
        print(row)

        N = len(row)
        mean = np.mean(row)
        n_sqrt = np.sqrt(N)
        sigma = np.sqrt(sigma2)
        u = scipy.stats.norm.ppf(1 - alpha / 2)
        ui.lineEdit_7.setText(str(round(u,3)))
        Z = np.abs((mean - mu_check) / (sigma / n_sqrt))
        ui.lineEdit_8.setText(str(round(Z,3)))
        if Z <= u:
            ui.lineEdit_9.setText("Выполняется гипотеза H0")
        else:
            ui.lineEdit_9.setText("Выполняется гипотеза H1")

        N = len(row)
        mean = np.mean(row)
        n_sqrt = np.sqrt(N)
        tau = scipy.stats.t.ppf(1 - alpha / 2, N - 1)
        ui.lineEdit_10.setText(str(round(tau,3)))
        s = np.sqrt(np.mean(np.square(row - mean)))
        Z = np.abs((mean - mu_check) / (s / n_sqrt))
        ui.lineEdit_11.setText(str(round(Z,3)))
        if  Z <= tau:
            ui.lineEdit_12.setText("Выполняется гипотеза H0")
        else:
            ui.lineEdit_12.setText("Выполняется гипотеза H1")
        print()

        N = len(row)
        mean = np.mean(row)
        n_sqrt = np.sqrt(N)
        S = np.sqrt(np.mean(np.square(row - mean)))
        z1 = scipy.stats.poisson.ppf(1 - alpha / 2, N - 1)
        z2 = scipy.stats.poisson.ppf(alpha / 2, N - 1)
        Z = N * S ** 2 / dispersion_check ** 2
        ui.lineEdit_13.setText(str(round(Z,3)))
        ui.lineEdit_14.setText(str(round(z1,3)))
        ui.lineEdit_15.setText(str(round(z1,3)))
        if Z <= z1 and Z >= z2:
            ui.lineEdit_17.setText("Выполняется гипотеза H0")
        else:
            ui.lineEdit_17.setText("Выполняется гипотеза H1")

ui.pushButton.clicked.connect(on_click)

sys.exit(app.exec_())


