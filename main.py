import math, os, time, pickle, threading
import sys
from playerGUI import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.m4a import M4A
from song import Song
from record_collection import Catalog
from database import Database, theme_dict
from ard_lib import Arduino
from pyQueue import Queue
import vlc
from collections import OrderedDict
import librosa
from mutagen import MutagenError
from PyLyrics import *
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.catalog=Catalog()
        self.Ard_conn=Arduino()
        self.db=Database()
        self.myQueue=Queue(self.ui.quView)
        self.player=None
        DEFAULT_HOME = "C://Users//David//Music"
        self.current_song=''
        self.last_added = ''
        self.query_dialog()
        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath("C://Users//David//Music")
        self.ui.librTree.setModel(self.model)
        self.ui.librTree.setRootIndex((self.model.index("C://Users//David//Music")))
        self.ui.librTree.setColumnHidden(1, True)
        self.ui.librTree.setColumnHidden(2, True)
        self.ui.librTree.setColumnHidden(3, True)
        self.ui.librTree.clicked.connect(self.on_librTree_clicked)
        self.ui.Pause.clicked.connect(lambda: self.porp_music('Pause'))
        self.ui.Play.clicked.connect(lambda: self.porp_music('Play'))
        self.ui.Next_2.clicked.connect(lambda: self.moveBetween('Next'))
        self.ui.Prev.clicked.connect(lambda: self.moveBetween('Prev'))
        self.ui.clearQu.clicked.connect(self.myQueue.PlayQueue.clear)
        self.ui.changeTheme.clicked.connect(self.change_theme)
        self.ui.queryQu.clicked.connect(self.wind.show)
        self.ui.clearQu.clicked.connect(self.myQueue.clear)
    def query_dialog(self):
        self.wind = QtGui.QDialog()
        temp = ['Artist', 'Theme', 'Album', 'Genre']
        layout = QtGui.QVBoxLayout()
        button_box = QtGui.QDialogButtonBox(parent = self.wind)
        ok_button = QtGui.QPushButton('Okay')
        role = QtGui.QDialogButtonBox.AcceptRole
        button_box.addButton(ok_button, role)
        button_box.accepted.connect(self.wind.accept)
        for item in temp:
            check = QtGui.QRadioButton(item, parent = self.wind)
            layout.addWidget(check)
        line_edit = QtGui.QLineEdit()
        layout.addWidget(line_edit)
        layout.addWidget(button_box)
        self.wind.setLayout(layout)
        self.wind.setWindowTitle('Query')
        self.wind.accepted.connect(self.query_songs)
    def query_songs(self):
        for radio in self.wind.findChildren(QtGui.QRadioButton):
            if radio.isChecked():
                choice = radio.text()
        line = self.wind.findChild(QtGui.QLineEdit)
        option = line.text()
        songs = self.db.query(choice, option)
        self.myQueue.addPlaylist(songs)
        self.ui.quView.setModel(self.myQueue.Model)
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_librTree_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)
        if fileName:
            self.grab_music(filePath)
    def moveBetween(self, choice):
        if choice == 'Next':
            self.myQueue.goNext()

            self.update_player()
        if choice == 'Prev':
            print('Prev')
            self.myQueue.goPrev()
            self.update_player()
    def grab_playlist(self, file):
        file_list = self.catalog.add_album(file)
        for file in file_list:
            self.grab_music(file)
    def update_player(self):
        def callback():
            t_gate = True
            while t_gate:
                item = self.myQueue.getCurr()
                if item == self.current_song and self.player is not None:
                    if (self.player.get_length() - self.player.get_time()) < 1000:
                        self.myQueue.goNext()
                        item = self.myQueue.getCurr()
                        print('Song Ended. Next Song')
                if item != self.current_song and item:
                    self.current_song = item
                    temp = self.catalog.songs.get(item)
                    if temp is None:
                        print(item)
                    self.ui.songLabel.setText("Song: %s" % temp.title)
                    self.ui.artistLabel.setText("Artist: %s" % temp.artist)
                    self.ui.albumLabel.setText("Album: %s" % temp.album)
                    self.Ard_conn.send_py(temp.theme)
                    self.ui.genreLabel.setText("Genre: %s" % temp.genre)
                    self.ui.themeLabel.setText("Theme: %s" % temp.theme)
                    self.porp_music("Pause")
                    if self.player is not None:
                        self.player.release()
                    self.player=vlc.MediaPlayer(temp.path)
                    self.player.play()
                    gate = True
                    while gate:
                        if self.player.is_playing():
                            gate = False
                            print('Song is Playing')
        self.t1=threading.Thread(target=callback)
        self.t1.start()
    def get_theme(self, name):
        return self.db.get_T_total(name)
    def porp_music(self, choice):
        if choice == "Pause" and self.player is not None:
            self.player.stop()
        elif self.player is not None:
            self.player.play()
        elif self.player is None and choice == 'Play':
            self.update_player()
    def grab_music(self, music_file):
        if self.last_added != music_file:
            self.last_added = music_file
            try:
                music = ID3(music_file)
                audio = MP3(music_file)
                music_data=music.pprint()
                title = music_data[(music_data.find("TIT2") + 5):music_data.find('\n', music_data.find("TIT2") + 5)]
                if self.catalog.check_exist(title):
                    print('Song is in Collection')
                else:
                    album = music_data[(music_data.find("TALB") + 5):music_data.find('\n', music_data.find("TALB") + 5)]
                    artist = music_data[(music_data.find("TPE1")+5):music_data.find('\n', music_data.find("TPE1")+5)]
                    genre = music_data[(music_data.find("TCON") + 5):music_data.find('\n', music_data.find("TCON") + 5)]
                    year = music_data[(music_data.find("TDOR") + 5):music_data.find('\n', music_data.find("TDOR") + 5)]
                    question = title + ' : Theme?? '
                    theme = input(question)
                    lyric = Song.get_lyrics(artist, title, album)
                    temp=[title, artist, album, music_file, audio.info.length, genre, year, lyric, theme]
                    new_song = Song(temp)
                    self.catalog.add_song(new_song)
                    self.db.add_song(new_song)
                self.myQueue.addSong(title)
                self.ui.quView.setModel(self.myQueue.Model)
            except MutagenError:
                self.grab_playlist(music_file)
    def change_theme(self):
        self.window=QtGui.QDialog(parent=self)
        layout=QtGui.QGridLayout()
        for key in theme_dict.keys():
            check=QtGui.QRadioButton(parent=self.window)
            check.setText(key)
            layout.addWidget(check)
        buttons = QtGui.QDialogButtonBox(parent=self.window)
        acceptButton = QtGui.QPushButton(parent=buttons)
        acceptButton.setText('Accept')
        buttons.addButton(acceptButton, QtGui.QDialogButtonBox.AcceptRole)
        acceptButton.clicked.connect(self.accept_new_theme)
        layout.addWidget(buttons)
        self.window.setLayout(layout)
        self.window.show()
    def accept_new_theme(self):
        self.window.accept()
        for children in self.window.findChildren(QtGui.QRadioButton):
            if children.isChecked():
                self.Ard_conn.send_py(children.text())
                print(children.text()+'was Sent')
if __name__ == "__main__":
    app= QtGui.QApplication(sys.argv)
    newWin = MyForm()
    newWin.show()
    sys.exit(app.exec_())
