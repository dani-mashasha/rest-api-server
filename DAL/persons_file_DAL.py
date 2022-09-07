import json
import os
import sys

class PersonsFileDAL():
    def __init__(self):
        self._path = os.path.join(sys.path[0],"data/persons.json")

    def read_file(self):
        with open(self._path) as f:
            data = json.load(f)
            return data
            
    def write_file(self, data):
        with open(self._path, "w") as f:
            json.dump(data, f, indent=4)