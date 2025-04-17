from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import *
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
        self.setIcon(QMessageBox.Icon.Information)
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
            database.create_user(email, name, password)
            msg = Alert()
            msg.success_message('Registration successfully')
            self.show_login()
            
    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        

class SongItemWidget(QWidget):
    play_song = pyqtSignal(str)
    add_song_to_playlist = pyqtSignal(str)

    def __init__(self, song_id, song_name, image_path, artist_names):
        super().__init__()
        uic.loadUi("ui/song_item.ui", self)
        
        # Store song data
        self.song_id = song_id
        self.song_name = song_name
        self.image_path = image_path
        self.artist_names = artist_names
        
        # Find UI elements
        self.name = self.findChild(QLabel, "lbl_name")
        self.artist = self.findChild(QLabel, "lbl_artist")
        self.image = self.findChild(QLabel, "lbl_image")
        self.btn_play = self.findChild(QPushButton, "btn_play")
        self.btn_add = self.findChild(QPushButton, "btn_add")
        
        # Set initial values
        self.name.setText(self.song_name)
        self.artist.setText(self.artist_names)
        self.image.setPixmap(QPixmap(self.image_path))
        
        # Connect signals
        self.btn_play.clicked.connect(self.play)
        self.btn_add.clicked.connect(self.add)
        
        # Set minimum size
        self.setMinimumSize(400, 80)
    
    def play(self):
        self.play_song.emit(str(self.song_id))

    def add(self):
        self.add_song_to_playlist.emit(str(self.song_id))
    
    def set_add_button_text(self, text):
        self.btn_add.setText(text)
    
    def set_remove_mode(self, is_remove):
        if is_remove:
            self.btn_add.setProperty("class", "remove")
            self.btn_add.setText("Remove")
        else:
            self.btn_add.setProperty("class", "")
            self.btn_add.setText("Add")
        self.btn_add.style().unpolish(self.btn_add)
        self.btn_add.style().polish(self.btn_add)

class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/mainmenu.ui', self)
        self.user_id = user_id
        
        # Initialize media player
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Connect player signals
        self.player.errorOccurred.connect(self.handle_player_error)
        self.player.playbackStateChanged.connect(self.mediaStateChanged)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        
        # Initialize UI elements
        self.playBtn = self.findChild(QPushButton, "btn_play")
        self.volumeBtn = self.findChild(QPushButton, "btn_volume")
        self.volumeBar = self.findChild(QSlider, "slider_volume")
        self.durationBar = self.findChild(QSlider, "slider_duration")
        self.timeLabel = self.findChild(QLabel, "lbl_time")
        self.curr_name = self.findChild(QLabel, "lbl_curr_name")
        self.curr_img = self.findChild(QLabel, "lbl_curr_img")
        self.curr_artist = self.findChild(QLabel, "lbl_curr_artist")
        
        # Initialize icons
        try:
            self.playIcon = QIcon("img/play-solid.svg")
            self.pauseIcon = QIcon("img/pause-solid.svg")
            self.volumeHighIcon = QIcon("img/volume-high-solid.svg")
            self.volumeLowIcon = QIcon("img/volume-low-solid.svg")
            self.volumeOffIcon = QIcon("img/volume-off-solid.svg")
            self.muteIcon = QIcon("img/volume-xmark-solid.svg")
        except:
            self.playIcon = None
            self.pauseIcon = None
            self.volumeHighIcon = None
            self.volumeLowIcon = None
            self.volumeOffIcon = None
            self.muteIcon = None
        
        # Set initial volume
        self.playBtn.setIcon(self.playIcon)
        self.playBtn.clicked.connect(self.togglePlay)
        self.volumeBtn.setIcon(self.volumeOffIcon)
        self.volumeBtn.clicked.connect(self.toggleMute)

        self.volumeBar.valueChanged.connect(self.setVolume)
        self.durationBar.sliderMoved.connect(self.setPosition)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.playbackStateChanged.connect(self.mediaStateChanged)
        self.volumeBar.setValue(50)
        self.durationBar.setValue(0)
        self.audio_output.setVolume(0.5)
        self.current_volume = 50
        
        # Setup UI elements
        self.setup_ui()
        
        # Load initial data
        self.load_initial_songs()
        self.load_playlists()
    
    def setup_ui(self):
        # Find navigation buttons
        self.btn_playlist = self.findChild(QPushButton, 'playlist_btn')
        self.btn_user = self.findChild(QPushButton, 'user_btn')
        self.btn_song_list = self.findChild(QPushButton, 'btn_song_list')
        self.stackedWidget = self.findChild(QStackedWidget, 'stackedWidget')
        
        # Setup song container with scroll area
        self.btn_search = self.findChild(QPushButton, 'btn_search')
        self.txt_search = self.findChild(QLineEdit, 'txt_search')
        self.song_container = self.findChild(QWidget, 'song_container')
        
        # Setup scroll area
        self.scroll_area = QScrollArea(self.song_container)
        self.scroll_area.setWidgetResizable(True)
        
        # Create scroll content
        self.scroll_content = QWidget()
        self.song_layout = QGridLayout(self.scroll_content)
        self.song_layout.setSpacing(20)
        self.song_layout.setContentsMargins(20, 20, 20, 20)
        
        # Setup scroll area layout
        self.scroll_area.setWidget(self.scroll_content)
        scroll_layout = QVBoxLayout(self.song_container)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.addWidget(self.scroll_area)
        
        # Setup playlist container
        self.playlist_container = self.findChild(QWidget, 'playlist_container')
        self.playlist_layout = QGridLayout(self.playlist_container)
        
        # Add playlist detail page
        self.btn_create_playlist = self.findChild(QPushButton, 'btn_create_playlist')
        self.playlist_detail_page = QWidget()
        self.stackedWidget.addWidget(self.playlist_detail_page)
        self.playlist_detail_layout = QVBoxLayout(self.playlist_detail_page)
        
        # Create playlist detail header
        self.playlist_detail_header = QWidget()
        header_layout = QHBoxLayout(self.playlist_detail_header)
        
        self.playlist_name_label = QLabel("Playlist Name")
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(lambda: self.navigate(1))
        
        header_layout.addWidget(self.playlist_name_label)
        header_layout.addStretch()
        header_layout.addWidget(self.back_button)
        
        # Setup playlist songs scroll area
        self.playlist_songs_scroll = QScrollArea()
        self.playlist_songs_scroll.setWidgetResizable(True)
        
        self.playlist_songs_container = QWidget()
        self.playlist_songs_layout = QGridLayout(self.playlist_songs_container)
        self.playlist_songs_layout.setSpacing(20)
        self.playlist_songs_layout.setContentsMargins(20, 20, 20, 20)
        
        self.playlist_songs_scroll.setWidget(self.playlist_songs_container)
        
        # Add widgets to playlist detail page
        self.playlist_detail_layout.addWidget(self.playlist_detail_header)
        self.playlist_detail_layout.addWidget(self.playlist_songs_scroll)
        
        # Connect signals
        self.btn_playlist.clicked.connect(lambda: self.navigate(1))
        self.btn_user.clicked.connect(lambda: self.navigate(0))
        self.btn_song_list.clicked.connect(lambda: self.navigate(2))
        self.btn_search.clicked.connect(self.search_song)
    
    def load_initial_songs(self):
        # Clear existing widgets
        for i in reversed(range(self.song_layout.count())):
            self.song_layout.itemAt(i).widget().setParent(None)
            
        # Get first 15 songs
        songs = database.get_first_15_songs()
        
        # Add songs to the layout in 2 columns
        row = 0
        col = 0
        for song in songs:
            item = SongItemWidget(song['id'], song['name'], song['image_path'], song['artist_names'])
            item.setFixedSize(400, 80)  # Set fixed size for each item
            item.play_song.connect(self.play_song)
            item.add_song_to_playlist.connect(self.add_song_to_playlist)
            self.song_layout.addWidget(item, row, col)
            col += 1
            if col == 2:  # Show 2 columns
                col = 0
                row += 1

    def load_playlists(self):
        # Clear existing widgets
        for i in reversed(range(self.playlist_layout.count())):
            self.playlist_layout.itemAt(i).widget().setParent(None)
            
        playlists = database.get_playlist_by_user_id(self.user_id)
        row = 0
        col = 0
        for playlist in playlists:
            item = PlaylistItemWidget(playlist['id'], playlist['name'], playlist['image_path'])
            item.view_playlist.connect(self.view_playlist)
            self.playlist_layout.addWidget(item, row, col)
            col += 1
            if col == 3:
                col = 0
                row += 1
                
    def view_playlist(self, playlist_id):
        # Clear existing widgets
        for i in reversed(range(self.playlist_songs_layout.count())):
            self.playlist_songs_layout.itemAt(i).widget().setParent(None)
        
        # Get playlist details
        playlists = database.get_playlist_by_user_id(self.user_id)
        current_playlist = next((p for p in playlists if p['id'] == playlist_id), None)
        
        if current_playlist:
            self.playlist_name_label.setText(current_playlist['name'])
            
            # Add songs to the layout
            row = 0
            col = 0
            for song in playlists:
                if song['id'] == playlist_id:
                    item = SongItemWidget(song['song_id'], song['song_name'], song['image_path'], song['artist_names'])
                    item.setFixedSize(400, 80)
                    item.play_song.connect(self.play_song)
                    item.add_song_to_playlist.connect(lambda sid: self.remove_song_from_playlist(playlist_id, sid))
                    item.set_remove_mode(True)
                    self.playlist_songs_layout.addWidget(item, row, col)
                    col += 1
                    if col == 2:  # Show 2 columns
                        col = 0
                        row += 1
            
            # Navigate to playlist detail page
            self.stackedWidget.setCurrentIndex(3)
            
    def remove_song_from_playlist(self, playlist_id, song_id):
        database.delete_song_from_playlist(playlist_id)
        self.view_playlist(playlist_id)  # Refresh the view
        
    def play_song(self, song_id):
        self.current_song = song_id
        song = database.get_song_by_id(song_id)
        file_path = QUrl.fromLocalFile(song["file_path"])
        self.player.setSource(file_path)
        self.player.play()
        
        if self.playBtn and self.pauseIcon:
            self.playBtn.setIcon(self.pauseIcon)
        elif self.playBtn:
            self.playBtn.setText("Pause")
        
        self.curr_name.setText(f"Now playing: {song['name']}")
        self.curr_img.setPixmap(QPixmap(song["image_path"]))
        self.curr_artist.setText(f"Artist: {song['artist_names']}")
    
    def navigate(self, index):
        self.stackedWidget.setCurrentIndex(index)
        
    def render_song_list(self, song_list:list):
        # clear the grid layout
        for i in reversed(range(self.song_layout.count())):
            widgetToRemove = self.song_layout.itemAt(i).widget()
            self.song_layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
            
        row = 0
        column = 0
        for song in song_list:
            itemWidget = SongItemWidget(song["id"], song["name"], song["image_path"], song["artist_names"])
            itemWidget.setFixedSize(400, 80)  # Set fixed size for each item
            itemWidget.play_song.connect(self.play_song)
            itemWidget.add_song_to_playlist.connect(self.add_song_to_playlist)
            self.song_layout.addWidget(itemWidget, row, column)
            column += 1
            if column == 2:  # Show 2 columns
                column = 0
                row += 1

    def get_and_render_playlist(self, user_id):
        # clear the grid layout
        for i in reversed(range(self.playlist_layout.count())):
            widgetToRemove = self.playlist_layout.itemAt(i).widget()
            self.playlist_layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        playlist = database.get_playlist_by_user_id(user_id)
        self.play_list = playlist
        row = 0
        column = 0
        for song in playlist:
            itemWidget = PlaylistItemWidget(song["song_id"], song["song_name"], song["image_path"])
            itemWidget.play_song.connect(self.play_song)
            itemWidget.delete_song_from_playlist.connect(self.delete_song_from_playlist)
            self.playlist_layout.addWidget(itemWidget, row, column)
            column += 1
            if column == 3:
                row += 1
                column = 0
                
    def search_song(self):
        name = self.txt_search.text()
        song_list = database.get_songs_by_name(name)
        self.render_song_list(song_list)

    @pyqtSlot(str)
    def add_song_to_playlist(self, song_id):
        dialog = PlaylistSelectionDialog(self.user_id, song_id, self)
        dialog.exec()
        self.get_and_render_playlist(self.user_id)
        
    def delete_song_from_playlist(self, song_id):
        database.delete_song_from_playlist(self.user_id, song_id)
        self.get_and_render_playlist(self.user_id)
        
    def handle_player_error(self, error, error_string):
        print(f"Media player error: {error} - {error_string}")
        
    def mediaStateChanged(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.playBtn.setIcon(self.pauseIcon)
        else:
            self.playBtn.setIcon(self.playIcon)

    def positionChanged(self, position):
        self.durationBar.setValue(position)
        # Convert position and duration from milliseconds to hh:mm:ss format
        current_time = self.formatTime(position)
        total_time = self.formatTime(self.player.duration())
        self.timeLabel.setText(f"{current_time}/{total_time}")
        
    def durationChanged(self, duration):
        self.durationBar.setRange(0, duration)
    
    def handleError(self):
        self.playBtn.setEnabled(False)
        error_message = self.player.errorString()
        self.playBtn.setText(f"Error: {error_message}")
        print(f"Media Player Error: {error_message}")
        
    def play(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()
    
    def setPosition(self, position):
        if self.player.duration() > 0:  # Only set position if media is loaded
            self.player.setPosition(position)
        
    def setVolume(self, volume):
        # Convert the slider value to a float between 0.0 and 1.0
        volume = volume / 100.0
        self.audio_output.setVolume(volume)
        if volume == 0.0:
            self.volumeBtn.setIcon(self.volumeOffIcon)
        elif volume < 0.5:
            self.audio_output.setMuted(False)
            self.volumeBtn.setIcon(self.volumeLowIcon)
        else:
            self.volumeBtn.setIcon(self.volumeHighIcon)
            self.audio_output.setMuted(False)
    
    def toggleMute(self):
        if self.audio_output.isMuted():
            self.audio_output.setMuted(False)
            if self.current_volume >= 50:
                self.volumeBtn.setIcon(self.volumeHighIcon)
            elif self.current_volume < 50:
                self.volumeBtn.setIcon(self.volumeLowIcon)
            else:
                self.volumeBtn.setIcon(self.volumeOffIcon)
            self.volumeBar.setValue(self.current_volume)
        else:
            self.audio_output.setMuted(True)
            self.volumeBtn.setIcon(self.muteIcon)
            self.current_volume = self.volumeBar.value()
            self.volumeBar.setValue(0)
    
    def togglePlay(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.playBtn.setIcon(self.playIcon)
        else:
            self.player.play()
            self.playBtn.setIcon(self.pauseIcon)

    def formatTime(self, milliseconds):
        total_seconds = milliseconds // 1000
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
        
class PlaylistItemWidget(QWidget):
    view_playlist = pyqtSignal(str)
    
    def __init__(self, playlist_id, playlist_name, image_path):
        super().__init__()
        uic.loadUi("ui/playlist_item.ui", self)
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name
        self.image_path = image_path
        
        self.name = self.findChild(QLabel, "lbl_name")
        self.image = self.findChild(QLabel, "lbl_image")
        self.btn_view = self.findChild(QPushButton, "btn_view")
        
        self.name.setText(self.playlist_name)
        self.image.setPixmap(QPixmap(self.image_path))
        
        self.btn_view.clicked.connect(self.view)
        
    def view(self):
        self.view_playlist.emit(self.playlist_id)

class PlaylistDetailWindow(QMainWindow):
    def __init__(self, playlist_id, user_id):
        super().__init__()
        uic.loadUi('ui/playlist_detail.ui', self)
        self.playlist_id = playlist_id
        self.user_id = user_id
        
        self.songs_container = self.findChild(QWidget, 'songs_container')
        self.songs_layout = QGridLayout(self.songs_container)
        
        self.load_playlist_songs()
        
    def load_playlist_songs(self):
        # Clear existing widgets
        for i in reversed(range(self.songs_layout.count())):
            self.songs_layout.itemAt(i).widget().setParent(None)
            
        songs = database.get_playlist_by_user_id(self.user_id)
        row = 0
        col = 0
        for song in songs:
            if song['id'] == self.playlist_id:
                item = SongItemWidget(song['song_id'], song['song_name'], song['image_path'], song['artist_names'])
                item.setFixedSize(400, 80)  # Set fixed size for each item
                item.play_song.connect(self.play_song)
                item.add_song_to_playlist.connect(self.remove_song)
                self.songs_layout.addWidget(item, row, col)
                col += 1
                if col == 2:  # Show 2 columns
                    col = 0
                    row += 1
                    
    def play_song(self, song_id):
        # Implement song playback
        pass
        
    def remove_song(self, song_id):
        database.delete_song_from_playlist(song_id)
        self.load_playlist_songs()

class PlaylistSelectionDialog(QDialog):
    def __init__(self, user_id, song_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.song_id = song_id
        self.setWindowTitle("Select Playlist")
        self.setMinimumWidth(300)
        
        layout = QVBoxLayout(self)
        
        # Create list widget for playlists
        self.playlist_list = QListWidget()
        self.playlist_list.setStyleSheet("""
            QListWidget {
                background-color: #2A2A2A;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #3A3A3A;
            }
            QListWidget::item:selected {
                background-color: #1DB954;
            }
        """)
        
        # Add playlists to the list
        playlists = database.get_playlist_by_user_id(self.user_id)
        for playlist in playlists:
            item = QListWidgetItem(playlist['name'])
            item.setData(Qt.ItemDataRole.UserRole, playlist['id'])
            self.playlist_list.addItem(item)
            
        layout.addWidget(self.playlist_list)
        
        # Add buttons
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add to Playlist")
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                color: white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
        """)
        self.add_button.clicked.connect(self.add_to_playlist)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #FF4444;
                color: white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #ff6666;
            }
        """)
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
    def add_to_playlist(self):
        selected_items = self.playlist_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select a playlist")
            return
            
        playlist_id = selected_items[0].data(Qt.ItemDataRole.UserRole)
        song = database.get_song_by_id(self.song_id)
        
        # Check if song already exists in playlist
        exist_song = database.get_playlist_by_user_id_and_song_id(self.user_id, self.song_id)
        if exist_song:
            QMessageBox.warning(self, "Warning", "Song already in playlist")
            return
            
        database.add_song_to_playlist(playlist_id, self.song_id, song["name"], song["image_path"])
        QMessageBox.information(self, "Success", "Song added to playlist")
        self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login = Home(2)
    login.show()
    app.exec()