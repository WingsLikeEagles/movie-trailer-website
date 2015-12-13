#!/bin/python
"""
Media.py - contains classes for storing information about media
"""

# We need the webbrowser library
import webbrowser


class Movie(object):
    """The movie class contains attributes about a movie

    Usage example:
    import media
    my_movie = media.Movie(movie_title, movie_storyline, poster_image,
                    trailer_youtube)

    print (my_movie.title)
    """

    # Create a class variable for valid ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]

    # Initializes the class movie based on arguments
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Initializes the movie class.

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Show a trailer for the movie.

        """
        webbrowser.open(self.trailer_youtube_url)

    def print_title(self):
        """Prints the title of the movie.

        """
        print (self.title)
