import requests

class MovieBl:
    def __init__(self):
        self._url = "https://api.tvmaze.com/shows"

    def get_movies(self):
        resp = requests.get(self._url)
        movies = resp.json()

        return list(map(lambda movie: {"name": movie["name"], "rating": movie["rating"]["average"]} ,movies))

