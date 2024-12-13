from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import sys
import database

class Alert(QMessageBox):
    def error_message(self, message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle('Error')
        self.exec()
        
    def success_message(self, message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle('Success')
        self.exec()


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/login.ui', self)
        
        self.email_input = self.findChild(QLineEdit, 'Email_txt')
        self.password_input = self.findChild(QLineEdit, 'password_txt')
        
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        self.btn_register = self.findChild(QPushButton, 'to_sign_up_btn')
        self.btn_hidepassword = self.findChild(QPushButton, 'hidepassword_btn')
        
        
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_hidepassword.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_hidepassword))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
       
       
    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        
        if email == '':
            msg = Alert()
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        
        if password == '':
            msg = Alert()
            msg.error_message('Please enter password')
            self.password_input.setFocus()
            return
        
        user = database.find_user_by_email_and_password(email, password)
        if user:
            msg = Alert()
            msg.success_message('Login successful')
            self.show_home(user["id"])
        else:
            msg = Alert()
            msg.error_message('Invalid email or password')
    
    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()        
        
    def show_home(self, user_id):
        self.home = Home(user_id)
        self.home.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/signup.ui', self)
        
        self.email_input = self.findChild(QLineEdit, 'email_txt')
        self.name_input = self.findChild(QLineEdit, 'username_txt')
        self.password_input = self.findChild(QLineEdit, 'password_txt')
        self.comfirm_password_input = self.findChild(QLineEdit, 'confirm_password_txt')
        
        self.btn_register = self.findChild(QPushButton, 'signup_btn')
        self.btn_login = self.findChild(QPushButton, 'tosignin_btn')
        self.btn_hidepassword1 = self.findChild(QPushButton, 'hidepassword_btn1')
        self.btn_hidepassword2 = self.findChild(QPushButton, 'hidepassword_btn2')
        
        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.show_login)
        
        self.btn_hidepassword1.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_hidepassword1))
        self.btn_hidepassword2.clicked.connect(lambda: self.hiddenOrShow(self.comfirm_password_input, self.btn_hidepassword2))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
        
    def register(self):
        email = self.email_input.text()
        name  = self.name_input.text()
        password = self.password_input.text()
        comfirm_password = self.comfirm_password_input.text()
        
        if email == ' ':
            msg = Alert()
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        
        if name == ' ':
            msg = Alert()
            msg.error_message('Please enter name')
            self.name_input.setFocus()
            return
        
        if password != comfirm_password:
            msg = Alert()
            msg.error_message('Please enter password')
            self.comfirm_password_input.setFocus()
            return
        
        user = database.find_user_by_email(email)
        if user:
            msg = Alert()
            msg.error_message('Email already exist')
        else:
            database.create_user(email, password)
            msg = Alert()
            msg.success_message('Registration successfully')
            self.show_login()
            
    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()
class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/mainmenu.ui', self)
        self.user_id = user_id  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    app.exec()