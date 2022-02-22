from tokenize import String
from Animal import Animal
from Sex import Sex
from Herbivore import Herbivore

class Zebra(Herbivore): #herbivore inheritance
    def __init__(self, sex : Sex, id_number : int = -1, animal_cannot_move : bool = False) -> None:
        super().__init__(
            food_points=4, life_points=4, cell_speed=2,
            animal_id=id_number, animal_cannot_move=animal_cannot_move,
            sex=sex, max_food_points=4
        )

    def info(self) -> String:
        result_string = 'Z-' + str(self._Animal__animal_id) + '('
        result_string = result_string + 'fem,' if self._Animal__animal_sex == Sex.FEMALE \
            else result_string + 'mal,'
        result_string += str(self._Animal__food_points) + ',' +\
                     str(self._Animal__life_points) + ')' 
        return result_string

    @staticmethod
    def get_class_name() -> String:
        return 'Z-'
        