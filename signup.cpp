#include "signup.h"
#include "ui_signup.h"
#include <QPixmap>

SignUp::SignUp(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SignUp)
{
    ui->setupUi(this);
    QPixmap pix(":/img/signup1.png");
    int w = ui->Lpic->width();
    int h = ui->Lpic->height();
    ui->Lpic->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));
}

SignUp::~SignUp()
{
    delete ui;
}
