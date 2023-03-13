import sys
sys.path.append('C:/Users/kshed/OneDrive/Desktop/programming/AirBnB_clone/models')
from base_model import BaseModel

class Review(BaseModel):
    
    place_id = "" #Place.id
    user_id = "" #User.id
    text = ""