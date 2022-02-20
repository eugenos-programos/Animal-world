import typing

class Animal():
    __cell_speed : int
    __animal_id : int
    __animal_cannot_move : bool
    __food_points : int
    __animal_sex : int
    __max_food_points : int
    __life_points : int
    def __init__(self, food_points : int = -1, life_points : int = -1) -> None:
        self.__food_points = food_points
        self.__life_points = life_points

    def get_cell_speed(self) -> int:
        return self.__cell_speed
    
    def get_animal_id(self) -> int:
        return self.__animal_id

    def set_animal_id(self, animal_id : int) -> None:
        self.__animal_id = animal_id

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

