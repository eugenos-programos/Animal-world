from Area import Area, create_area_from_database
from sql import *

print("Get start data : True / False :")
start_data = input()
start_data = True if start_data == 'True' else False
print("Initial area:")
area = create_area_from_database(start_data=start_data)
area.display_area()
area.menu()