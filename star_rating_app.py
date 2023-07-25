import math
"""
Homework 3: Star Rating App
===========================
Course:   CS 5001
Semester: Spring 2023
Student:  Hla Htoo
An application that queries the client for movie titles
and a rating for each movie.
"""

# update
_MIN_STARS = 1
_MAX_STARS = 5
movies = ""


def add_movie():
    """
    Creates a string by combining the movie name and rating
    """
    movie = get_movie()
    r = get_rating()
    list_ele = convert_rating(r) + "  " + movie + "\n"
    return list_ele


def get_movie():
    """
    Asks the user to input the name of the movie
    """
    movie_name = str(input("Enter a movie: "))
    return movie_name


def get_rating():
    """
    Asks the user to input the rating of the movie and
    also round down the number
    """
    movie_rating = input(f"Enter a rating {_MIN_STARS}-{_MAX_STARS}: ")
    print(type(movie_rating))
    while type(movie_rating) == float or (float(movie_rating) < 0):
        print("Must be a positive whole number.")
        movie_rating = input(f"Enter a rating {_MIN_STARS}-{_MAX_STARS}: ")
    return math.floor(float(movie_rating))


def convert_rating(rate):
    """
    converts the rating that the user puts in to stars (*) accordingly
    """
    if rate < _MIN_STARS:
        return "*" * _MIN_STARS
    elif rate > _MAX_STARS:
        return "*" * _MAX_STARS
    else:
        return "*" * rate


def list_movies(movies):
    """
    prints the list of movies and rating that the user added
    """
    print(movies)


def menu():
    """
    Asks the user to input the function that he/she would like to do
    """
    return input("What would you like to do (add, list, exit)? ").lower()


def run(movies: str = '') -> None:
    """
    Runs the star rating application.
    Args:
       The movie string, keeping track
       of all movies added between menu calls.
    """

    command = menu()

    if command == "add":
        movies += add_movie()
    elif command == "list":
        list_movies(movies)
    if command != "exit":
        run(movies)


if __name__ == "__main__":
    run()
