import requests

class MoviesWsDAL():
    def __init__(self):
       self._url = "https://api.tvmaze.com/shows"

    def get_all_movies(self):
        resp = requests.get(self._url)
        return resp.json()

