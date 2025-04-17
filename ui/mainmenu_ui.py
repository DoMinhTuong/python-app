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
        self.profile_image_label = QtWidgets.QLabel(parent=self.profile_frame)
        self.profile_image_label.setGeometry(QtCore.QRect(50, 10, 171, 161))
        self.profile_image_label.setText("")
        self.profile_image_label.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/download.png"))
        self.profile_image_label.setObjectName("profile_image_label")
        self.btn_avatar = QtWidgets.QPushButton(parent=self.profile_frame)
        self.btn_avatar.setGeometry(QtCore.QRect(60, 10, 191, 151))
        self.btn_avatar.setObjectName("btn_avatar")
        self.d_dob = QtWidgets.QDateEdit(parent=self.profile_frame)
        self.d_dob.setGeometry(QtCore.QRect(120, 310, 161, 31))
        self.d_dob.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.d_dob.setObjectName("d_dob")
        self.cb_gender = QtWidgets.QComboBox(parent=self.profile_frame)
        self.cb_gender.setGeometry(QtCore.QRect(120, 360, 161, 31))
        self.cb_gender.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.cb_gender.setObjectName("cb_gender")
        self.cb_gender.addItem("")
        self.cb_gender.addItem("")
        self.cb_gender.addItem("")
        self.label = QtWidgets.QLabel(parent=self.profile_frame)
        self.label.setGeometry(QtCore.QRect(20, 210, 71, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.profile_frame)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.profile_frame)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.profile_frame)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 81, 31))
        self.label_6.setObjectName("label_6")
        self.btn_update_info = QtWidgets.QPushButton(parent=self.profile_frame)
        self.btn_update_info.setGeometry(QtCore.QRect(90, 420, 121, 41))
        self.btn_update_info.setObjectName("btn_update_info")
        self.txt_name = QtWidgets.QLineEdit(parent=self.profile_frame)
        self.txt_name.setGeometry(QtCore.QRect(120, 260, 161, 31))
        self.txt_name.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: rgb(163, 161, 164);\n"
"border-radius: 5px;")
        self.txt_name.setObjectName("txt_name")
        self.txt_email = QtWidgets.QLineEdit(parent=self.profile_frame)
        self.txt_email.setGeometry(QtCore.QRect(120, 210, 161, 31))
        self.txt_email.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: rgb(163, 161, 164);\n"
"border-radius: 5px;")
        self.txt_email.setText("")
        self.txt_email.setObjectName("txt_email")
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
        self.btn_create_playlist = QtWidgets.QPushButton(parent=self.frame_4)
        self.btn_create_playlist.setGeometry(QtCore.QRect(820, 20, 91, 51))
        self.btn_create_playlist.setObjectName("btn_create_playlist")
        self.playlist_widget = QtWidgets.QWidget(parent=self.frame_4)
        self.playlist_widget.setGeometry(QtCore.QRect(10, 90, 921, 551))
        self.playlist_widget.setObjectName("playlist_widget")
        self.stackedWidget.addWidget(self.MyPlaylist_page)
        self.Mainmenu_page = QtWidgets.QWidget()
        self.Mainmenu_page.setObjectName("Mainmenu_page")
        self.background_frame_2 = QtWidgets.QFrame(parent=self.Mainmenu_page)
        self.background_frame_2.setGeometry(QtCore.QRect(0, 0, 1024, 650))
        self.background_frame_2.setStyleSheet("background-color:rgb(92, 92, 92);")
        self.background_frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background_frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background_frame_2.setObjectName("background_frame_2")
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
        self.song_container = QtWidgets.QWidget(parent=self.background_frame_2)
        self.song_container.setGeometry(QtCore.QRect(0, 170, 931, 481))
        self.song_container.setObjectName("song_container")
        self.txt_search = QtWidgets.QLineEdit(parent=self.background_frame_2)
        self.txt_search.setGeometry(QtCore.QRect(10, 10, 801, 61))
        self.txt_search.setStyleSheet("background-color:rgb(171, 171, 171);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.txt_search.setObjectName("txt_search")
        self.btn_search = QtWidgets.QPushButton(parent=self.background_frame_2)
        self.btn_search.setGeometry(QtCore.QRect(820, 10, 91, 61))
        self.btn_search.setStyleSheet("background-color:rgb(171, 171, 171);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.btn_search.setObjectName("btn_search")
        self.stackedWidget.addWidget(self.Mainmenu_page)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 650, 1261, 111))
        self.frame.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btn_play = QtWidgets.QPushButton(parent=self.frame)
        self.btn_play.setGeometry(QtCore.QRect(520, 0, 93, 51))
        self.btn_play.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.btn_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/images.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_play.setIcon(icon1)
        self.btn_play.setObjectName("btn_play")
        self.lbl_curr_name = QtWidgets.QLabel(parent=self.frame)
        self.lbl_curr_name.setGeometry(QtCore.QRect(100, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        self.lbl_curr_name.setFont(font)
        self.lbl_curr_name.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;\n"
"font-size:18px;\n"
"color: rgb(0, 0, 0);")
        self.lbl_curr_name.setObjectName("lbl_curr_name")
        self.lbl_curr_artist = QtWidgets.QLabel(parent=self.frame)
        self.lbl_curr_artist.setGeometry(QtCore.QRect(100, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_curr_artist.setFont(font)
        self.lbl_curr_artist.setStyleSheet("color:rgb(255, 255, 255);")
        self.lbl_curr_artist.setObjectName("lbl_curr_artist")
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
        self.btn_volume = QtWidgets.QPushButton(parent=self.frame)
        self.btn_volume.setGeometry(QtCore.QRect(900, 50, 93, 51))
        self.btn_volume.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.btn_volume.setText("")
        self.btn_volume.setIcon(icon1)
        self.btn_volume.setObjectName("btn_volume")
        self.volume = QtWidgets.QFrame(parent=self.frame)
        self.volume.setGeometry(QtCore.QRect(1010, 50, 221, 41))
        self.volume.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;")
        self.volume.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.volume.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.volume.setObjectName("volume")
        self.slider_volume = QtWidgets.QSlider(parent=self.volume)
        self.slider_volume.setGeometry(QtCore.QRect(10, 10, 201, 22))
        self.slider_volume.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_volume.setObjectName("slider_volume")
        self.song_progress = QtWidgets.QFrame(parent=self.frame)
        self.song_progress.setGeometry(QtCore.QRect(250, 60, 621, 41))
        self.song_progress.setStyleSheet("background-color:rgb(118, 118, 118);\n"
"border-radius: 15px;")
        self.song_progress.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.song_progress.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.song_progress.setObjectName("song_progress")
        self.slider_duration = QtWidgets.QSlider(parent=self.song_progress)
        self.slider_duration.setGeometry(QtCore.QRect(10, 10, 591, 22))
        self.slider_duration.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_duration.setObjectName("slider_duration")
        self.lbl_curr_img = QtWidgets.QLabel(parent=self.frame)
        self.lbl_curr_img.setGeometry(QtCore.QRect(10, 10, 71, 81))
        self.lbl_curr_img.setScaledContents(True)
        self.lbl_curr_img.setObjectName("lbl_curr_img")
        self.lbl_time = QtWidgets.QLabel(parent=self.frame)
        self.lbl_time.setGeometry(QtCore.QRect(180, 70, 58, 16))
        self.lbl_time.setObjectName("lbl_time")
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/bars-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.playlist_btn.setIcon(icon2)
        self.playlist_btn.setObjectName("playlist_btn")
        self.user_btn = QtWidgets.QPushButton(parent=self.home_frame)
        self.user_btn.setGeometry(QtCore.QRect(10, 10, 81, 81))
        self.user_btn.setStyleSheet("background-color: white !important;")
        self.user_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/user-regular.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.user_btn.setIcon(icon3)
        self.user_btn.setObjectName("user_btn")
        self.btn_song_list = QtWidgets.QPushButton(parent=self.home_frame)
        self.btn_song_list.setGeometry(QtCore.QRect(10, 210, 81, 81))
        self.btn_song_list.setStyleSheet("background-color: white !important;")
        self.btn_song_list.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/MinhTuong/python-app/ui/../img/magnifying-glass-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_song_list.setIcon(icon4)
        self.btn_song_list.setObjectName("btn_song_list")
        self.user_btn.raise_()
        self.playlist_btn.raise_()
        self.btn_song_list.raise_()
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_avatar.setText(_translate("MainWindow", "PushButton"))
        self.cb_gender.setItemText(0, _translate("MainWindow", "None"))
        self.cb_gender.setItemText(1, _translate("MainWindow", "Male"))
        self.cb_gender.setItemText(2, _translate("MainWindow", "Female"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "Day of birth"))
        self.label_6.setText(_translate("MainWindow", "Gender"))
        self.btn_update_info.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "Your playlists:"))
        self.btn_create_playlist.setText(_translate("MainWindow", "Create"))
        self.for_you.setText(_translate("MainWindow", "For you:"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.lbl_curr_name.setText(_translate("MainWindow", "Song name"))
        self.lbl_curr_artist.setText(_translate("MainWindow", "Artist"))
        self.lbl_curr_img.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_time.setText(_translate("MainWindow", "TextLabel"))
        self.username_label_2.setText(_translate("MainWindow", "Popular"))
        self.username_label_3.setText(_translate("MainWindow", "Trending"))
