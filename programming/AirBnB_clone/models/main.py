import sys
sys.path.append('C:/Users/kshed/OneDrive/Desktop/programming/AirBnB_clone')

from models.base_model import BaseModel
from engine.file_storage import FileStorage 
from models import storage

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
my_model.new()
# print(my_model)