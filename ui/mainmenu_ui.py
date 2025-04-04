# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/mainmenu.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 0, 931, 650))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Account_page = QtWidgets.QWidget()
        self.Account_page.setEnabled(True)
        self.Account_page.setObjectName("Account_page")
        self.background_frame = QtWidgets.QFrame(parent=self.Account_page)
        self.background_frame.setGeometry(QtCore.QRect(0, 0, 1024, 650))
        self.background_frame.setStyleSheet("background-color:rgb(92, 92, 92);")
        self.background_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background_frame.setObjectName("background_frame")
        self.profile_frame = QtWidgets.QFrame(parent=self.background_frame)
        self.profile_frame.setGeometry(QtCore.QRect(310, 70, 300, 500))
        self.profile_frame.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"border-radius: 30px")
        self.profile_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.profile_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.profile_frame.setObjectName("profile_frame")
        self.username_label = QtWidgets.QLabel(parent=self.profile_frame)
        self.username_label.setGeometry(QtCore.QRect(20, 250, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.username_label.setObjectName("username_label")
        self.useremail_label = QtWidgets.QLabel(parent=self.profile_frame)
        self.useremail_label.setGeometry(QtCore.QRect(20, 300, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        self.useremail_label.setFont(font)
        self.useremail_label.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.useremail_label.setObjectName("useremail_label")
        self.userid_label = QtWidgets.QLabel(parent=self.profile_frame)
        self.userid_label.setGeometry(QtCore.QRect(20, 350, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        self.userid_label.setFont(font)
        self.userid_label.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.userid_label.setObjectName("userid_label")
        self.profile_image_label = QtWidgets.QLabel(parent=self.profile_frame)
        self.profile_image_label.setGeometry(QtCore.QRect(40, 30, 211, 200))
        self.profile_image_label.setText("")
        self.profile_image_label.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/download.png"))
        self.profile_image_label.setObjectName("profile_image_label")
        self.setting = QtWidgets.QPushButton(parent=self.background_frame)
        self.setting.setGeometry(QtCore.QRect(20, 30, 81, 81))
        self.setting.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"")
        self.setting.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/forward-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setting.setIcon(icon)
        self.setting.setObjectName("setting")
        self.stackedWidget.addWidget(self.Account_page)
        self.MyPlaylist_page = QtWidgets.QWidget()
        self.MyPlaylist_page.setObjectName("MyPlaylist_page")
        self.frame_4 = QtWidgets.QFrame(parent=self.MyPlaylist_page)
        self.frame_4.setGeometry(QtCore.QRect(-7, -1, 1031, 651))
        self.frame_4.setStyleSheet("background-color:rgb(92, 92, 92);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(171, 171, 171);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.playlist_frame = QtWidgets.QFrame(parent=self.frame_4)
        self.playlist_frame.setGeometry(QtCore.QRect(20, 140, 450, 150))
        self.playlist_frame.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.playlist_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.playlist_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.playlist_frame.setObjectName("playlist_frame")
        self.plus_playlist_btn = QtWidgets.QPushButton(parent=self.playlist_frame)
        self.plus_playlist_btn.setGeometry(QtCore.QRect(180, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.plus_playlist_btn.setFont(font)
        self.plus_playlist_btn.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 20px;\n"
"")
        self.plus_playlist_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/plus-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.plus_playlist_btn.setIcon(icon1)
        self.plus_playlist_btn.setObjectName("plus_playlist_btn")
        self.playlist_name_txt = QtWidgets.QLabel(parent=self.playlist_frame)
        self.playlist_name_txt.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.playlist_name_txt.setFont(font)
        self.playlist_name_txt.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:20px;\n"
"color: rgb(0, 0, 0);")
        self.playlist_name_txt.setObjectName("playlist_name_txt")
        self.label_5 = QtWidgets.QLabel(parent=self.playlist_frame)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 100, 100))
        self.label_5.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/music-solid.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.playlist_frame_2 = QtWidgets.QFrame(parent=self.frame_4)
        self.playlist_frame_2.setGeometry(QtCore.QRect(480, 140, 450, 150))
        self.playlist_frame_2.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.playlist_frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.playlist_frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.playlist_frame_2.setObjectName("playlist_frame_2")
        self.plus_playlist_btn_2 = QtWidgets.QPushButton(parent=self.playlist_frame_2)
        self.plus_playlist_btn_2.setGeometry(QtCore.QRect(180, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.plus_playlist_btn_2.setFont(font)
        self.plus_playlist_btn_2.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 20px;\n"
"")
        self.plus_playlist_btn_2.setText("")
        self.plus_playlist_btn_2.setIcon(icon1)
        self.plus_playlist_btn_2.setObjectName("plus_playlist_btn_2")
        self.playlist_name_txt_2 = QtWidgets.QLabel(parent=self.playlist_frame_2)
        self.playlist_name_txt_2.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.playlist_name_txt_2.setFont(font)
        self.playlist_name_txt_2.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:20px;\n"
"color: rgb(0, 0, 0);")
        self.playlist_name_txt_2.setObjectName("playlist_name_txt_2")
        self.label_11 = QtWidgets.QLabel(parent=self.playlist_frame_2)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 100, 100))
        self.label_11.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/music-solid.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.playlist_frame_3 = QtWidgets.QFrame(parent=self.frame_4)
        self.playlist_frame_3.setGeometry(QtCore.QRect(20, 310, 450, 150))
        self.playlist_frame_3.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.playlist_frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.playlist_frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.playlist_frame_3.setObjectName("playlist_frame_3")
        self.plus_playlist_btn_3 = QtWidgets.QPushButton(parent=self.playlist_frame_3)
        self.plus_playlist_btn_3.setGeometry(QtCore.QRect(180, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.plus_playlist_btn_3.setFont(font)
        self.plus_playlist_btn_3.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 20px;\n"
"")
        self.plus_playlist_btn_3.setText("")
        self.plus_playlist_btn_3.setIcon(icon1)
        self.plus_playlist_btn_3.setObjectName("plus_playlist_btn_3")
        self.playlist_name_txt_3 = QtWidgets.QLabel(parent=self.playlist_frame_3)
        self.playlist_name_txt_3.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.playlist_name_txt_3.setFont(font)
        self.playlist_name_txt_3.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:20px;\n"
"color: rgb(0, 0, 0);")
        self.playlist_name_txt_3.setObjectName("playlist_name_txt_3")
        self.label_13 = QtWidgets.QLabel(parent=self.playlist_frame_3)
        self.label_13.setGeometry(QtCore.QRect(40, 30, 100, 100))
        self.label_13.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/music-solid.svg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.playlist_frame_4 = QtWidgets.QFrame(parent=self.frame_4)
        self.playlist_frame_4.setGeometry(QtCore.QRect(480, 310, 450, 150))
        self.playlist_frame_4.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.playlist_frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.playlist_frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.playlist_frame_4.setObjectName("playlist_frame_4")
        self.plus_playlist_btn_4 = QtWidgets.QPushButton(parent=self.playlist_frame_4)
        self.plus_playlist_btn_4.setGeometry(QtCore.QRect(180, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.plus_playlist_btn_4.setFont(font)
        self.plus_playlist_btn_4.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 20px;\n"
"")
        self.plus_playlist_btn_4.setText("")
        self.plus_playlist_btn_4.setIcon(icon1)
        self.plus_playlist_btn_4.setObjectName("plus_playlist_btn_4")
        self.playlist_name_txt_4 = QtWidgets.QLabel(parent=self.playlist_frame_4)
        self.playlist_name_txt_4.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.playlist_name_txt_4.setFont(font)
        self.playlist_name_txt_4.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:20px;\n"
"color: rgb(0, 0, 0);")
        self.playlist_name_txt_4.setObjectName("playlist_name_txt_4")
        self.label_16 = QtWidgets.QLabel(parent=self.playlist_frame_4)
        self.label_16.setGeometry(QtCore.QRect(40, 30, 100, 100))
        self.label_16.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/music-solid.svg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.playlist_frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.playlist_frame_5.setGeometry(QtCore.QRect(20, 480, 450, 150))
        self.playlist_frame_5.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.playlist_frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.playlist_frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.playlist_frame_5.setObjectName("playlist_frame_5")
        self.plus_playlist_btn_5 = QtWidgets.QPushButton(parent=self.playlist_frame_5)
        self.plus_playlist_btn_5.setGeometry(QtCore.QRect(180, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.plus_playlist_btn_5.setFont(font)
        self.plus_playlist_btn_5.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 20px;\n"
"")
        self.plus_playlist_btn_5.setText("")
        self.plus_playlist_btn_5.setIcon(icon1)
        self.plus_playlist_btn_5.setObjectName("plus_playlist_btn_5")
        self.playlist_name_txt_5 = QtWidgets.QLabel(parent=self.playlist_frame_5)
        self.playlist_name_txt_5.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.playlist_name_txt_5.setFont(font)
        self.playlist_name_txt_5.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:20px;\n"
"color: rgb(0, 0, 0);")
        self.playlist_name_txt_5.setObjectName("playlist_name_txt_5")
        self.label_18 = QtWidgets.QLabel(parent=self.playlist_frame_5)
        self.label_18.setGeometry(QtCore.QRect(40, 30, 100, 100))
        self.label_18.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/music-solid.svg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.playlist_frame_6 = QtWidgets.QFrame(parent=self.frame_4)
        self.playlist_frame_6.setGeometry(QtCore.QRect(480, 480, 450, 150))
        self.playlist_frame_6.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.playlist_frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.playlist_frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.playlist_frame_6.setObjectName("playlist_frame_6")
        self.plus_playlist_btn_6 = QtWidgets.QPushButton(parent=self.playlist_frame_6)
        self.plus_playlist_btn_6.setGeometry(QtCore.QRect(180, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.plus_playlist_btn_6.setFont(font)
        self.plus_playlist_btn_6.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 20px;\n"
"")
        self.plus_playlist_btn_6.setText("")
        self.plus_playlist_btn_6.setIcon(icon1)
        self.plus_playlist_btn_6.setObjectName("plus_playlist_btn_6")
        self.playlist_name_txt_6 = QtWidgets.QLabel(parent=self.playlist_frame_6)
        self.playlist_name_txt_6.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.playlist_name_txt_6.setFont(font)
        self.playlist_name_txt_6.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:20px;\n"
"color: rgb(0, 0, 0);")
        self.playlist_name_txt_6.setObjectName("playlist_name_txt_6")
        self.label_20 = QtWidgets.QLabel(parent=self.playlist_frame_6)
        self.label_20.setGeometry(QtCore.QRect(40, 30, 100, 100))
        self.label_20.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/music-solid.svg"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.stackedWidget.addWidget(self.MyPlaylist_page)
        self.Mainmenu_page = QtWidgets.QWidget()
        self.Mainmenu_page.setObjectName("Mainmenu_page")
        self.background_frame_2 = QtWidgets.QFrame(parent=self.Mainmenu_page)
        self.background_frame_2.setGeometry(QtCore.QRect(0, 0, 1024, 650))
        self.background_frame_2.setStyleSheet("background-color:rgb(92, 92, 92);")
        self.background_frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background_frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background_frame_2.setObjectName("background_frame_2")
        self.search_bar = QtWidgets.QTextEdit(parent=self.background_frame_2)
        self.search_bar.setGeometry(QtCore.QRect(10, 10, 881, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.search_bar.setFont(font)
        self.search_bar.setStyleSheet("background-color:rgb(171, 171, 171);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.search_bar.setObjectName("search_bar")
        self.for_you = QtWidgets.QLabel(parent=self.background_frame_2)
        self.for_you.setGeometry(QtCore.QRect(10, 80, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        self.for_you.setFont(font)
        self.for_you.setStyleSheet("background-color:rgb(171, 171, 171);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.for_you.setObjectName("for_you")
        self.stackedWidget.addWidget(self.Mainmenu_page)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 650, 1261, 111))
        self.frame.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.start_btn = QtWidgets.QPushButton(parent=self.frame)
        self.start_btn.setGeometry(QtCore.QRect(520, 0, 93, 51))
        self.start_btn.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.start_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/images.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.start_btn.setIcon(icon2)
        self.start_btn.setObjectName("start_btn")
        self.playing_song_txt = QtWidgets.QLabel(parent=self.frame)
        self.playing_song_txt.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.playing_song_txt.setFont(font)
        self.playing_song_txt.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:18px;\n"
"color: rgb(0, 0, 0);")
        self.playing_song_txt.setObjectName("playing_song_txt")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(30, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.last_song = QtWidgets.QPushButton(parent=self.frame)
        self.last_song.setGeometry(QtCore.QRect(420, 0, 93, 51))
        self.last_song.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.last_song.setText("")
        self.last_song.setIcon(icon)
        self.last_song.setObjectName("last_song")
        self.next_song = QtWidgets.QPushButton(parent=self.frame)
        self.next_song.setGeometry(QtCore.QRect(620, 0, 93, 51))
        self.next_song.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.next_song.setText("")
        self.next_song.setIcon(icon)
        self.next_song.setObjectName("next_song")
        self.volume_btn = QtWidgets.QPushButton(parent=self.frame)
        self.volume_btn.setGeometry(QtCore.QRect(890, 40, 93, 51))
        self.volume_btn.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.volume_btn.setText("")
        self.volume_btn.setIcon(icon2)
        self.volume_btn.setObjectName("volume_btn")
        self.volume = QtWidgets.QFrame(parent=self.frame)
        self.volume.setGeometry(QtCore.QRect(1010, 50, 221, 41))
        self.volume.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;")
        self.volume.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.volume.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.volume.setObjectName("volume")
        self.volume_slider = QtWidgets.QSlider(parent=self.volume)
        self.volume_slider.setGeometry(QtCore.QRect(10, 10, 591, 22))
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.song_progress = QtWidgets.QFrame(parent=self.frame)
        self.song_progress.setGeometry(QtCore.QRect(250, 60, 621, 41))
        self.song_progress.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;")
        self.song_progress.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.song_progress.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.song_progress.setObjectName("song_progress")
        self.progress_slider = QtWidgets.QSlider(parent=self.song_progress)
        self.progress_slider.setGeometry(QtCore.QRect(10, 10, 591, 22))
        self.progress_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progress_slider.setObjectName("progress_slider")
        self.home_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.home_frame.setGeometry(QtCore.QRect(0, 0, 101, 651))
        self.home_frame.setAutoFillBackground(False)
        self.home_frame.setStyleSheet("background-color: black")
        self.home_frame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.home_frame.setObjectName("home_frame")
        self.playlist_btn = QtWidgets.QPushButton(parent=self.home_frame)
        self.playlist_btn.setGeometry(QtCore.QRect(10, 110, 81, 81))
        self.playlist_btn.setStyleSheet("background-color: white !important;")
        self.playlist_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/bars-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.playlist_btn.setIcon(icon3)
        self.playlist_btn.setObjectName("playlist_btn")
        self.user_btn = QtWidgets.QPushButton(parent=self.home_frame)
        self.user_btn.setGeometry(QtCore.QRect(10, 10, 81, 81))
        self.user_btn.setStyleSheet("background-color: white !important;")
        self.user_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/user-regular.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.user_btn.setIcon(icon4)
        self.user_btn.setObjectName("user_btn")
        self.search_btn = QtWidgets.QPushButton(parent=self.home_frame)
        self.search_btn.setGeometry(QtCore.QRect(10, 210, 81, 81))
        self.search_btn.setStyleSheet("background-color: white !important;")
        self.search_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/magnifying-glass-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_btn.setIcon(icon5)
        self.search_btn.setObjectName("search_btn")
        self.user_btn.raise_()
        self.playlist_btn.raise_()
        self.search_btn.raise_()
        self.song_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.song_frame.setGeometry(QtCore.QRect(1030, 0, 221, 651))
        self.song_frame.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.song_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.song_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.song_frame.setObjectName("song_frame")
        self.username_label_2 = QtWidgets.QLabel(parent=self.song_frame)
        self.username_label_2.setGeometry(QtCore.QRect(10, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        self.username_label_2.setFont(font)
        self.username_label_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.username_label_2.setObjectName("username_label_2")
        self.username_label_3 = QtWidgets.QLabel(parent=self.song_frame)
        self.username_label_3.setGeometry(QtCore.QRect(10, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        self.username_label_3.setFont(font)
        self.username_label_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.username_label_3.setObjectName("username_label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Not avalable as a guest"))
        self.useremail_label.setText(_translate("MainWindow", "Not avalable as a guest"))
        self.userid_label.setText(_translate("MainWindow", "Not avalable as a guest"))
        self.label_2.setText(_translate("MainWindow", "Your playlists:"))
        self.playlist_name_txt.setText(_translate("MainWindow", "No playlist"))
        self.playlist_name_txt_2.setText(_translate("MainWindow", "No playlist"))
        self.playlist_name_txt_3.setText(_translate("MainWindow", "No playlist"))
        self.playlist_name_txt_4.setText(_translate("MainWindow", "No playlist"))
        self.playlist_name_txt_5.setText(_translate("MainWindow", "No playlist"))
        self.playlist_name_txt_6.setText(_translate("MainWindow", "No playlist"))
        self.search_bar.setPlaceholderText(_translate("MainWindow", "Finding something?"))
        self.for_you.setText(_translate("MainWindow", "For you:"))
        self.playing_song_txt.setText(_translate("MainWindow", "Song name"))
        self.label.setText(_translate("MainWindow", "Artist"))
        self.username_label_2.setText(_translate("MainWindow", "Popular"))
        self.username_label_3.setText(_translate("MainWindow", "Trending"))
