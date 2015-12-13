# Movie Trailer Website

This code will render a static favorite movie trailers website.

#### Dependencies

Python 2.7, Desktop, Internet Browser

#### Operating Systems

Windows, Linux or Mac OSX

### Getting the code

Download the zip file *movie-trailer-website.zip*.

Extract the file into a directory of choice.

### Running the code

Browse to the directory where you extracted *movie-trailer-website.zip*.

Then, to run the code and display the movie trailer website on Linux (gnome), execute:

```bash
./entertainment_center.py
```

In windows, double click the file *entertainment_center.py*

### The movie class

media.py contains a class (data structure). This class contains attributes about a movie such as:

**Movie Name**
**Story Line**
**Poster Image**
**Youtube Trailer URL**

To instantiate this class in python:
```python
import media

my_movie = media.Movie(movie_title, movie_storyline, poster_image,
            trailer_youtube)

# To print the title of my_movie
print (my_movie.title)
```

### Adding more movies

Movies displayed on the movie trailer website are defined in movies_list.py changes can be made there to add additonal movies to the site.

*Author: Bryan Apperson*

This code was created for the Foundations in Python course on Udacity, a part of the Full Stack Developer Nanodegree.

*Date Created: 08/15/2015*
