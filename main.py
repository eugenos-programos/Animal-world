from Area import Area, create_area_from_database
from sql import *

print("Initial area:")
area = create_area_from_database()
area.display_area()
area.menu()