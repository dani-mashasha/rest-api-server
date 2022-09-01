from flask import Flask
from routers.movies import movies
from routers.persons import persons
from routers.students import students

app = Flask(__name__)

app.register_blueprint(movies, url_prefix='/movies')
app.register_blueprint(persons, url_prefix='/persons')
app.register_blueprint(students, url_prefix='/students')

app.run()