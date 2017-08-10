import fresh_tomatoes
import media

# below is a list of movies available
# movie instances with detailed information are created by meida.Movie()
toy_story = media.Movie(
	"Toy Story",
    "A story of a boy and his toy come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )


avatar = media.Movie(
    "Avatar",
    "A marine on an alien plant",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=-9ceBgWV8io"
    )


school_of_rock = media.Movie(
    "School of Rock",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=3PsUJFEBC74"
    )

ratatouille = media.Movie(
    "Ratatouille",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
    )

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=FAfR8omt-CY"
    )

hunger_games = media.Movie(
    "Hunger Games",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=4S9a5V9ODuY"
    )

# create an array set for these movies above that will pass to the media file
movies = [
    toy_story,
    avatar,
    school_of_rock,
    ratatouille,
    midnight_in_paris,
    hunger_games
    ]

# create and open the html website using fresh_tomatoes.open_movies_page()
fresh_tomatoes.open_movies_page(movies)
