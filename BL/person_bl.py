import json
import os
import sys

class PersonBl():
    def __init__(self):
        self._path = os.path.join(sys.path[0],"data/persons.json")

    def get_all_persons(self):
        with open(self._path) as f:
            data = json.load(f)
            return data["persons"]

    def get_person_by_id(self,id):
        with open(self._path) as f:
            data = json.load(f)
            persons_arr = list(filter(lambda person: person["id"] == int(id) ,data["persons"]))
            return persons_arr[0]

    def create_person(self, person_obj):
        with open(self._path, "r") as f:
            data = json.load(f)
            data["persons"].append(person_obj)

            with open(self._path, "w") as f:
                json.dump(data,f, indent = 4)

    def update_perosn(self, id, person_obj):
        with open(self._path, "r") as f:
            data = json.load(f)
            for per in data["persons"]:
                if per["id"] == int(id):
                    per["name"] = person_obj["name"]
                    per["phone"] = person_obj["phone"]
            with open(self._path, "w") as f2:
                json.dump(data,f2, indent = 4)

    def delete_perosn(self,id):
        with open(self._path,"r") as f:
            data = json.load(f)
            persons = list(filter(lambda person: person["id"] != int(id) ,data["persons"]))
            updeted_data = {"persons": persons}
            with open(self._path, "w") as f2:
                json.dump(updeted_data, f2, indent=4)

