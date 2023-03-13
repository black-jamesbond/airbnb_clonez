#!/usr/bin/env python3
"""A module that implements the BaseModel class"""
import sys
import uuid
import datetime as dt
import models
sys.path.append('C:/Users/kshed/OneDrive/Desktop/programming/AirBnB_clone/models')

class BaseModel():
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if (kwargs):
            for key, value in kwargs.items():
                tform = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, dt.datetime.strptime(value, tform))
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        cls = self.__class__.__name__
        idx = self.id
        dicts = self.__dict__
        string = "[{}] ({}) {}".format(cls, idx, dicts)
        return (string)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = dt.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["created_at"] = self.created_at.isoformat()

        return rdict
