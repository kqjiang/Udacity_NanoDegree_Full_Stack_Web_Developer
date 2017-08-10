import webbrowser


# Movie class contains detail information and the show_trailer operation
class Movie():
    # this is the constructor of the Movie class with inputs and outputs
    def __init__(self, movie_title, storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    # this is a function to open the movie trailer url on youtube by webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
