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

    table = []
    for row in range(0, int(ui.tableWidget.rowCount())):
        table.append([])
        for col in range(0, int(ui.tableWidget.columnCount() - 1)):
            table[row].append(float(ui.tableWidget.item(row, col + 1).text()))


ui.pushButton.clicked.connect(create_tabl)
ui.pushButton_2.clicked.connect(reset)
ui.pushButton_3.clicked.connect(generate_tabl)
ui.pushButton_4.clicked.connect(calculation)

sys.exit(app.exec_())
