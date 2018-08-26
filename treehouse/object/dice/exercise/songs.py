from functools import total_ordering

@total_ordering
class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __eq__(self, other):
        return self.length == other

    def __gt__(self, other):
        return self.length > other

    def __int__(self):
        return self.length


s1 = Song("Yang", "SongOne", 5)
s2 = Song("Yang", "SongTwo", 3)
