from collections import deque
from PyQt4 import QtCore, QtGui
class Queue():
    def __init__(self, view):
        self.PlayQueue = deque(maxlen=35)
        self.PrevSong = deque(maxlen=10)
        self.Model = QtGui.QStringListModel(self.PlayQueue)
        self.view = view
        self.view.setModel(self.Model)
        self.updateModel()
    def addSong(self, song):
        self.PlayQueue.append(song)
        self.updateModel()
    def addPlaylist(self, playlist):
        for song in playlist:
            self.PlayQueue.append(song)
        self.updateModel()
        for item in self.PlayQueue:
            print(item)
    def delSong(self, song='', index=-1):
        try:
            print('deleted')
            if song:
                self.PlayQueue.remove(song)
            elif index > 0:
                song = self.PlayQueue[index]
                self.PlayQueue.remove(song)
            elif index == 0:
                self.PrevSong = self.PlayQueue.popleft()
            else:
                self.PlayQueue.pop()
            self.updateModel()
        except IndexError:
            print('Queue Empty')

    def goNext(self):
        temp = self.getCurr()
        if temp:
            self.PrevSong.append(self.getCurr())
            self.PlayQueue.remove(self.PrevSong[-1])
    def goPrev(self):
        try:
            for x in self.PrevSong:
                print(x)
            print(self.PrevSong)
            self.PlayQueue.insert(0, self.PrevSong[-1])
            self.PrevSong.pop()
        except IndexError:
            print('No Previous')
    def getCurr(self):
        try:
            output=self.PlayQueue[0]
        except IndexError:
            output = ''
        return output
    def clear(self):
        self.updateModel()
    def updateModel(self):
        self.Model = QtGui.QStringListModel(self.PlayQueue)
        self.view.setModel(self.Model)