from asyncio import constants
from random import paretovariate

from numpy import inf
from Animal import Animal
from Predator import Predator
from Sex import Sex

class Tiger(Predator):
    __max_food_points : int = 4 

    def __init__(self, sex : Sex, id_number : int = -1, animal_cannot_move : bool = False) -> None:
        super().__init__()
        self.__animal_sex = sex
        self.__cell_speed = 2
        self.__life_points = 4
        self.__food_points = 4
        self.__animal_id = id_number
        self.__animal_cannot_move = animal_cannot_move

    def info(self) -> str:
        info_string = f'T-{self.__animal_id}('
        info_string = info_string + 'fem,' if self.__animal_sex == Sex.FEMALE \
                                           else info_string + 'mal,'
        info_string += f'{self.__food_points},{self.__life_points})'
        return info_string
    
    def get_class_name(self) -> str:
        return "T-"
    
    def get_max_food_points(self) -> int:
        return self.__max_food_points
