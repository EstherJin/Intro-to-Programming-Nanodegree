import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, director):
        """
        Creates space in memory to remember movie information
        self: refers to the object itself
        movie_title: the title of a movie
        movie_storyline: the storyline of a movie
        poster_image: the poster image of a movie
        trailer_youtube: the trailer of the movie
        director: the director of a movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director

    def show_trailer(self):
    """
    Executes code to open a web browser showing a movie trailer
    """
        webbrowser.open(self.trailer_youtube_url)
