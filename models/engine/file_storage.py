#!/usr/bin/python3
"""
This module contains the FileStorage class, which handles the serialization
and deserialization of all your data, to and from a JSON file.
"""
import json
from models import base_model
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage class for handling storage of instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in
                       FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        class_dict = {"BaseModel": base_model.BaseModel, "User": User,
                      "State": State, "City": City, "Place": Place}
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    if cls_name in class_dict:
                        if issubclass(
                                class_dict[cls_name], base_model.BaseModel):
                            self.new(class_dict[cls_name](**o))
        except FileNotFoundError:
            print("File not found")
        except json.decoder.JSONDecodeError:
            print("File is not valid JSON")
