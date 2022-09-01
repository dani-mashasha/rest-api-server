from pymongo import MongoClient
from bson import ObjectId

class StudentBl():
    def __init__(self):
        self._client = MongoClient(port=27017)
        self._db = self._client["studentsDB"]
        self._student_collection = self._db["students"]

    def get_all_students(self):
        students =list(self._student_collection.find({}))
        for stud in students:
            stud["_id"] = str(stud["_id"])
        return students

        
    def get_student_by_id(self, id):
        student = self._student_collection.find_one({"_id": ObjectId(id)})
        student["_id"] = str(student["_id"])
        return student
        
    def search_student_by_name(self, first_name, last_name):
        if first_name:
            student = self._student_collection.find_one({"firstName": first_name})
        elif last_name:
            student = self._student_collection.find_one({"lastName": last_name})
        if student:
            student["_id"] = str(student["_id"])
        return student

    def create_student(self, student_obj):
        self._student_collection.insert_one(student_obj)

    def update_student(self, id, student_obj):
        self._student_collection.find_one_and_update({"_id": ObjectId(id)} , {"$set": student_obj})

    def delete_student(self, id):
        self._student_collection.delete_one({"_id": ObjectId(id) })