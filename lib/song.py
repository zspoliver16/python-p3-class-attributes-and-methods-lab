class Song: 
    count = 0 #variable to keep track of total number of songs
    genres = [] #variables to stor genres and artists
    artists = []
    genre_count = {} #dictionaries to count the occurences of each genre and artist
    artist_count = {}
#initioalize s song obj with name,artist and genre
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count() #increment the total song count
        self.add_to_genres() #add the genre and artist to the respective lists if they are not already present
        self.add_to_artists()
        Song.add_to_genre_count(self.genre) #increment the genre and artist counts in the class dict
        Song.add_to_artist_count(self.artist)

    @classmethod #method to increment the total song count
    def add_song_to_count(cls):
        cls.count += 1 #increment song count by 1

    def add_to_genres(self): #method to add the genre to the genres list if not already there
        if self.genre not in self.genres:
            self.genres.append(self.genre)

    def add_to_artists(self): #method to do the same for the artist
        if self.artist not in self.artists:
            self.artists.append(self.artist)

    @classmethod #incriment the genre count in dict
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod #increment the artist count in dict
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1

#couple song obj's with their details
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")



