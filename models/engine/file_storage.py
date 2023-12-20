#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class for handling storage of instances"""
    def __init__(self, filename):
        self.filename = filename
        self.objects = {}

    def save(self, obj):
        """Save an instance to a file"""
        self.objects[obj.id] = obj.to_dict()
        with open(self.filename, 'w') as f:
            json.dump(self.objects, f)

    def reload(self):
        """Load instances from a file"""
        try:
            with open(self.filename, 'r') as f:
                self.objects = json.load(f)
        except FileNotFoundError:
            pass

        for obj_id, obj_dict in self.objects.items():
            self.objects[obj_id] = BaseModel.from_dict(obj_dict)
