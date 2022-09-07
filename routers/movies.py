from flask import jsonify, Blueprint
from BL.movies_bl import MoviesBl

movies = Blueprint('movies',__name__)

movie_bl = MoviesBl()

@movies.route("/", methods=['GET'])
def get_all_movies():
    movies_data = movie_bl.get_movies()
    return jsonify(movies_data)