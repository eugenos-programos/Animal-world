from Animal import Animal
from Plant import Plant
import unittest

class Cell():
    __column_index : int
    __raw_index : int
    __plant : Plant
    __animals : list[Animal]

    def __init__(self, raw_index : int, column_index : int,
                plant_on_cell : Plant, animals : list[Animal]) -> None:
        if len(animals) > 4 or len(animals) == 4 and Plant:
            raise "check input"
        self.__column_index = column_index
        self.__raw_index = raw_index
        self.__plant = plant_on_cell
        self.__animals = animals
    
    def add_animal_on_cell(self, animal : Animal) -> bool:
        cannot_add = (len(self.__animals) == 3 and self.get_plant_on_cell()) \
                                            or len(self.__animals) == 4
        if not cannot_add:
            self.__animals.append(animal)
        return cannot_add

    def is_animal_with_another_sex(self, animal : Animal) -> Animal:
        animal_type = type(animal)
        for animal in self.__animals:
            if isinstance(animal, animal_type):
                return animal
        return None
    
    def find_herbivore(self) -> Animal:
        for animal in self.__animals:
            if animal.get_animal_class_name() == 'Herbivore':
                return animal
        return None
    
    def get_column_index(self) -> int:
        return self.__column_index

    def get_raw_index(self) -> int:
        return self.__raw_index

    def get_plant_on_cell(self) -> Plant:
        return self.__plant
    
    def delete_animal(self, animal : Animal) -> None:
        if animal not in self.__animals:
            raise f"Animal {animal.info()} does not axist in this cell"
        self.__animals.remove(animal)
        
    def info(self) -> list[str]:
        str_empty_place = "      -       "
        string_describing_cell = []
        if self.get_plant_on_cell():
            string_describing_cell.append(self.__plant.info())
        for animal in self.__animals:
            string_describing_cell.append(animal.info())
        string_describing_cell += [
            str_empty_place for index in range(4 - len(string_describing_cell))
        ]
        return string_describing_cell

    def get_animals_in_cell(self) -> list[Animal]:
        return self.__animals

    def delete_plant_on_cell(self) -> None:
        if not self.__plant:
            raise 'Plant does not exist in this cell'
        self.__plant = None
    
    def next_step(self) -> None:
        if(self.__plant and not self.__plant.next_step()):
            self.delete_plant_on_cell()
        animals_will_die_in_next_step = [
            animal for animal in self.__animals if not animal.next_step() 
        ]
        for animal in animals_will_die_in_next_step:
            self.delete_animal(animal)

    def add_plant_in_cell(self, plant_id=-1) -> None:
        if len(self.__animals) == 4 or self.__plant:
            raise 'There is no place for plant in cell'

    def inhabitant_numb(self) -> int:
        is_plant_on_cell = int(self.__plant is None)
        return is_plant_on_cell + len(self.__animals)


