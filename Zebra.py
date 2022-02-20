from tokenize import String
from Animal import Animal
from Sex import Sex
from Herbivore import Herbivore

class Zebra(Herbivore): #herbivore inheritance
    def __init__(self, sex_ : Sex, id_number = -1, animal_cannot_move = False) -> None:
        super().__init__()
        self.__animal_sex = sex_
        self.__cell_speed = 2
        self.__life_points = 4
        self.__food_points = 4
        self.__animal_cannot_move = animal_cannot_move
        self.__animal_id = id_number
        self.__max_food_points = 4

    def info(self) -> String:
        result_string = 'Z-' + str(self.__animal_id) + '('
        result_string = result_string + 'fem,' if self.__animal_sex == Sex.FEMALE \
            else result_string + 'mal,'
        result_string += str(self.__food_points) + ',' +\
                     str(self.__life_points) + ')' 
        return result_string

    @staticmethod
    def get_class_name() -> String:
        return 'Z-'
    
    def get_max_food_points(self):
        return self.__max_food_points