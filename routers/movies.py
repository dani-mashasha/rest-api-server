import json
from flask import jsonify, Blueprint
from BL.movie_bl import MovieBl

movies = Blueprint('movies',__name__)

movie_bl = MovieBl()

#Get ALL movies
@movies.route("/", methods=['GET'])
def get_all_movies():
    movies_data = movie_bl.get_movies()
    return jsonify(movies_data)