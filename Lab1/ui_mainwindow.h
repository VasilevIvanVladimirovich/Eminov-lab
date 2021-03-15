/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>
#include <qcustomplot.h>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QFormLayout *formLayout_4;
    QFormLayout *formLayout;
    QLineEdit *lineEdit;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QLabel *label;
    QLabel *label_3;
    QLineEdit *lineEdit_8;
    QLabel *label_5;
    QLineEdit *lineEdit_3;
    QFormLayout *formLayout_2;
    QLabel *label_10;
    QLineEdit *lineEdit_9;
    QLineEdit *lineEdit_10;
    QLabel *label_11;
    QLabel *label_7;
    QLineEdit *lineEdit_5;
    QLabel *label_8;
    QLineEdit *lineEdit_6;
    QLabel *label_9;
    QLineEdit *lineEdit_7;
    QFormLayout *formLayout_6;
    QLabel *label_6;
    QTextBrowser *textBrowser;
    QCustomPlot *customPlot;
    QPushButton *pushButton;
    QStatusBar *statusbar;
    QMenuBar *menubar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(622, 443);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        formLayout_4 = new QFormLayout(centralwidget);
        formLayout_4->setObjectName(QString::fromUtf8("formLayout_4"));
        formLayout = new QFormLayout();
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        formLayout->setWidget(0, QFormLayout::FieldRole, lineEdit);

        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_2);

        lineEdit_2 = new QLineEdit(centralwidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        formLayout->setWidget(1, QFormLayout::FieldRole, lineEdit_2);

        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_3);

        lineEdit_8 = new QLineEdit(centralwidget);
        lineEdit_8->setObjectName(QString::fromUtf8("lineEdit_8"));

        formLayout->setWidget(2, QFormLayout::FieldRole, lineEdit_8);

        label_5 = new QLabel(centralwidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        formLayout->setWidget(3, QFormLayout::LabelRole, label_5);

        lineEdit_3 = new QLineEdit(centralwidget);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));

        formLayout->setWidget(3, QFormLayout::FieldRole, lineEdit_3);


        formLayout_4->setLayout(0, QFormLayout::LabelRole, formLayout);

        formLayout_2 = new QFormLayout();
        formLayout_2->setObjectName(QString::fromUtf8("formLayout_2"));
        label_10 = new QLabel(centralwidget);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        formLayout_2->setWidget(0, QFormLayout::LabelRole, label_10);

        lineEdit_9 = new QLineEdit(centralwidget);
        lineEdit_9->setObjectName(QString::fromUtf8("lineEdit_9"));

        formLayout_2->setWidget(0, QFormLayout::FieldRole, lineEdit_9);

        lineEdit_10 = new QLineEdit(centralwidget);
        lineEdit_10->setObjectName(QString::fromUtf8("lineEdit_10"));

        formLayout_2->setWidget(1, QFormLayout::FieldRole, lineEdit_10);

        label_11 = new QLabel(centralwidget);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        formLayout_2->setWidget(1, QFormLayout::LabelRole, label_11);

        label_7 = new QLabel(centralwidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        formLayout_2->setWidget(2, QFormLayout::LabelRole, label_7);

        lineEdit_5 = new QLineEdit(centralwidget);
        lineEdit_5->setObjectName(QString::fromUtf8("lineEdit_5"));

        formLayout_2->setWidget(2, QFormLayout::FieldRole, lineEdit_5);

        label_8 = new QLabel(centralwidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        formLayout_2->setWidget(3, QFormLayout::LabelRole, label_8);

        lineEdit_6 = new QLineEdit(centralwidget);
        lineEdit_6->setObjectName(QString::fromUtf8("lineEdit_6"));

        formLayout_2->setWidget(3, QFormLayout::FieldRole, lineEdit_6);

        label_9 = new QLabel(centralwidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        formLayout_2->setWidget(4, QFormLayout::LabelRole, label_9);

        lineEdit_7 = new QLineEdit(centralwidget);
        lineEdit_7->setObjectName(QString::fromUtf8("lineEdit_7"));

        formLayout_2->setWidget(4, QFormLayout::FieldRole, lineEdit_7);


        formLayout_4->setLayout(0, QFormLayout::FieldRole, formLayout_2);

        formLayout_6 = new QFormLayout();
        formLayout_6->setObjectName(QString::fromUtf8("formLayout_6"));
        label_6 = new QLabel(centralwidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        formLayout_6->setWidget(0, QFormLayout::LabelRole, label_6);

        textBrowser = new QTextBrowser(centralwidget);
        textBrowser->setObjectName(QString::fromUtf8("textBrowser"));

        formLayout_6->setWidget(0, QFormLayout::FieldRole, textBrowser);


        formLayout_4->setLayout(1, QFormLayout::LabelRole, formLayout_6);

        customPlot = new QCustomPlot(centralwidget);
        customPlot->setObjectName(QString::fromUtf8("customPlot"));

        formLayout_4->setWidget(1, QFormLayout::FieldRole, customPlot);

        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        formLayout_4->setWidget(2, QFormLayout::LabelRole, pushButton);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 622, 21));
        MainWindow->setMenuBar(menubar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "\320\224\320\276", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "\320\236\321\202", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "N =", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "\320\234 =", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "\320\234\320\260\321\202 \320\276\320\266\320\270\320\264\320\260\320\275\320\270\320\265", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "\320\241\321\200\320\265\320\264\320\275\320\265\320\265 \320\272\320\262\320\260\320\264\321\200\320\260\321\202\320\270\321\207\320\275\320\276\320\265", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "\320\234\320\265\320\264\320\270\320\260\320\275\320\260", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "\320\240\320\260\320\267\320\274\320\260\321\205", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "\320\224\320\270\321\201\320\277\320\265\321\200\321\201\320\270\321\217", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "\320\230\321\201\321\205\320\276\320\264\320\275\321\213\320\271 \321\200\321\217\320\264", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", "\320\240\320\260\321\201\321\207\321\221\321\202", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
