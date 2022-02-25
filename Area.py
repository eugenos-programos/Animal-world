from typing import List
from black import out
from Sex import Sex
from Zebra import Zebra
from Rabbit import Rabbit
from Lion import Lion
from Tiger import Tiger
from Cell import Cell
from Animal import Animal
from Plant import Plant
from Herbivore import Herbivore
from Predator import Predator
from sql import *
import os
import random
import pandas as pd


class Area():
    __length: int
    __width: int
    __last_inhabitant_id: int
    __area: list[list[Cell]]
    __inhabitant_log: str

    def __animal_moving(self) -> None:
        for cell_raw in self.__area:
            for cell in cell_raw:
                for animal_in_cell in cell.get_animals_in_cell():
                    if animal_in_cell.get_cannot_animal_move(): continue
                    if animal_in_cell.get_life_points() == 1:
                        if not self.__find_partner(cell, animal_in_cell):
                            self.__find_eat(cell, animal_in_cell)
                    if animal_in_cell.get_food_points() == 2:
                        self.__find_eat(cell, animal_in_cell)
                    if animal_in_cell.get_food_points() >= 3:
                        if not self.__find_partner(cell, animal_in_cell):
                            ### move to random cell if animal was not found partner and has max food_points
                            if animal_in_cell.get_food_points() == animal_in_cell.get_max_food_points():
                                random_neighbor_cell = Area.__get_random_neighbor_cell(
                                    self.__get_neighbor_cells(
                                        cell, animal_in_cell.get_cell_speed()))
                                self.__move_animal_between_cells(
                                    cell, random_neighbor_cell, animal_in_cell)
                                animal_in_cell.set_cannot_animal_move(True)
                            ### if not - find food
                            else:
                                self.__find_eat(cell, animal_in_cell)
                    animal_in_cell.set_cannot_animal_move(True)
        self.__all_animal_can_move()

    def __find_eat_for_herbivore(self, cell_with_herbivore: Cell,
                                 animal: Animal) -> None:
        if cell_with_herbivore.get_plant_on_cell():
            self.__eat_plant(animal, cell_with_herbivore, cell_with_herbivore)
            return
        neighbor_cells = self.__get_neighbor_cells(cell_with_herbivore, animal.get_cell_speed()) 
        for neighbor_cell in neighbor_cells:
            if neighbor_cell.get_plant_on_cell():
                animal.set_cannot_animal_move(True)
                self.__eat_plant(animal, cell_with_herbivore, neighbor_cell)
                return
        ### if can not find food animal goes to the rand neighbor cell
        for neighbor_cell in neighbor_cells:
            if self.__move_animal_between_cells(cell_with_herbivore, neighbor_cell, animal):
                animal.set_cannot_animal_move(True)
        return

    def __find_eat_for_predator(self, cell_with_predator: Cell,
                                animal: Animal) -> None:
        if cell_with_predator.find_herbivore():
            self.__eat_herbivore(animal, cell_with_predator,
                                 cell_with_predator,
                                 cell_with_predator.find_herbivore())
            return
        for cell_level in range(1, animal.get_cell_speed() + 1):
            for neighbor_cell in self.__get_neighbor_cells(cell_with_predator):
                if neighbor_cell.find_herbivore():
                    animal.set_cannot_animal_move(True)
                    self.__eat_herbivore(animal, cell_with_predator,
                                         neighbor_cell,
                                         neighbor_cell.find_herbivore())
                    return
        for cell_level in range(animal.get_cell_speed() + 1, 1):
            for neighbor_cell in Area.__get_random_neighbor_cell(
                    cell_with_predator, cell_level):
                if self.__move_animal_between_cells(cell_with_predator,
                                                    neighbor_cell, animal):
                    animal.set_cannot_animal_move(True)
                    return
        return

    def __find_eat(self, cell_with_animal: Cell, animal: Animal) -> None:
        if (animal.get_animal_class_name() == 'Herbivore'):
            self.__find_eat_for_herbivore(cell_with_animal, animal)
        elif (animal.get_animal_class_name() == 'Predator'):
            self.__find_eat_for_predator(cell_with_animal, animal)

    def __find_partner(self, cell_with_animal: Cell, animal: Animal) -> bool:
        neighbor_cells = self.__get_neighbor_cells(cell_with_animal, animal.get_cell_speed()) + [cell_with_animal]
        for neighbor_cell in neighbor_cells:
                if neighbor_cell.is_animal_with_another_sex(animal) and neighbor_cell.inhabitant_numb() <= 2:
                    partner_animal = neighbor_cell.is_animal_with_another_sex(
                        animal)
                    if not neighbor_cell == cell_with_animal:
                        self.__move_animal_between_cells(
                            cell_with_animal, neighbor_cell, animal)
                    self.__propagate_the_animals(neighbor_cell, animal,
                                                 partner_animal)
                    self.__inhabitant_log += f'{animal.get_class_name()}{animal.get_animal_id()}' + \
                                            '+' + f'{partner_animal.get_class_name()}{partner_animal.get_animal_id()}=' +\
                                                 f'{animal.get_class_name()}{self.__last_inhabitant_id}|'
                                                
                    return True
        return False

    def __get_neighbor_cells(self, cell: Cell, scope_level: int) -> list[Cell]:
        if scope_level < 0:
            raise f"Negative scope_level parameter - {scope_level}"
        raw_index = cell.get_row_index()
        column_index = cell.get_column_index()
        result = []
        while scope_level:
            if column_index - scope_level >= 0:
                result.append(self.__area[raw_index][column_index -
                                                     scope_level])
                if raw_index - scope_level >= 0:
                    result.append(self.__area[raw_index -
                                              scope_level][column_index -
                                                           scope_level])
                if raw_index + scope_level < self.__length:
                    result.append(self.__area[raw_index +
                                              scope_level][column_index -
                                                           scope_level])
            if raw_index - scope_level >= 0:
                result.append(self.__area[raw_index -
                                          scope_level][column_index])
            if column_index + scope_level < self.__width:
                result.append(self.__area[raw_index][column_index +
                                                     scope_level])
                if raw_index + scope_level < self.__length:
                    result.append(self.__area[raw_index +
                                              scope_level][column_index +
                                                           scope_level])
                if raw_index - scope_level >= 0:
                    result.append(self.__area[raw_index -
                                              scope_level][column_index +
                                                           scope_level])
            if raw_index + scope_level < self.__length:
                result.append(self.__area[raw_index +
                                          scope_level][column_index])
            scope_level -= 1
        return result

    def __move_animal_between_cells(self, first_cell: Cell, second_cell: Cell,
                                    animal: Animal) -> bool:
        if not second_cell.add_animal_on_cell(animal):
            return False
        self.__inhabitant_log += animal.get_class_name() +\
                            f'{animal.get_animal_id()}->[{second_cell.get_row_index()},' +\
                            f'{second_cell.get_column_index()}] |'
        first_cell.delete_animal(animal)
        return True

    def __propagate_the_plant(self, cell_with_plant: Cell) -> None:
        if not cell_with_plant.get_plant_on_cell(
        ) or cell_with_plant.get_plant_on_cell().it_is_new_plant():
            return
        neighbor_cells = self.__get_neighbor_cells(cell_with_plant, 1)
        random.shuffle(neighbor_cells)
        for neighbor_cell in neighbor_cells:
            if neighbor_cell.get_plant_on_cell() and neighbor_cell.get_plant_on_cell().get_life_points() != \
                neighbor_cell.get_plant_on_cell()._Plant__max_life_points:
                neighbor_cell.get_plant_on_cell().set_life_points(
                    4)  # 4 change on name later
                self.__inhabitant_log += f'P-{cell_with_plant.get_plant_on_cell().get_plant_id()}+->P-' +\
                                        f'{neighbor_cell.get_plant_on_cell().get_plant_id()}|'
            elif neighbor_cell.inhabitant_numb() < 4 and not neighbor_cell.get_plant_on_cell():
                self.__last_inhabitant_id += 1
                neighbor_cell.add_plant_in_cell(self.__last_inhabitant_id)
                self.__inhabitant_log += f"P-{cell_with_plant.get_plant_on_cell().get_plant_id()}*->P-" + \
                                        f"{self.__last_inhabitant_id}|"
                return

    def __propagate_the_animals(self, cell_with_animals: Cell,
                                first_animal: Animal,
                                second_animal: Animal) -> None:

        if (first_animal.get_class_name() == "R-"):
            self.__increase_last_inhabitant_id()
            new_rabbit = Rabbit(self.generate_animal_sex(),
                                self.__last_inhabitant_id, True)
            cell_with_animals.add_animal_on_cell(new_rabbit)

        elif (first_animal.get_class_name() == "Z-"):
            self.__increase_last_inhabitant_id()
            new_zebra = Zebra(self.generate_animal_sex(),
                              self.__last_inhabitant_id, True)
            cell_with_animals.add_animal_on_cell(new_zebra)

        elif (first_animal.get_class_name() == "T-"):
            self.__increase_last_inhabitant_id()
            new_tiger = Tiger(self.generate_animal_sex(),
                              self.__last_inhabitant_id, True)
            cell_with_animals.add_animal_on_cell(new_tiger)

        elif (first_animal.get_class_name() == "L-"):
            self.__increase_last_inhabitant_id()
            new_lion = Lion(self.generate_animal_sex(),
                            self.__last_inhabitant_id, True)
            cell_with_animals.add_animal_on_cell(new_lion)
        first_animal.set_cannot_animal_move(True)
        second_animal.set_cannot_animal_move(True)

    def __check_propagating_in_all_cells(self) -> None:
        for cell_row in self.__area:
            for cell in cell_row:
                self.__propagate_the_plant(cell)
        for cell_row in self.__area:
            for cell in cell_row:
                if cell.get_plant_on_cell():
                    cell.get_plant_on_cell().is_new_plant(False)

    def __check_life_and_food_points_in_all_cells(self) -> None:
        for cell_row in self.__area:
            for cell in cell_row:
                cell.next_step()

    @staticmethod
    def __get_random_neighbor_cell(neighbor_cells: list[Cell]) -> None:
        return neighbor_cells[random.randint(0, len(neighbor_cells) - 1)]

    def __all_animal_can_move(self) -> None:
        for cell_row in self.__area:
            for cell in cell_row:
                for animal in cell.get_animals_in_cell():
                    animal.set_cannot_animal_move(False)

    def __eat_plant(self, animal: Animal, cell_with_animal: Cell,
                    cell_with_plant: Cell) -> None:
        max_fpoints = animal.get_max_food_points()
        fpoints = animal.get_food_points()
        plant_lpoints = cell_with_plant.get_plant_on_cell().get_life_points()
        if max_fpoints - fpoints <= plant_lpoints:
            animal.set_food_points(max_fpoints)
            cell_with_plant.get_plant_on_cell().set_life_points(plant_lpoints -
                                                                max_fpoints +
                                                                fpoints)
            self.__inhabitant_log += animal.get_class_name() +\
                 f'{animal.get_animal_id()} eat P- {cell_with_plant.get_plant_on_cell().get_plant_id()}|'
            return
        else:
            animal.set_food_points(fpoints + plant_lpoints)
            self.__inhabitant_log += animal.get_class_name()  +\
                f'{animal.get_animal_id()} eatten P-{cell_with_plant.get_plant_on_cell().get_plant_id()}|'

    def __eat_herbivore(self, animal: Animal, cell_with_animal: Cell,
                        cell_with_herbivore: Cell, herbivore: Animal) -> None:
        if animal.get_cell_speed() <= herbivore.get_cell_speed(
        ) and random.randint(0, 1) == 1:
            self.__inhabitant_log += animal.get_class_name() +\
                                     f'{animal.get_animal_id()} dsnt catch ' + herbivore.get_class_name() +\
                                         f'{herbivore.get_animal_id()}|'
            self.__move_animal_between_cells(
                cell_with_herbivore,
                Area.__get_random_neighbor_cell(
                    self.__get_neighbor_cells(cell_with_herbivore, 1)),
                herbivore)
            herbivore.set_cannot_animal_move(True)
            return
        max_fpoints = animal.get_max_food_points()
        fpoints = animal.get_food_points()
        hlpoints = herbivore.get_life_points()
        animal.set_food_points(fpoints + hlpoints)
        self.__inhabitant_log += animal.get_class_name() + f'{animal.get_animal_id()} eat ' + \
                                        herbivore.get_class_name() + f'{herbivore.get_animal_id()}|'
        cell_with_herbivore.delete_animal_from_cell(herbivore)
        if animal.get_food_points() > max_fpoints:
            animal.set_food_points(max_fpoints)

    def get_last_inh_id(self) -> int:
        return self.__last_inhabitant_id

    def __increase_last_inhabitant_id(self) -> None:
        self.__last_inhabitant_id += 1

    def __init__(self, area: list[list[Cell]]) -> None:

        self.__area = area
        self.__length = len(area)
        self.__width = len(area[0])
        self.__inhabitant_log = ""
        for area_row in area:
            if isinstance(area_row, Cell):
                raise "Lengt and width values should be more than 2"
            if len(area_row) != self.__width:
                raise "Area should be rectangular size"
        inhabitant_id = 0
        for area_row in area:
            for cell in area_row:
                if cell.get_plant_on_cell() is not None:
                    cell.get_plant_on_cell().set_plant_id(id=inhabitant_id)
                    inhabitant_id += 1
                for animal in cell.get_animals_in_cell():
                    animal.set_animal_id(inhabitant_id)
                    inhabitant_id += 1
        self.__last_inhabitant_id = inhabitant_id

    def transform_area_into_matrix_form(self) -> list[str]:
        matrix_form = []
        for raw_index in range(self.__length):
            for str_index in range(4):
                str_temp = ''
                for column_index in range(self.__width):
                    str_temp += self.__area[raw_index][column_index].info(
                    )[str_index] + '\t'
                matrix_form.append(str_temp)
        return matrix_form

    def display_area(self) -> None:
        for raw_index in range(self.__length):
            for str_index in range(4):
                str_temp = ''
                for column_index in range(self.__width):
                    str_temp += self.__area[raw_index][column_index].info(
                    )[str_index] + '\t'
                print(str_temp)
            print('\n')
        print('___________LOG____________\n', self.__inhabitant_log)

    def next_step(self) -> None:
        self.__inhabitant_log = ''
        self.__animal_moving()
        self.__check_propagating_in_all_cells()
        self.__check_life_and_food_points_in_all_cells()
        self.display_area()

    def get_length(self) -> int:
        return self.__length

    def get_width(self) -> int:
        return self.__width

    @staticmethod
    def generate_animal_sex() -> Sex:
        res_sex = None
        if (random.randint(0, 1) == 0):
            res_sex = Sex.FEMALE
        else:
            res_sex = Sex.MALE
        return res_sex

    @staticmethod
    def create_area_from_database() -> object:    
        length = 3
        wigth = 7
        all_cells = []
        cell_inh_data = pd.DataFrame(
            data=get_data(),
            columns=[
                'id', 'Animal_type', 'Cell_row_index', 'Cell_column_index', 'Sex'
            ],
        ).set_index(keys='id')
        length = cell_inh_data.Cell_row_index.max() + 1
        width = cell_inh_data.Cell_column_index.max() + 1
        for row_index in range(length):
            cell_row = []
            for column_index in range(width):
                selected_inh_data = cell_inh_data.query("Cell_row_index == @row_index & Cell_column_index == @column_index")
                inhabitant_list, plant = Area.transform_df_into_inh_list(selected_inh_data)
                cell_row.append(Cell(row_index, column_index, plant, inhabitant_list))
            all_cells.append(cell_row)
        return Area(all_cells)
        


    @staticmethod
    def transform_df_into_inh_list(df : pd.DataFrame) -> List[object]:
        output = []
        is_plant = False
        for ind, row in df.iterrows():
            type = row.Animal_type
            animal_sex = Sex.MALE if row.Sex == 'male' else Sex.FEMALE
            if type == 'Plant':
                is_plant = True
            if type == 'Rabbit':
                output.append(Rabbit(animal_sex))
            elif type == 'Zebra':
                output.append(Zebra(animal_sex))
            elif type == 'Tiger':
                output.append(Tiger(animal_sex))
            elif type == 'Lion':
                output.append(Lion(animal_sex))
        plant = Plant() if is_plant else None
        return output, plant


