#!/bin/python
"""
entertainment_center.py uses movies_list.py and
fresh_tomatoes.py to create a web page with information about
class Movie instances defined in <moviesfile>, a JSON file. It then opens
a browser window with the generated html file.
"""

# import the media library from media.py, fresh_tomatoes.py and movies_list
import fresh_tomatoes
import movies_list


def main():
    """The main function calls all other funtions of the website.

    """
    # Read the movies.json file to define all movies
    moviesfile = "movies.json"
    movies = movies_list.populate_movies(moviesfile)
    # Call fresh_tomatoes with all movie instance pointers in list movies
    fresh_tomatoes.open_movies_page(movies)


main()
