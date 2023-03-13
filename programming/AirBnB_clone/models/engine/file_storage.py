#!/usr/bin/env python3
import sys
sys.path.append('C:/Users/kshed/OneDrive/Desktop/programming/AirBnB_clone')
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity

class FileStorage():
    """cla

    Returns:
        _type_: _description_
    """
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self) -> None:
        pass
    
    def all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__objects
    
    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        ocname = obj.__class__.__name__
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

        
    def save(self):
        """_summary_
        """
        odict = self.__objects
        objdict = {obj:odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(objdict,file)
            
            
    def reload(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return        
        
        

