#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "qcustomplot.h"
#include <QDoubleSpinBox>
#include <ctime>
#include <cmath>
#include <QApplication>
#include <QDialog>

    QString ar;
    int a,b,n,m;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowTitle("Лаборатная работа №1");
    ui->lineEdit_9->setReadOnly(true);
    ui->lineEdit_10->setReadOnly(true);
    ui->lineEdit_5->setReadOnly(true);
    ui->lineEdit_6->setReadOnly(true);
    ui->lineEdit_7->setReadOnly(true);
    ui->textBrowser->setReadOnly(true);
    //textItem = new QCPItemText(ui->customPlot);
    //connect(ui->customPlot, &QCustomPlot::mouseMove, this, &MainWindow::onMouseMove);
}

/*void MainWindow::onMouseMove(QMouseEvent *event)
{
QCustomPlot* customPlot = qobject_cast<QCustomPlot*>(sender());
double x = customPlot->xAxis->pixelToCoord(event->pos().x());
double y = customPlot->yAxis->pixelToCoord(event->pos().y());
textItem->setText(QString("(%1, %2)").arg(round(x*1000)/1000).arg(round(y*1000)/1000));
textItem->position->setCoords(QPointF(x, y));
textItem->setFont(QFont(font().family(), 10));
customPlot->replot();
}*/

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::Generate(double * gen)
{
    for(int i=0;i<n;i++)
    {
        gen[i] =(double)(rand())/RAND_MAX * (b - a) + a;
        ar += QString::number(i+1)+")  " + QString::number(gen[i]) + "\n" ;
    }
}

double MainWindow::Mediana(double * gen)
{
   int min=0;
   double smen;
   for(int i=0;i<n;i++)
   {
       for(int j=i+1;j<n;j++)
       {
           if(gen[j]<gen[min]) min= j;
       }
       if(gen[min]==gen[i]) continue;
       smen=gen[i];
       gen[i]=gen[min];
       gen[min]=smen;
   }


    if(n % 2 == 1)
    {
        return gen[((n)/2)];
    }
    if(n % 2 == 0)
    {
        return (gen[(n-1)/2] + gen[((n-1)/2)+1] )/ 2;
    }
}

double MainWindow::Mat(double * gen)
{
    double sum=0;
    for(int i=0;i<n;i++)
    {
        sum += gen[i];
    }
    return sum/n;
}

double MainWindow::Disp(double * gen)
{
    double sum=0;
    for(int i = 0; i < n; i++)
    {
      sum+=(gen[i] - Mat(gen)) * (gen[i]-Mat(gen));
    }
    return sum / n;
}

double MainWindow::Quadratic(double * gen)
{
    return sqrt(Disp(gen));
}

double MainWindow::max(double * gen)
{
    double max=gen[0];
    for(int i=1;i<n;i++)
    {
        if (gen[i] > max) max = gen[i];
    }
    return max;

}

double MainWindow::min(double * gen)
{
    double min=gen[0];
    for(int i=1;i<n;i++)
    {
        if(gen[i] < min) min = gen[i];

    }
    return min;
}



double MainWindow::Scope(double * gen)
{
    double max=gen[0],min=gen[0];
    for(int i=1;i<n;i++)
    {
        if (gen[i] > max) max = gen[i];
        if(gen[i] < min) min = gen[i];

    }
    return max-min;
}

double getGen(double *gen)
{
    return *gen;
}

void MainWindow::on_pushButton_clicked()
{
    ar="";
    ui->customPlot->clearPlottables();
    a = ui->lineEdit->text().toInt();
    b = ui->lineEdit_2->text().toInt();
    n = ui->lineEdit_8->text().toInt();
    m = ui->lineEdit_3->text().toInt();

   double *gen = new double [n];
   Generate(gen);
    ui->textBrowser->setText(ar); //Вывод ряда
    ui->lineEdit_5->setText(QString::number(Mediana(gen))); //Медиана
    ui->lineEdit_6->setText(QString::number(Scope(gen))); //Размах
    ui->lineEdit_7->setText(QString::number(Disp(gen))); //Дисперсия ? 0,08
    ui->lineEdit_9->setText(QString::number(Mat(gen)));//Выборочное среднее около 0,5
    ui->lineEdit_10->setText(QString::number(Quadratic(gen)));//среднееквадратичное

    double h,hh=0;
    double ni;
    h = double(b-a)/m;
    QVector<double> x1(m), y1(m);
    for (int i=0; i<m; i++)
    {
      ni=0;
      for(int j = 0; j<n;j++)
      {
    if(gen[j] >= double(a)+hh and gen[j] < double(a)+hh+h) ni++;
         else continue;
      }
       x1[i] = double(a)+hh+(h/2);
       y1[i] = ni/(n*h);
       hh+=h;
      }
    double maxY=a,minY=b;
       for(int i=0; i<m; i++)
        {
            if(y1[i]>maxY) maxY = y1[i];
            if(y1[i]<minY) minY = y1[i];
        }
    ui->customPlot->xAxis->setRange(0,b+0.5);
    ui->customPlot->yAxis->setRange(0,maxY+minY); //сюда надо вставить максимальное h
    QCPBars *bars1 = new QCPBars(ui->customPlot->xAxis, ui->customPlot->yAxis);
    bars1->setData(x1, y1,true);
    bars1->setWidth(h);
    ui->customPlot->replot();
    delete [] gen;
}
