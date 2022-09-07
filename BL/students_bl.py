
from DAL.students_db_DAL import StudentsDbDAL

class StudentsBl():
    def __init__(self):
        self._students = StudentsDbDAL()

    def get_all_students(self):
        students = self._students.get_all_students()
        return students

    def get_student_by_id(self, id):
        student = self._students.get_student_by_id(id)
        return student
        
    def search_student_by_name(self, first_name, last_name):
        student = self._students.search_student_by_name(first_name, last_name)
        return student

    def create_student(self, student_obj):
        resp = self._students.create_student(student_obj)
        return resp

    def update_student(self, id, student_obj):
        resp = self._students.update_student(id, student_obj)
        return resp

    def delete_student(self, id):
        resp = self._students.delete_student(id)
        return resp