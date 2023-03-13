#!/usr/bin/env python3
import sys
sys.path.append('C:/Users/kshed/OneDrive/Desktop/programming/AirBnB_clone/models')
from base_model import BaseModel

class User(BaseModel):
    """Represent a user.

    Attribute:
        email(str): the email of the user.
        password (str): the password of the user.
        first_name (str): the first name of user.
        last_name(str) : the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

