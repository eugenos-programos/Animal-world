from asyncio import constants
from random import paretovariate

from numpy import inf
from Animal import Animal
from Predator import Predator
from Sex import Sex

class Tiger(Predator):

    def __init__(self, sex : Sex, id_number : int = -1, animal_cannot_move : bool = False) -> None:
        super().__init__(
            food_points=4, life_points=4, cell_speed=2,
            animal_id=id_number, animal_cannot_move=animal_cannot_move,
            sex=sex, max_food_points=4
        )

    def info(self) -> str:
        info_string = f'T-{self._Animal__animal_id}('
        info_string = info_string + 'fem,' if self._Animal__animal_sex == Sex.FEMALE \
                                           else info_string + 'mal,'
        info_string += f'{self._Animal__food_points},{self._Animal__life_points})'
        return info_string
    
    def get_class_name(self) -> str:
        return "T-"
