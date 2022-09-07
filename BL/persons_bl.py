from DAL.persons_file_DAL import PersonsFileDAL

class PersonsBl():
    def __init__(self): 
        self._persons = PersonsFileDAL()

    def get_all_persons(self):
        data = self._persons.read_file()
        return data["persons"]

    def get_person_by_id(self,id):
        data = self._persons.read_file()
        persons = data["persons"]
        persons_arr = list(filter(lambda person: person["id"] == int(id) , persons))
        return persons_arr[0]

    def create_person(self, person_obj):
        data = self._persons.read_file()
        persons = data["persons"]
        persons.append(person_obj)
        obj = { "persons": persons }
        self._persons.write_file(obj)
        return "Created !"

    def update_perosn(self, id, person_obj):
        data = self._persons.read_file()
        persons = data["persons"]
        for i in range(len(persons)):
            if persons[i]["id"] == int(id):
                persons[i] = person_obj
                break

        obj = { "persons": persons }
        self._persons.write_file(obj)
        return "Updated !"

    def delete_perosn(self,id):
        data = self._persons.read_file()
        persons = data["persons"]
        index = 0
        for i in range(len(persons)):
            if persons[i]["id"] == int(id):
                index = i
                break
        persons.pop(index)
        obj = { "persons": persons }
        self._persons.write_file(obj)
        return "Deleted !"



