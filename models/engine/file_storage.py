#!/usr/bin/python3
"""
This module contains the FileStorage class, which handles the serialization
and deserialization of all your data, to and from a JSON file.
"""
import json
from models import base_model

# models/engine/file_storage.py
class FileStorage:
    """FileStorage class for handling storage of instances"""
    __file_path = "file.json"
    __objects = {}


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
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    if cls_name in globals() and issubclass(globals()[cls_name], base_model.BaseModel):
                        self.new(globals()[cls_name](**o))
        except FileNotFoundError:
            return
