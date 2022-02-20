
from email.policy import strict
from tokenize import String


class Plant():
    def __init__(self, id_number : int = -1, new_plant : bool = False) -> None:
        self.__max_life_points = 4
        self.__new_plant = new_plant
        self.__life_points = self.__max_life_points if not new_plant else self.__max_life_points + 1
        self.__id = id_number

    def set_life_points(self, points : int) -> None:
        self.__life_points = points if points > 0 else 0

    def get_life_points(self) -> int:
        return self.__life_points
    
    def next_step(self) -> bool:
        can_live_in_next_step = self.__life_points == 1 or self.__life_points == 0
        if can_live_in_next_step:
            self.__life_points -= 1
        return can_live_in_next_step 
    
    def info(self) -> String:
        info_string = 'P-' + str(self.__id) + '(' + str(self.__life_points) + ')'
        return info_string
    
    def it_is_new_plant(self, parameter : bool) -> bool:
        return self.__new_plant

    def is_new_plant(self, parameter : bool) -> None:
        self.__new_plant = parameter
    
    def set_plant_id(self, id : int) -> None:
        self.__id = id

    def get_plant_id(self):
        return self.__id