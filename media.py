# In this file, the class Movie is defined.
import webbrowser

class Movie():
    # This class provides a way to store movie related information
    '''
    Movie
           Has the following instance variables:
               title: Type: String. Provides the movie's title.
               storyline: Type: String. Provides the movie's storyline.
               poster_image_url: Type: String. Provides the URL for the movie's poster from Wiki.
               trailer_youtube_url: Type: String. Provides the URL for the movie's YouTube Trailer
       '''

    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube):
        # initialize instance of class Movie with its instance variables: title, poster image and Youtube trailer url.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Instance method that opens new window to show the trailer
        webbrowser.open(self.trailer_youtube_url)