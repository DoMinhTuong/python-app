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
    remove_song_from_playlist = pyqtSignal(str)

    def __init__(self, song_id, song_name, image_path, artist_names, is_playlist_mode=False):
        super().__init__()
        uic.loadUi("ui/song_item.ui", self)
        
        # Store song data
        self.song_id = song_id
        self.song_name = song_name
        self.image_path = image_path
        self.artist_names = artist_names
        self.is_playlist_mode = is_playlist_mode
        
        # Find UI elements
        self.name = self.findChild(QLabel, "lbl_name")
        self.artist = self.findChild(QLabel, "lbl_artist")
        self.image = self.findChild(QLabel, "lbl_image")
        self.btn_play = self.findChild(QPushButton, "btn_play")
        self.btn_playlist = self.findChild(QPushButton, "btn_add")
        
        # Set initial values
        self.name.setText(self.song_name)
        self.artist.setText(self.artist_names)
        self.image.setPixmap(QPixmap(self.image_path.replace("/", "\\")))
        
        # Connect signals
        self.btn_play.clicked.connect(self.play)
        self.btn_playlist.clicked.connect(self.handle_playlist_action)
        
        # Set button text based on mode
        self.setup_playlist_button()
        
        # Set minimum size
        self.setMinimumSize(400, 80)
    
    def play(self):
        self.play_song.emit(str(self.song_id))

    def handle_playlist_action(self):
        if self.is_playlist_mode:
            self.remove_song_from_playlist.emit(str(self.song_id))
        else:
            self.add_song_to_playlist.emit(str(self.song_id))
    
    def setup_playlist_button(self):
        if self.is_playlist_mode:
            self.btn_playlist.setText("Remove")
            self.btn_playlist.setProperty("class", "remove")
        else:
            self.btn_playlist.setText("Add")
            self.btn_playlist.setProperty("class", "")

class PlaylistWidget(QWidget):
    play_song_signal = pyqtSignal(str)  # Add signal at class level
    
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        # Create scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Create container for songs
        self.songs_container = QWidget()
        self.songs_layout = QGridLayout(self.songs_container)
        self.songs_layout.setSpacing(20)
        self.songs_layout.setContentsMargins(20, 20, 20, 20)
        self.songs_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        # Setup scroll area
        self.scroll_area.setWidget(self.songs_container)
        self.layout.addWidget(self.scroll_area)
        
        # Load initial songs
        self.load_songs()
    
    def load_songs(self):
        # Clear existing widgets
        for i in reversed(range(self.songs_layout.count())):
            self.songs_layout.itemAt(i).widget().setParent(None)
            
        # Get user's playlist songs
        songs = database.get_user_playlist_songs(self.user_id)
        
        # Add songs to the layout in 2 columns
        row = 0
        col = 0
        for song in songs:
            # Create widget in playlist mode (Remove button only)
            item = SongItemWidget(song['id'], song['name'], song['image_path'].replace("/", "\\"), song['artist_names'], is_playlist_mode=True)
            item.setFixedSize(400, 80)  # Set fixed size for each item
            item.play_song.connect(self.on_play_song)  # Connect to intermediate handler
            item.remove_song_from_playlist.connect(self.remove_song)
            self.songs_layout.addWidget(item, row, col)
            col += 1
            if col == 2:  # Show 2 columns
                col = 0
                row += 1
        
        # Add stretch to push items to the top-left
        self.songs_layout.setRowStretch(row + 1, 1)
    
    def on_play_song(self, song_id):
        # Emit signal to parent
        self.play_song_signal.emit(song_id)
    
    def remove_song(self, song_id):
        database.remove_song_from_user_playlist(self.user_id, song_id)
        self.load_songs()  # Refresh the view

class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/mainmenu.ui', self)
        self.user_id = user_id
        self.user = database.find_user_by_id(user_id)
        # Initialize media player
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Initialize playlist and current index
        self.current_playlist = database.get_user_playlist_songs(self.user_id)
        self.current_song_index = -1
        
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
            print("Warning: Could not load some icons")
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
        self.load_user_info()
        
    def load_user_info(self):
        self.btn_avatar = self.findChild(QPushButton,'btn_avatar')
        self.txt_name = self.findChild(QLineEdit,'txt_name')
        self.txt_email = self.findChild(QLineEdit,'txt_email')
        self.d_dob = self.findChild(QDateEdit,'d_dob')
        self.cb_gender = self.findChild(QComboBox,'cb_gender')
        self.btn_update_info = self.findChild(QPushButton,'btn_update_info')
        self.btn_update_info.clicked.connect(self.update_info)


        self.txt_name.setText(self.user["name"])
        self.txt_email.setText(self.user["email"])
        self.txt_email.setReadOnly(True)
        self.d_dob.setDate(QDate.fromString(self.user["dob"], "dd/MM/yyyy"))
        self.cb_gender.setCurrentText(self.user["gender"])
        self.btn_avatar.setIcon(QIcon(self.user["avatar"]))
    
    def update_info(self):
        name = self.txt_name.text()
        dob = self.d_dob.date().toString("dd/MM/yyyy")
        gender = self.cb_gender.currentText()
        database.update_user(self.user_id, name, dob, gender)
        msg = Alert()
        msg.success_message("Update info success")
        self.load_user_info() 
    
    def update_avatar(self):
        file,_ = QFileDialog.getOpenFileName(self,"Select Image","","Image Files(*.png *.jpg *jpeg *.bmp)")
        if file:
            self.user["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            database.update_user_avatar(self.user_id, file)
    
    def setup_ui(self):
        # Find navigation buttons
        self.btn_user = self.findChild(QPushButton, 'user_btn')
        self.btn_song_list = self.findChild(QPushButton, 'btn_song_list')
        self.btn_playlist = self.findChild(QPushButton, 'playlist_btn')
        self.stackedWidget = self.findChild(QStackedWidget, 'stackedWidget')
        
        # Find player control buttons
        self.btn_prev_song = self.findChild(QPushButton, 'btn_prev_song')
        self.btn_next_song = self.findChild(QPushButton, 'btn_next_song')
        
        # Connect player control buttons
        self.btn_prev_song.clicked.connect(self.previous_song)
        self.btn_next_song.clicked.connect(self.next_song)
        
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
        self.playlist_container = self.findChild(QWidget, 'playlist_widget')
        self.playlist_widget = PlaylistWidget(self.user_id)
        self.playlist_widget.play_song_signal.connect(self.play_song)  # Connect playlist signal
        playlist_layout = QVBoxLayout(self.playlist_container)
        playlist_layout.setContentsMargins(0, 0, 0, 0)
        playlist_layout.addWidget(self.playlist_widget)
        
        # Connect signals
        self.btn_user.clicked.connect(lambda: self.navigate(0))  # Account page
        self.btn_playlist.clicked.connect(lambda: self.navigate(1))  # Playlist page
        self.btn_song_list.clicked.connect(lambda: self.navigate(2))  # Song list page
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
            item = SongItemWidget(song['id'], song['name'], song['image_path'].replace("/", "\\"), song['artist_names'], is_playlist_mode=False)
            item.setFixedSize(400, 80)  # Set fixed size for each item
            item.play_song.connect(self.play_song)
            item.add_song_to_playlist.connect(self.add_to_playlist)
            item.remove_song_from_playlist.connect(self.remove_from_playlist)
            self.song_layout.addWidget(item, row, col)
            col += 1
            if col == 2:  # Show 2 columns
                col = 0
                row += 1

    def add_to_playlist(self, song_id):
        try:
            # Check if song is already in playlist
            if database.is_song_in_user_playlist(self.user_id, song_id):
                msg = Alert()
                msg.error_message("This song is already in your playlist")
                return
                
            # Add song to playlist
            database.add_song_to_user_playlist(self.user_id, song_id)
            
            # Update current playlist
            self.current_playlist = database.get_user_playlist_songs(self.user_id)
            
            # Always refresh playlist widget to keep it in sync
            self.playlist_widget.load_songs()
            
            # Show success message
            msg = Alert()
            msg.success_message("Song added to playlist successfully")
            
        except Exception as e:
            print(f"Error adding song to playlist: {e}")
            msg = Alert()
            msg.error_message("Failed to add song to playlist")

    def remove_from_playlist(self, song_id):
        try:
            # Remove song from playlist
            database.remove_song_from_user_playlist(self.user_id, song_id)
            
            # Update current playlist
            self.current_playlist = database.get_user_playlist_songs(self.user_id)
            
            # Always refresh playlist widget to keep it in sync
            self.playlist_widget.load_songs()
            
            # Show success message
            msg = Alert()
            msg.success_message("Song removed from playlist successfully")
            
        except Exception as e:
            print(f"Error removing song from playlist: {e}")
            msg = Alert()
            msg.error_message("Failed to remove song from playlist")

    def update_song_item_state(self, song_id, is_in_playlist):
        # Find and update the song item in the current view
        for i in range(self.song_layout.count()):
            item = self.song_layout.itemAt(i).widget()
            if isinstance(item, SongItemWidget) and str(item.song_id) == str(song_id):
                item.is_playlist_mode = is_in_playlist
                item.setup_playlist_button()
                break

    def play_song(self, song_id):
        # Always refresh the playlist when playing a song
        self.current_playlist = database.get_user_playlist_songs(self.user_id)
        
        # Find the song in the current playlist
        self.current_song_index = -1  # Reset index
        for i, song in enumerate(self.current_playlist):
            if str(song['id']) == str(song_id):
                self.current_song_index = i
                break
        
        self.current_song = song_id
        song = database.get_song_by_id(song_id)
        file_path = QUrl.fromLocalFile(song["file_path"].replace("/", "\\"))
        self.player.setSource(file_path)
        self.player.play()
        
        if self.playBtn and self.pauseIcon:
            self.playBtn.setIcon(self.pauseIcon)
        elif self.playBtn:
            self.playBtn.setText("Pause")
        
        self.curr_name.setText(f"Now playing: {song['name']}")
        self.curr_img.setPixmap(QPixmap(song["image_path"].replace("/", "\\")))
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
            # Create widget in song list mode (Add button only)
            itemWidget = SongItemWidget(song["id"], song["name"], song["image_path"].replace("/", "\\"), song["artist_names"], is_playlist_mode=False)
            itemWidget.setFixedSize(400, 80)  # Set fixed size for each item
            itemWidget.play_song.connect(self.play_song)
            itemWidget.add_song_to_playlist.connect(self.add_to_playlist)
            self.song_layout.addWidget(itemWidget, row, column)
            column += 1
            if column == 2:  # Show 2 columns
                column = 0
                row += 1

    def search_song(self):
        name = self.txt_search.text()
        song_list = database.get_songs_by_name(name)
        self.render_song_list(song_list)
        
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

    def next_song(self):
        if not self.current_playlist:
            msg = Alert()
            msg.error_message("No playlist is currently loaded")
            return
            
        if self.current_song_index < len(self.current_playlist) - 1:
            next_song = self.current_playlist[self.current_song_index + 1]
            self.play_song(next_song['id'])
        else:
            # Loop back to the start of the playlist
            first_song = self.current_playlist[0]
            self.play_song(first_song['id'])

    def previous_song(self):
        if not self.current_playlist:
            msg = Alert()
            msg.error_message("No playlist is currently loaded")
            return
            
        if self.current_song_index > 0:
            prev_song = self.current_playlist[self.current_song_index - 1]
            self.play_song(prev_song['id'])
        else:
            # Go to the last song in the playlist
            last_song = self.current_playlist[-1]
            self.play_song(last_song['id'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()