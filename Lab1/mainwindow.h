#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "qcustomplot.h"
#include <QDialog>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    void Generate(double * gen);
    double Mediana(double * gen);
    double Scope(double * gen);
    double Mat(double * gen);
    double Disp(double * gen);
    double Quadratic(double * gen);
    double max(double * gen);
    double min(double * gen);
    double getGen(double *gen);
    //QCPItemText *textItem;

    ~MainWindow();
private slots:
    void on_pushButton_clicked();
    //void onMouseMove(QMouseEvent* event);
private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
