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


def check_5(row1, row2, alpha):
    N = len(row1)
    M = len(row2)
    mean1 = np.mean(row1)
    mean2 = np.mean(row2)

    S1 = np.mean(np.square(row1 - mean1))
    S2 = np.mean(np.square(row2 - mean2))
    S = ((N - 1) * S1 + (M - 1) * S2) / (M + N + 2)
    s = np.sqrt(S)

    tau = scipy.stats.t.ppf(1 - alpha / 2, N + M - 2)

    Z = np.abs(mean1 - mean2) / s * np.sqrt((M * N) / (M + N))
    ui.lineEdit_7.setText(str(round(Z, 3)))
    ui.lineEdit_8.setText(str(round(tau, 3)))
    return Z <= tau

def check_6(row, mu, sigma2, alpha, m):
    if m == 0:
        m = int(1 + np.floor(3.22 * np.log10(len(row))))
    min = np.min(row)
    max = np.max(row)
    h = (max - min) / m
    delta_sum = 0
    for i in range(m):
        n = np.sum((row >= min + h * i) & (row <= min + h * (i + 1)))
        p = scipy.stats.norm.cdf(min + h * (i + 1), mu, sigma2) - scipy.stats.norm.cdf(min + h * i, mu, sigma2)
        delta = (n - len(row) * p) ** 2 / (len(row) * p)
        delta_sum += delta

    tau = scipy.stats.poisson.ppf(1 - alpha / 2, m - 1)
    ui.lineEdit_10.setText(str(round(delta_sum, 3)))
    ui.lineEdit_11.setText(str(round(tau, 3)))
    return np.abs(delta_sum) <= tau

def make_row(N, mu, sigma2):
    row = np.random.normal(size=int(N), loc=mu, scale=sigma2 ** .5)
    return row


def on_click():
    N_1 = int(ui.lineEdit_3.text())
    mu_1 = float(ui.lineEdit.text())
    sigma2 = float(ui.lineEdit_2.text())
    N_2 = int(ui.lineEdit_5.text())
    mu_2 = float(ui.lineEdit_4.text())
    alpha = float(ui.lineEdit_6.text())
    m=float(ui.lineEdit_13.text())
    num_row1 = []
    num_row2 = []
    num_row1 = make_row(N_1, mu_1, sigma2)
    num_row2 = make_row(N_2, mu_2, sigma2)
    if check_5(num_row1, num_row2, alpha):
        ui.lineEdit_9.setText("Выполняется гипотеза H0")
    else:
        ui.lineEdit_9.setText("Выполняется гипотеза H1")

    if check_6(num_row2, mu_2, sigma2, alpha, m):
        ui.lineEdit_12.setText("Выполняется гипотеза H0")
    else:
        ui.lineEdit_12.setText("Выполняется гипотеза H1")

ui.pushButton.clicked.connect(on_click)
sys.exit(app.exec_())
