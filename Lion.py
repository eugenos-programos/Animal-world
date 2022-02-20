from Predator import Predator
from Sex import Sex

class Lion(Predator):
    __max_food_points = 5

    def __init__(self, sex : Sex, id_number=-1, animal_cannot_move=False) -> None:
        super().__init__()
        self.__animal_sex = sex
        self.__animal_id = id_number
        self.__cell_speed = 3
        self.__life_points = 4
        self.__food_points = 5
        self.__animal_cannot_move = animal_cannot_move
    
    def info(self) -> str:
        output = f'L-{self.__animal_id}('
        if self.__animal_sex == Sex.FEMALE:
            output += 'fem,'
        else:
            output += 'mal,'
        output += f'{self.__food_points},{self.__life_points})'
        return output

    def get_class_name(self) -> str:
        return 'L-'
    
    def get_max_food_points(self):
        return self.__max_food_points

