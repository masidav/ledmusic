import sqlite3 as sql
SONG_INDEX=0
ARTIST_INDEX=1
ALBUM_INDEX=2
GENRE_INDEX=3
THEME_INDEX=4
DATE_INDEX=5
TIME_INDEX=6
LYRIC_INDEX=7
create_song = '''CREATE TABLE song_theme(title varchar, artist varchar, album varchar, genre varchar, theme varchar, date varchar, time int,
lyric1 varchar, lyric2 varchar, lyric3 varchar, path varchar)'''
create_artist = '''CREATE TABLE artist_theme (artist varchar, theme varchar)'''
create_genre = '''CREATE TABLE genre_theme (genre varchar, theme varchar)'''
create_album = '''CREATE TABLE album_theme (album varchar, theme varchar)'''
create_date = '''CREATE TABLE date_theme (date varchar, theme varchar)'''
create_time = '''CREATE TABLE time_theme (time int, theme varchar)'''
create_lyric = '''CREATE TABLE lyric_theme (lyric varchar, theme varchar)'''
insert_song = '''INSERT INTO song_theme(title, artist, album, genre, theme) values (?, ?, ?, ?, ?)'''
insert_artist = '''INSERT INTO artist_theme(artist, theme) values (?, ?)'''
insert_album = '''INSERT INTO album_theme(album, theme) values (?, ?)'''
insert_genre = '''INSERT INTO genre_theme(genre, theme) values (?, ?)'''
insert_time = '''INSERT INTO artist_theme(time, theme) values (?, ?)'''
insert_date = '''INSERT INTO date_theme(date, theme) values (?, ?)'''
insert_lyric = '''INSERT INTO lyric_theme(lyric, theme) values (?, ?)'''
find_song='''select * from song_theme where title = ? '''
find_artist='''select * from song_theme where artist = ? '''
find_album='''select * from song_theme where album = ? '''
find_genre='''select * from song_theme where genre = ? '''
find_theme = '''select * from song_theme where theme = ?'''
update_theme_song='''UPDATE song_theme SET theme = ? WHERE title = ?'''
update_artist_theme='''UPDATE artist_theme SET theme = ? WHERE artist = ?'''
update_album_theme='''UPDATE album_theme SET theme = ? WHERE album = ?'''
update_genre_theme='''UPDATE genre_theme SET theme = ? WHERE genre = ?'''
weight=[1, .5, .3, .1]
find_commands=[find_song, find_artist, find_album, find_genre, find_theme]
update_commands=[update_theme_song, update_artist_theme,  update_album_theme, update_genre_theme]
theme_dict={'0':-1,'T':0, 'S':0, 'P':0, 'M':0, 'B':0, 'R':0, 'H':0, 'D':0, 'A':0, 'I':0,'F':0}
class Database():
    def __init__(self):
        self.conn=sql.connect('theme_library.db', timeout=180, check_same_thread=False)
        self.cursor=self.conn.cursor()
        try:
            self.cursor.execute(create_song)
            self.cursor.execute(create_artist)
            self.cursor.execute(create_album)
            self.cursor.execute(create_genre)
        except sql.OperationalError as e:
            print(e)
    def add_song(self, song):
        self.cursor.execute(insert_song, (song.title, song.artist, song.album, song.genre, song.theme))
        self.cursor.execute(insert_artist, (song.artist, song.theme))
        self.cursor.execute(insert_album, (song.album, song.theme))
        self.cursor.execute(insert_genre, (song.genre, song.theme))
        self.conn.commit()
    def get_T_total(self, song):
        self.cursor.execute(find_commands[0], (song.title,))
        info = self.cursor.fetchall()
        info = info[0]
        values=[info[0]]
        if info and info != ():
            print(info)
            if info[4]:
                return info[4]
            else:
                high='0'
                for cmd_idx in range(1, len(find_commands)):
                    self.cursor.execute(find_commands[cmd_idx], [info[cmd_idx]])
                    temp=self.cursor.fetchall()[0][1]
                    values.append(info[cmd_idx])
                    for char in temp:
                        theme_dict[char]=theme_dict[char]+weight[cmd_idx]
                for key in theme_dict.keys():
                    if theme_dict[key]>theme_dict[high]:
                        high=key
                    else:
                        if key>high:
                             high=key
                self.update_themes(high, values)
                return high
        else:
            self.add_song(song)
            return self.get_T_total(song)
    def update_themes(self, theme, values):
        for cmd_idx in range(1, len(update_commands)):
            self.cursor.execute(update_commands[cmd_idx], (theme, values[cmd_idx]))
    def query(self, choice, option):
        if choice == 'Artist':
            use = ARTIST_INDEX
        elif choice == 'Album':
            use = ALBUM_INDEX
        elif choice == 'Genre':
            use = GENRE_INDEX
        elif choice == 'Theme':
            use = THEME_INDEX
        command = find_commands[use]
        self.cursor.execute(command, (option,))
        info = self.cursor.fetchall()
        output = []
        for row in info:
            output.append(row[0])
            print(row[0])
        return output