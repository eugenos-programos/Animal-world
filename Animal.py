import typing
from Sex import Sex

class Animal():
    __cell_speed : int
    __animal_id : int
    __animal_cannot_move : bool
    __food_points : int
    __animal_sex : Sex
    __max_food_points : int
    __life_points : int

    def __init__(self, food_points : int, life_points : int,
                cell_speed : int, animal_id : int, sex : Sex,
                max_food_points : int,
                animal_cannot_move : bool
    ) -> None:
        self.__food_points = food_points
        self.__life_points = life_points
        self.__animal_cannot_move = animal_cannot_move
        self.__cell_speed = cell_speed
        self.__animal_id = animal_id
        self.__animal_sex = sex
        self.__max_food_points = max_food_points

    def get_cell_speed(self) -> int:
        return self.__cell_speed
    
    def get_animal_id(self) -> int:
        return self.__animal_id

    def set_animal_id(self, animal_id : int) -> None:
        self.__animal_id = animal_id

    def get_cannot_animal_move(self) -> bool:
        return self.__animal_cannot_move

    def set_cannot_animal_move(self, moving : bool) -> None:
        self.__animal_cannot_move = moving

    def get_animal_sex(self) -> int:
        return self.__animal_sex

    def get_food_points(self) -> int:
        return self.__food_points

    def get_life_points(self) -> int:
        return self.__life_points
    
    def set_food_points(self, food_points : int) -> None:
        self.__food_points = food_points
    
    def get_max_food_points(self) -> int:
        return self.__max_food_points

    def next_step(self) -> bool:
        if self.__food_points in [0, 1] or self.__life_points in [0, 1]:
            return False
        self.__food_points -= 1
        self.__life_points -= 1
        return True

