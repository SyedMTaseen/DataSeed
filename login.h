#ifndef LOGIN_H
#define LOGIN_H

#include <QMainWindow>
#include"home.h"
#include"signup.h"

namespace Ui {
class Login;
}

class Login : public QMainWindow
{
    Q_OBJECT

public:
    explicit Login(QWidget *parent = 0);
    ~Login();

private slots:
    void on_loginButton_clicked();

    void on_pushButton_clicked();

private:
    Ui::Login *ui;
    Home *homeobj;
    SignUp *signupobj;
};

#endif // LOGIN_H
