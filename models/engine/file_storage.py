#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        Or returns a specified dictionary of objects based on
        specified cls"""
        if cls is not None:
            dct = {}
            for key, val in self.__objects.items():
                if type(val) == cls:
                    dct[key] = val
            return dct
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        dct = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, 'w') as f:
            json.dump(dct, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Calls the reload method"""
        self.reload()
