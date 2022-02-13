from Sex import Sex
from Zebra import Zebra
from Rabbit import Rabbit
from Lion import Lion
from Tiger import Tiger
from Cell import Cell
from Animal import Animal
import os

class Area():
    __length : int
    __width : int
    __last_inhabitant_id : int
    __area : list(list(Cell))
    __inhabitant_log : str

    def __animal_moving() -> None:
        pass

    def __find_eat_for_herbivore(cell_with_herbivore : Cell, animal : Animal) -> None:
        pass
    
    def __find_eat_for_predator(cell_with_predator : Cell, animal : Animal) -> None:
        pass

    def __find_eat(cell_with_animal : Cell, animal : Animal) -> None:
        pass

    def __find_partner(cell_with_animal : Cell, animal : Animal) -> bool:
        pass

    def __get_neighbor_cells(cell : Cell, int scope_level) -> list(Cell):
        pass

    def __move_animal_between_cells(first_cell : Cell, second_cell : Cell, animal : Animal) -> bool:
        pass

    def __propagate_the_plant(cell_with_plant : Cell) -> None:
        pass

    def __propagate_the_animal(cell_with_animals : Cell, first_animal : Animal, second_animal : Animal) -> None:
        pass

    def __check_propagating_in_all_cells(self) -> None:
        pass

    def __check_life_and_food_points_in_all_cells() -> None:
        pass

    def __get_random_neighbor_cell(neighbor_cells : list(Cell)) -> None:
        pass

    def __all_animal_can_propagate(self) -> None:
        pass

    def __eat_plant(self, animal : Animal, cell_with_animal : Cell, cell__with_plant : Cell) -> None:
        pass

    def __eat_herbivore(self, animal : Animal, cell_with_animal : Cell, cell_with_herbivore : Cell, herbivore : Animal) -> None:
        pass

    def get_last_inh_id(self) -> int:
        pass

    def increase_last_inh_id(self) -> None:
        pass

    def __init__(self, area : list(list(Cell)), length : int, width : int) -> None:
        pass

    def transform_area_into_matrix_form(self) -> str:
        pass

    def display_area(self) -> None:
        pass

    def next_step(self) -> None:
        pass

    def get_length(self) -> int:
        return self.__length

    def get_width(self) -> int:
        return self.__width

    @staticmethod
    def generate_animal_sex() -> Sex:
        pass

    @staticmethod
    def fill_cells_from_file(directory : str) -> None:
        if not os.path.exists(directory):
            raise "Invalid directory"
        pass