#!/usr/bin/python3
"""
This module contains the FileStorage class, which handles the serialization
and deserialization of all your data, to and from a JSON file.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place

class FileStorage:
    """FileStorage class for handling storage of instances"""
    __file_path = "file.json"
    __objects = {}
    __class_map = {'BaseModel': BaseModel, 'User': User, 'State': State,
                    'City': City, 'Place': Place}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in
                       FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o.pop("__class__", None)
                    if cls_name in FileStorage.__class_map:
                        class_ = FileStorage.__class_map[cls_name]
                        self.new(class_(o))

        except FileNotFoundError:
            print("File not found.")
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON.")

