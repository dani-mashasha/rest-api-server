from DAL.movies_ws_DAL import MoviesWsDAL

class MoviesBl:
    def __init__(self):
        self._movies = MoviesWsDAL()

    def get_movies(self):
        movies = self._movies.get_all_movies()

        return list(map(lambda movie: {"name": movie["name"], "rating": movie["rating"]["average"]} ,movies))

