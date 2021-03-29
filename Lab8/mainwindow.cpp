#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <ctime>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->lineEdit_5->setReadOnly(true);
    ui->lineEdit_6->setReadOnly(true);
    ui->lineEdit_7->setReadOnly(true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::Generate(double *arr,int N,int a,int b)
{
    for(int i=0;i<N;i++)
    {
        arr[i]= (double)(rand())/RAND_MAX * (b - a) + a;
    }
}

int comp(const void * a, const void * b)   // функция сравнения элементов массива
{
    return ( *(double*)a - *(double*)b );            // если результат вычитания равен 0, то числа равны, < 0: x1 < x2; > 0: x1 > x2
}

double MainWindow::DPlusFunc(double *array,int N,int a)
{
    double *buff=new double[N];
    for(int i = 0;i<N;i++)
    {
        buff[i]=abs(((i+1)/N) - array[i]);
    }
    double max=a;
    for(int i=0; i<N; i++)
            {
                if(array[i]>max) max = array[i];
            }
    delete [] buff;
    return max;
}

double MainWindow::DMinusFunc(double *array,int N,int a)
{
    double *buff=new double[N];
    for(int i = 0;i<N;i++)
    {
        buff[i]=abs(array[i]-(i/N));
    }
    double max=a;
    for(int i=0; i<N; i++)
            {
                if(array[i]>max) max = array[i];
            }
    delete [] buff;
    return max;
}

double MainWindow::Max(double x1,double x2)
{
    if(x1>x2) return x1;
    else return x2;
}

double MainWindow::CriticalNum(int N,double alpha)
{
    return sqrt(1/(2*double(N))*log10(2/(1-alpha)));
}

void MainWindow::on_pushButton_clicked()
{
    srand(time(NULL));
    int a = ui->lineEdit_2->text().toInt();
    int b = ui->lineEdit_3->text().toInt();
    int N = ui->lineEdit->text().toInt();
    double alpha = ui->lineEdit_4->text().toDouble();
    double *array=new double[N];
    Generate(array,N,a,b);
    qsort(array,N,sizeof(double),comp);
    double D_plus = DPlusFunc(array,N,a);
    double D_minus = DMinusFunc(array,N,a);
    double D=Max(D_plus,D_minus);
    ui->lineEdit_5->setText(QString::number(D));
    double Da=CriticalNum(N,alpha);
    ui->lineEdit_6->setText(QString::number(Da));

    if(D>Da) ui->lineEdit_7->setText("Выполняется гипотеза H1");
    else ui->lineEdit_7->setText("Выполняется гипотеза H0");

    delete [] array;
}
