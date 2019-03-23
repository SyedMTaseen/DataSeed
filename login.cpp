#include "login.h"
#include "ui_login.h"
#include <QMessageBox>
#include <QPixmap>

Login::Login(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Login)
{
    ui->setupUi(this);
    QPixmap pix(":/img/login.png");
    int w = ui->LPic->width();
    int h = ui->LPic->height();
    ui->LPic->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));

}

Login::~Login()
{
    delete ui;
}

void Login::on_loginButton_clicked()
{
    QString username = ui->TUname->text();
        QString password = ui->Tpass->text();

        if(username ==  "test" && password == "test") {
            QMessageBox::information(this, "Login", "Username and password is correct");
            hide();
            homeobj = new Home(this);
            homeobj->show();
        }
        else {
            QMessageBox::warning(this,"Login", "Username and password is not correct");
        }
}

void Login::on_pushButton_clicked()
{
    hide();
    signupobj =new SignUp(this);
    signupobj->show();
}
