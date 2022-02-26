from ast import Str
from shutil import move
import typing
from xxlimited import foo
from Sex import Sex


class Animal():
    __cell_speed: int
    __animal_id: int
    __animal_cannot_move: bool
    __food_points: int
    __animal_sex: Sex
    __max_food_points: int
    __life_points: int
    __animal_type: Str

    def __init__(self, animal_type : str, sex : Sex,
                 animal_id: int = -1, animal_cannot_move : bool = False) -> None:


        self.__animal_type = animal_type
        self.__animal_id = animal_id
        self.__animal_cannot_move = animal_cannot_move
        self.__animal_sex = sex
        if animal_type == 'R-':
            self.__food_points=4
            self.__life_points=4
            self.__cell_speed=3
            self.__max_food_points=3
        elif animal_type == 'Z-':
            self.__food_points = 4
            self.__life_points = 4
            self.__cell_speed = 2
            self.__max_food_points = 4
        elif animal_type == 'L-':
            self.__food_points = 5
            self.__life_points = 4
            self.__cell_speed = 3
            self.__max_food_points = 5
        elif animal_type == 'T-':
            self.__food_points = 4
            self.__life_points = 4
            self.__cell_speed = 2
            self.__max_food_points=4
        else:
            print(self.__animal_type,'!')
            raise f"Uncorrect animal type - {self.__animal_type}"

    def get_cell_speed(self) -> int:
        return self.__cell_speed

    def get_animal_id(self) -> int:
        return self.__animal_id

    def set_animal_id(self, animal_id: int) -> None:
        self.__animal_id = animal_id

    def get_cannot_animal_move(self) -> bool:
        return self.__animal_cannot_move

    def set_cannot_animal_move(self, moving: bool) -> None:
        self.__animal_cannot_move = moving

    def get_animal_sex(self) -> int:
        return self.__animal_sex

    def get_food_points(self) -> int:
        return self.__food_points

    def get_life_points(self) -> int:
        return self.__life_points

    def set_food_points(self, food_points: int) -> None:
        self.__food_points = food_points

    def get_max_food_points(self) -> int:
        return self.__max_food_points

    def get_animal_type(self) -> str:
        return self.__animal_type

    def next_step(self) -> bool:
        if self.__food_points in [0, 1] or self.__life_points in [0, 1]:
            return False
        self.__food_points -= 1
        self.__life_points -= 1
        return True
    
    def info(self) -> str:
        result_string = self.__animal_type +\
            f"{str(self.__animal_id)}("
        result_string = result_string + 'fem,' if self.__animal_sex == Sex.FEMALE else\
                                                result_string + 'mal,'
        result_string += str(self.__food_points) + ',' +\
                                                str(self.__life_points) + ')'
        return result_string

    def move_choise(self) -> str:
        move_choise = ''
        if self.__animal_cannot_move:
            move_choise = 'Cannot move'
        elif self.__life_points == 1:
            move_choise = 'Will die'
        elif self.__food_points == 2:
            move_choise = 'Find eat'
        elif self.__food_points >= 3:
            move_choise = 'Find partner'
        return move_choise