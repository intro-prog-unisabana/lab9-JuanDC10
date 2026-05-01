# Write your code here!
class Song: 
    def __init__(self, name, artist, lenght): 
        self.name = name
        self.artist = artist
        self.lenght = lenght 
    def get_length_in_seconds(self):
        seconds = 60
        self.get_length_in_seconds = self.lenght * seconds
        return self.get_length_in_seconds
my_song = my_song = Song("tv off", "Kendrick Lamar", 3.7)
print(my_song.get_length_in_seconds())
