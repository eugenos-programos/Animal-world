from ast import Try
from tracemalloc import start
from Area import Area, create_area_from_database
from sql import *


while(True):
    print("Get start data : True / False :")
    start_data = input()
    if start_data not in ['True', 'False']:
        print("Uncorrect input!")
        continue
    start_data = True if start_data == 'True' else False
    break
try:
    print("Initial area:")
    area = create_area_from_database(start_data=start_data)
    area.display_area()
    area.menu()
except Exception as e:
    print(e)