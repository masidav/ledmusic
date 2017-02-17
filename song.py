import PyLyrics
from collections import Counter
from difflib import SequenceMatcher
class Song:
    def __init__(self, music_data):
        self.album=music_data[2]
        self.artist=music_data[1]
        self.title=music_data[0]
        self.path=music_data[3]
        self.theme=music_data[8]
        self.length=music_data[4]
        self.genre=music_data[5]
        self.date = music_data[6]
        self.lyric = music_data[7]
        #self.tempo=music_data[9]
    @staticmethod
    def get_lyrics(artist, title, album):
        return 'Beep'
        # lyric = None
        # try:
        #     lyric = PyLyrics.PyLyrics.getLyrics(artist, title)
        # except ValueError:
        #     # try:
        #     #     tracks = PyLyrics.PyLyrics.getAlbums(album)
        #     #     for track in tracks:
        #     #         if Song.similar(track, title) > .75:
        #     #             lyric = track.getLyrics()
        #     pass
        #     except ValueError:
        #         print('Here')
        # if lyric is not None:
        #     return Song.top_words(lyric)
    @staticmethod
    def top_words(lyrics):
        top_3=[]
        count = Counter(lyrics)
        for word in count.most_common(50):
            if len(top_3) == 3:
                return top_3
            if word not in most_common_words:
                top_3.append(word)
    @staticmethod
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

most_common_words = 'the be to of and a in that have I it for not on with he as you do at this but his by from they we say her she or an will my one' +\
'all would there their what so up out if about who get which go me when make can like no just know take person into your good some could them see' +\
'other than then now look only come its over think also back after use two how our first well way evennew want because anythesegive day most us'