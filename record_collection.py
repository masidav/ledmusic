import song as Song
import pickle, os
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
class Catalog():
    def __init__(self):
        self.songs={}
        try:
            with open('records.p', 'rb') as fp:
                self.songs = pickle.load(fp)
        except FileNotFoundError:
            print('no songs yet')
    def add_song(self, song):
        self.songs[song.title]=song
        self.update()
    def check_exist(self, title):
        try:
            temp = self.songs[title]
            if temp:
                return True
        except KeyError:
            print('Song has not been Previously Added')
            return False
    def add_album(self, album_file):
        file_list = []
        for root, dirs, files in os.walk(album_file):
            for file in files:
                if file.endswith(".mp3"):
                    file_list.append(os.path.join(root, file))
        return file_list
    def update(self):
        with open('records.p', 'wb') as fp:
            pickle.dump(self.songs, fp)
    def get_path(self, title):
        try:
            song = self.songs[title]
            return song.path
        except KeyError:
            print('Path Could not be Found. Song is not in Collection')