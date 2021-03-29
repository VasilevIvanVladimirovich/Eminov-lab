#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    void Generate(double *arr,int N,int a,int b);
    double DPlusFunc(double *array,int N,int a);
    double DMinusFunc(double *array,int N,int a);
    double Max(double x1,double x2);
    double CriticalNum(int N,double alpha);
    ~MainWindow();

private slots:
    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
