import os
from random import choice

folder_path = ".\\audio\\alarms"
DEFAULT_ALARM_PATH = None 

items = os.listdir(folder_path)
if items:
    first_item = choice(items)
    DEFAULT_ALARM_PATH = os.path.join(folder_path, first_item)
