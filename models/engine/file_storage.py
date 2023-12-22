#!/usr/bin/python3
import json
from models.base_model import BaseModel

# models/engine/file_storage.py
class FileStorage:
    """FileStorage class for handling storage of instances"""
    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def all():
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    @staticmethod
    def new(obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    @staticmethod
    def save():
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    @staticmethod
    def reload():
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for key, value in objs.items():
                FileStorage.__objects[key] = BaseModel.from_dict(value)
        except FileNotFoundError:
            pass
