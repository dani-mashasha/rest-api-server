from flask import jsonify,request, Blueprint
from BL.persons_bl import PersonsBl

persons = Blueprint('persons', __name__)

persons_bl = PersonsBl()


@persons.route("/", methods=['GET'])
def get_all_persons():
    persons_data = persons_bl.get_all_persons()
    return jsonify(persons_data)

@persons.route('/<string:id>', methods=["GET"])
def get_person_by_id(id):
    person = persons_bl.get_person_by_id(id)
    return jsonify(person)

@persons.route('/', methods=["POST"])
def create_perosn():
    person_obj = request.json
    persons_bl.create_person(person_obj)
    return jsonify("Created !")

@persons.route('/<string:id>', methods=["PUT"])
def update_perosn(id):
    person_obj = request.json
    persons_bl.update_perosn(id, person_obj)
    return jsonify("Updated !")

@persons.route('/<string:id>', methods=["DELETE"])
def delete_perosn(id):
    persons_bl.delete_perosn(id)
    return jsonify("Deleted !")