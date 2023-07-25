import math

_MIN_STARS = 100
_MAX_STARS = 300

def test_main():
    """
    Asks the user to input the rating of the movie and
    also round down the number
    """
    movie_rating = input(f"Enter a rating {_MIN_STARS}-{_MAX_STARS}: ")
    while type(movie_rating) == float or (float(movie_rating) < 0):
        print("Must be a positive whole number.")
        movie_rating = input(f"Enter a rating {_MIN_STARS}-{_MAX_STARS}: ")
    return math.floor(float(movie_rating))

test_main()