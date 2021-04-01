#include "mainwindow.h"
#include "qcustomplot.h"
#include "ui_mainwindow.h"
#include <QWidget>
#include <ctime>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <QApplication>
#include <QDialog>

QString debug="";
QString genarr="";
QString i_del_n="";
QString i_minus_one_del_n="";

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->lineEdit_5->setReadOnly(true);
    ui->lineEdit_6->setReadOnly(true);
    ui->lineEdit_7->setReadOnly(true);
    ui->textBrowser->setReadOnly(true);
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

double MainWindow::DPlusFunc(double *array,int N,int a)
{
    double *buff=new double[N];
     i_del_n+="i/n";
     i_del_n+="\n";
    for(int i = 0;i<N;i++)
    {
        i_del_n+=QString::number(i+1)+": "+QString::number((double(i+1)/double(N))) +"\n";
        buff[i]=(double(i+1)/double(N)) - array[i];
    }
    double max=a;
    for(int i=0; i<N; i++)
            {
                if(buff[i] > max) max = buff[i];
            }
    debug+="D+ "+QString::number(max) + "\n";
    delete [] buff;
    return max;
}

double MainWindow::DMinusFunc(double *array,int N,int a)
{
    double *buff=new double[N];
    i_minus_one_del_n+= "i-1/n";
    i_minus_one_del_n+= "\n";
    for(int i = 0;i<N;i++)
    {
        i_minus_one_del_n+=QString::number(i+1)+": "+QString::number((double(i)/double(N)))+"\n";
        buff[i]=array[i]-(double(i)/double(N));
    }

    double max=a;
    for(int i=0; i<N; i++)
            {
                if(buff[i]>max) max = buff[i];
            }
    debug+="D- "+QString::number(max) + "\n";
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
    return sqrt(double(1/(2*double(N)))*log(2/(1-alpha)));
}

void MainWindow::on_pushButton_clicked()
{
    ui->customPlot->clearPlottables();
    debug="";
    genarr="";
    i_del_n="";
    i_minus_one_del_n="";
    srand(time(NULL));
    int a = ui->lineEdit_2->text().toInt();
    int b = ui->lineEdit_3->text().toInt();
    int N = ui->lineEdit->text().toInt();
    double alpha = ui->lineEdit_4->text().toDouble();
    double *array=new double[N];
    Generate(array,N,a,b);
    std::sort(array,array+N);
    for(int i = 0;i<N;i++) genarr+="x" + QString::number(i+1) +"= " + QString::number(array[i])+"\n";
    double D_plus = DPlusFunc(array,N,a);
    double D_minus = DMinusFunc(array,N,a);
    double D=Max(D_plus,D_minus);
    ui->lineEdit_5->setText(QString::number(D));
    double Da=CriticalNum(N,alpha);
    ui->lineEdit_6->setText(QString::number(Da));

    if(D>Da) ui->lineEdit_7->setText("Выполняется гипотеза H1");
    else ui->lineEdit_7->setText("Выполняется гипотеза H0");

    ui->textBrowser->setText(debug);
    ui->textBrowser_2->setText(genarr);
    ui->textBrowser_3->setText(i_del_n);
    ui->textBrowser_4->setText(i_minus_one_del_n);

    double h,hh=0;
    int m = 1+3.22*log(N);
        double ni;
        h = double(b-a)/m;
        QVector<double> x1(m), y1(m);
        for (int i=0; i<m; i++)
        {
          ni=0;
          for(int j = 0; j<N;j++)
          {
        if(array[j] >= double(a)+hh and array[j] < double(a)+hh+h) ni++;
             else continue;
          }
           x1[i] = double(a)+hh+(h/2);
           y1[i] = ni/(N*h);
           hh+=h;
          }
        double maxY=a,minY=b;
           for(int i=0; i<m; i++)
            {
                if(y1[i]>maxY) maxY = y1[i];
                if(y1[i]<minY) minY = y1[i];
            }
        ui->customPlot->xAxis->setRange(0,b);
        ui->customPlot->yAxis->setRange(0,maxY+minY); //сюда надо вставить максимальное h
        QCPBars *bars1 = new QCPBars(ui->customPlot->xAxis, ui->customPlot->yAxis);
        bars1->setData(x1, y1,true);
        bars1->setWidth(h);
        ui->customPlot->replot();
    delete [] array;
}
