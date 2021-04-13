# k - кол-во предприятий (факторы А)
# l - техгнологии (факторы B)
# n - кол-во столбцов

# a - уровень значимости

# VA,VB,VAB - надо сравнить гипотезы

#
# 1 столбце - номер строки: n - кол-во столбцов, строки = k*l
# 2 столбец сначала А и обход по B
# 3 - n столбцы это вводимые данные
#


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
from PyQt5.QtWidgets import QTableWidgetItem

from form import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.lineEdit_7.setReadOnly(1)
ui.lineEdit_6.setReadOnly(1)
ui.lineEdit_5.setReadOnly(1)
ui.lineEdit_10.setReadOnly(1)
ui.lineEdit_11.setReadOnly(1)
ui.lineEdit_12.setReadOnly(1)
ui.lineEdit_14.setReadOnly(1)
ui.lineEdit_15.setReadOnly(1)
ui.lineEdit_13.setReadOnly(1)


def create_tabl():  # Инициализация таблицы
    if ui.lineEdit.text() == '' or ui.lineEdit_2.text() == '' or ui.lineEdit_3.text() == '' or ui.lineEdit_4.text() == '':
        reset()
        return 0
    k = int(ui.lineEdit.text())
    l = int(ui.lineEdit_2.text())
    n = int(ui.lineEdit_3.text())

    ui.tableWidget.setRowCount(k * l)
    ui.tableWidget.setColumnCount(n + 1)
    column_labels = ['AB']
    for i in range(1, n + 1):
        column_labels.insert(i, str(i))

    ui.tableWidget.setHorizontalHeaderLabels(column_labels)

    i = 0
    for a in range(1, k + 1):  # Вывод первого столбца
        for b in range(1, l + 1):
            out = QTableWidgetItem(str(a) + str(b))
            ui.tableWidget.setItem(i, 0, out)
            ui.tableWidget.item(i, 0).setBackground(QtGui.QColor(180, 250, 169))
            ui.tableWidget.item(i, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            i += 1


def reset():
    ui.lineEdit.clear()
    ui.lineEdit_2.clear()
    ui.lineEdit_3.clear()
    ui.lineEdit_4.clear()
    ui.tableWidget.clear()
    ui.lineEdit_7.clear()
    ui.lineEdit_6.clear()
    ui.lineEdit_5.clear()
    ui.lineEdit_8.clear()
    ui.lineEdit_9.clear()
    ui.lineEdit_10.clear()
    ui.lineEdit_11.clear()
    ui.lineEdit_12.clear()
    ui.lineEdit_14.clear()
    ui.lineEdit_15.clear()
    ui.lineEdit_13.clear()

def generate_tabl():
    if ui.lineEdit_8.text() == '' or ui.lineEdit_9.text() == '':
        ui.lineEdit_8.setText('1')
        ui.lineEdit_9.setText('0')
    M = float(ui.lineEdit_9.text())
    D = float(ui.lineEdit_8.text())
    for row in range(0, ui.tableWidget.rowCount()):
        for col in range(1, ui.tableWidget.columnCount()):
            gen = np.random.normal(M, D)
            out = QTableWidgetItem(str(round(gen, 3)))
            ui.tableWidget.setItem(row, col, out)


def calculation():
    k = int(ui.lineEdit.text())
    l = int(ui.lineEdit_2.text())
    n = int(ui.lineEdit_3.text())
    alpha = float(ui.lineEdit_4.text())
    N = k * l * n
    table = []
    for row in range(0, int(ui.tableWidget.rowCount())):
        table.append([])
        for col in range(0, int(ui.tableWidget.columnCount() - 1)):
            table[row].append(float(ui.tableWidget.item(row, col + 1).text()))

    # расчёты
    c_zero = np.sum(np.square(table))
    c = np.sum(table)
    q = c_zero - (c ** 2 / N)

    number_row = 1
    summa = 0
    ci = []
    for row in table:
        if (number_row % l == 0):
            summa += sum(row)
            ci.append(summa)
            summa = 0
        else:
            summa += sum(row)
        number_row += 1

    q_a = k / N * np.sum(np.square(ci)) - c ** 2 / N

    number_row = 1
    cj = [0] * l
    for row in table:
        cj[number_row % l] += sum(row)
        number_row += 1

    q_b = l / N * np.sum(np.square(cj)) - c ** 2 / N

    cij = []
    for row in table:
        cij.append(sum(row))

    q_a_b = l * k / N * np.sum(np.square(cij)) - q_a - q_b - c ** 2 / N

    q_z = c_zero - 1 / n * np.sum(np.square(cij))

    summa_q = q_a + q_b + q_a_b + q_z

    v = N - 1
    v_a = k - 1
    v_b = l - 1
    v_a_b = k * l - (k + l - 1)
    v_z = k * l * (n - 1)

    s_pow = q / v
    s_pow_a = q_a / v_a
    s_pow_b = q_b / v_b
    s_pow_a_b = q_a_b / v_a_b
    s_pow_z = q_z / v_z

    f_a = s_pow_a / s_pow_z
    f_b = s_pow_b / s_pow_z
    f_a_b = s_pow_a_b / s_pow_z

    crit_a = scipy.stats.f.ppf(q=1 - alpha, dfn=v_a, dfd=v_z)
    crit_b = scipy.stats.f.ppf(q=1 - alpha, dfn=v_b, dfd=v_z)
    crit_a_b = scipy.stats.f.ppf(q=1 - alpha, dfn=v_a_b, dfd=v_z)

    is_a = f_a > crit_a
    is_b = f_b > crit_b
    is_a_b = f_a_b > crit_a_b

    # вывод
    ui.lineEdit_7.setText(str(f_a))
    ui.lineEdit_6.setText(str(f_b))
    ui.lineEdit_5.setText(str(f_a_b))

    ui.lineEdit_10.setText(str(crit_a))
    ui.lineEdit_11.setText(str(crit_b))
    ui.lineEdit_12.setText(str(crit_a_b))

    ui.lineEdit_14.setText(str(is_a))
    ui.lineEdit_15.setText(str(is_b))
    ui.lineEdit_13.setText(str(is_a_b))



ui.pushButton.clicked.connect(create_tabl)
ui.pushButton_2.clicked.connect(reset)
ui.pushButton_3.clicked.connect(generate_tabl)
ui.pushButton_4.clicked.connect(calculation)

sys.exit(app.exec_())
