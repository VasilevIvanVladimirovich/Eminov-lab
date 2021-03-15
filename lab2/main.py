import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from form import Ui_Form

#Преобразование в файл .py через команду  " pyuic5 -x name.ui -o name.py "

# Создаём приложение
app = QtWidgets.QApplication(sys.argv)

# Инициализация формы
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


# логика приложения
def bp():
    # Ввод данных

    N = int(ui.lineEdit.text())
    alpha = float(ui.lineEdit_2.text())
    dispersion = float(ui.lineEdit_3.text())

    # Формирумем выборку N элементов из нормального раcпределения
    selection = np.random.normal(scale=np.sqrt(dispersion), size=N)
    ui.textBrowser.setText(str(selection))
    
    # Данные для формулы
    X = np.mean(selection)  # Х - выбоочное среднее или (X c чертой)
    n_sqrt = np.sqrt(N)  # Корень из n
    sigma = np.sqrt(dispersion)  # это Сигма, в отличие от диперсии, которая сигма^2

    # Вычисление доверительного интервала для математического ожидания при известной дисперсии
    u = scipy.stats.norm.ppf(1 - alpha / 2)  # Квантиль нормального распределения для вероятности 1 - (a/2)
    ui.lineEdit_4.setText(str(round(u, 2)))
    #print("Квантиль нормального распределения: " + str(round(u, 2)))  # Вывод квантиля
    delta = u * sigma / n_sqrt
    interval_with_known_dispersion = ((X - delta), (X + delta))

    # Вычисление доверительного интервала для математического ожидания при неизвестной дисперсии
    tau = scipy.stats.t.ppf(1 - alpha / 2,
                            N - 1)  # Квантиль порядка 1-α/2 для распределения Стьюдента с n-1  степенью свободы.
    #print("Квантиль распределения Стьюдента: " + str(round(tau, 2)))  # Вывод квантиля
    ui.lineEdit_5.setText(str(round(tau, 2)))
    S = np.sqrt(np.mean(np.square(selection - X)) * (N / (N - 1)))  # Считаем исправленную выборочную дисперсию
    delta = tau * S / n_sqrt
    interval_with_unknown_dispersion = ((X - delta), (X + delta))

    # Вычисление доверительного интервала для дисперсии.
    z1 = scipy.stats.chi2.ppf(1 - alpha / 2,N - 1)  # Квантиль порядка 1-α/2 для распределения Пирсона с n-1  степенью свободы
    z2 = scipy.stats.chi2.ppf(alpha / 2,N - 1)  # Квантиль порядка α/2 также для распределения Пирсона с n-1  степенью свободы.
    #print("Квантиль порядка 1-α/2 для распределения Пирсона с n-1:  " + str(round(z1, 2)))  # Вывод квантиля
    ui.lineEdit_6.setText(str(round(z1, 2)))
    #print("Квантиль порядка α/2 для распределения Пирсона с n-1:  " + str(round(z2, 2)))  # Вывод квантиля
    ui.lineEdit_7.setText(str(round(z2, 2)))
    interval_of_dispersion = (N * S ** 2 / z1, N * S ** 2 / z2)

    #print("Доверительный интервал при известной дисперисии: " + str(interval_with_known_dispersion))
    ui.lineEdit_8.setText(str(interval_with_known_dispersion))
    #print("Доверительный интервал при неизвестной дисперисии: " + str(interval_with_unknown_dispersion))
    ui.lineEdit_9.setText(str(interval_with_unknown_dispersion))
    #print("Доверительный интервал дисперисии: " + str(interval_of_dispersion))
    ui.lineEdit_10.setText(str(interval_of_dispersion))

ui.pushButton.clicked.connect(bp)

sys.exit(app.exec_())


