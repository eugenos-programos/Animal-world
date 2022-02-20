from Herbivore import Herbivore
from Sex import Sex

class Rabbit(Herbivore):
    __max_food_points : int = 3 
    def __init__(self, sex : Sex, id_number=-1, animal_cannot_move=False) -> None:
        super().__init__(4, 4)
        self.__animal_sex = sex
        self.__animal_id = id_number
        self.__cell_speed = 1
        self.__life_points = 4
        self.__food_points = 4
        self.__animal_cannot_move = animal_cannot_move
    
    def info(self) -> str:
        output = f'R-{self.__animal_id}('
        if self.__animal_sex == Sex.FEMALE:
            output += 'fem,'
        else:
            output += 'mal,'
        output += f'{self.__food_points},{self.__life_points})'
        return output

    def get_class_name(self) -> str:
        return 'R-'
    
    def get_max_food_points(self):
        return self.__max_food_points
