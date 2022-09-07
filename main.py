from flask import Flask
from routers.movies import movies
from routers.persons import persons
from routers.students import students
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, obj) :
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self,obj)

app = Flask(__name__)

app.json_encoder = JSONEncoder

app.register_blueprint(movies, url_prefix='/movies')
app.register_blueprint(persons, url_prefix='/persons')
app.register_blueprint(students, url_prefix='/students')

app.run()