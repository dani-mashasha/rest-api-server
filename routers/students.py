from flask import Blueprint, jsonify, request
from BL.students_bl import StudentsBl

students = Blueprint("students", __name__)

students_bl = StudentsBl()

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
    res = students_bl.create_student(student)
    return jsonify(res)

@students.route('/<string:id>', methods=["PUT"])
def update_student(id):
    student = request.json
    res = students_bl.update_student(id,student)
    return jsonify(res)

@students.route('/<string:id>', methods=["DELETE"])
def delete_student(id):
    res = students_bl.delete_student(id)
    return jsonify(res)