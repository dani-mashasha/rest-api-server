from flask import Blueprint, jsonify, request
from BL.student_bl import StudentBl

students = Blueprint("students", __name__)

students_bl = StudentBl()

@students.route('/', methods=["GET"])
def get_all_students():
    students = students_bl.get_all_students()
    return jsonify(students)

@students.route('/<string:id>', methods=["GET"])
def get_student_by_id(id):
    student = students_bl.get_student_by_id(id)
    return jsonify(student)

@students.route('/search', methods=["GET"])
def search_student_by_name():
    first_name = request.args.get('firstName')
    last_name = request.args.get('lastName')
    student = students_bl.search_student_by_name(first_name, last_name)
    if not student:
        return jsonify("No student by this name...")
    return jsonify(student)

@students.route('/', methods=["POST"])
def create_student():
    student = request.json
    students_bl.create_student(student)
    return jsonify("Created !")

@students.route('/<string:id>', methods=["PUT"])
def update_student(id):
    student = request.json
    students_bl.update_student(id,student)
    return jsonify("Updated !")

@students.route('/<string:id>', methods=["DELETE"])
def delete_student(id):
    students_bl.delete_student(id)
    return jsonify("Deleted !")