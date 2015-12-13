#!/bin/python
"""
Loads movie list from json file and returns movie objects

Example:
filename = "movies.json"
movies = populate_movies(filename)
"""

import json
import media


def read_json(filename):
    """Reads json file and returns contents in a string.

    """
    return json.loads((open(filename, 'r')).read())


def create_movie(movie):
    """Populates a video object and returns the object.

    """
    thismovie = media.Movie(movie['movie_title'], movie['movie_storyline'],
                            movie['poster_image'], movie['trailer_youtube'])
    return thismovie


def populate_movies(movies_list):
    """Populates a dictionary of video objects and returns the dictionary.

    """
    inputmovies = (read_json(movies_list))['movies']
    outputmovies = []
    for i in range(0, len(inputmovies)):
        outputmovies.append(create_movie(inputmovies[i]))
    return outputmovies
