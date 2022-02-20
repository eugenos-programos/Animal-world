from tokenize import Triple
import unittest
import time
import random
from colorama import Fore

from sqlalchemy import true

from Animal import Animal
from Zebra import Zebra
from Sex import Sex
from Rabbit import Rabbit
from Herbivore import Herbivore 
from Tiger import Tiger
from Lion import Lion
from Cell import Cell
from Plant import Plant

def pprint() -> None:
    print('.', end='', flush=True)
    time.sleep(random.random())

def gratulations_message(tests_name : str) -> None:
    print(Fore.GREEN + f'\nGratulations! {tests_name.capitalize()} tests passed!')

class Test(unittest.TestCase):        
    def tests_for_animal_class(self) -> None:
        animal_ex = Animal()

        #initializing
        animal_ex._Animal__max_food_points = 100
        animal_ex._Animal__life_points = 34
        animal_ex._Animal__animal_sex = Sex.FEMALE
        animal_ex.set_food_points(6)
        animal_ex.set_cannot_animal_move(True)
        animal_ex.set_animal_id(234)
        animal_ex._Animal__cell_speed = 2
        print(Fore.WHITE + 'Animal class testing', end='', flush=True)
        pprint()

        #tests
        self.assertEqual(animal_ex.get_food_points(), 6)
        self.assertEqual(animal_ex.get_life_points(), 34)
        self.assertEqual(animal_ex.get_cell_speed(), 2)
        self.assertEqual(animal_ex.get_animal_id(), 234)
        self.assertEqual(animal_ex.get_animal_sex(), Sex.FEMALE)
        self.assertEqual(animal_ex.get_max_food_points(), 100)
        pprint()
        animal_ex.next_step()

        self.assertEqual(animal_ex.get_food_points(), 5)
        self.assertEqual(animal_ex.get_life_points(), 33)
        pprint()
        gratulations_message('animal class')
    
    def tests_for_herbivore_and_predator_classes(self) -> None:
        print(Fore.WHITE + "Herbivore and predator classes testing", end='', flush=True)
        zebra = Zebra(Sex.FEMALE, id_number=34, animal_cannot_move=True)
        self.assertEqual(zebra.info(), "Z-34(fem,4,4)")
        self.assertEqual(Zebra.get_class_name(), 'Z-')
        self.assertEqual(zebra.get_max_food_points(), 4)
        pprint()

        rabbit = Rabbit(Sex.MALE)
        self.assertEqual(rabbit.info(), "R--1(mal,4,4)")
        self.assertEqual(rabbit.get_class_name(), 'R-')
        self.assertEqual(rabbit.get_max_food_points(), 3)
        self.assertEqual(rabbit._Rabbit__animal_cannot_move, False)
        self.assertEqual(rabbit._Rabbit__cell_speed, 1)
        pprint()

        tiger = Tiger(sex=Sex.FEMALE, id_number=100)
        self.assertEqual(tiger._Tiger__max_food_points, 4)
        self.assertEqual(tiger.info(), "T-100(fem,4,4)")
        self.assertEqual(tiger.get_class_name(), "T-")
        self.assertEqual(tiger.get_max_food_points(), 4)
        self.assertEqual(tiger._Tiger__animal_cannot_move, False)
        self.assertEqual(tiger._Tiger__cell_speed, 2)
        pprint()

        lion = Lion(sex=Sex.MALE, id_number=6, animal_cannot_move=True)
        self.assertEqual(lion.info(), "L-6(mal,5,4)")
        self.assertEqual(lion.get_class_name(), "L-")
        self.assertEqual(lion.get_max_food_points(), 5)
        self.assertEqual(lion._Lion__cell_speed, 3)
        self.assertEqual(lion._Lion__animal_cannot_move, True)
        pprint()

        gratulations_message("herbivore and predator classes")

    def cell_tests(self) -> None:
        print(Fore.WHITE + 'Cell class testing')
        animals_for_cell = [
            Rabbit(Sex.MALE),
            Lion(Sex.MALE)
        ]
        plant_on_cell = Plant()

        cell = Cell(raw_index=2,
                    column_index=3,
                    plant_on_cell=plant_on_cell,
                    animals=animals_for_cell.copy()
        )

        animal_to_add = Zebra(Sex.FEMALE)
        cell.add_animal_on_cell(animal_to_add)
        self.assertListEqual(cell.get_animals_in_cell(),
                             animals_for_cell + [animal_to_add]  # add animal function
        )
        self.assertTrue(cell.is_animal_with_another_sex(Zebra(Sex.MALE)))
        self.assertFalse(cell.is_animal_with_another_sex(Tiger(Sex.MALE)))
        self.assertTrue(cell.find_herbivore())
        self.assertListEqual([cell.get_column_index(), cell.get_raw_index()],
                             [3, 2]
        )
        self.assertEqual(cell.get_plant_on_cell(), plant_on_cell)
        correct_information = [
            'P--1(4)', 'R--1(mal,4,4)',
            'L--1(mal,5,4)', 'Z--1(fem,4,4)'
        ]
        self.assertEqual(correct_information, cell.info())
        cell.next_step()
        correct_information = [

        ]
        print(cell.info())
        self.assertEqual()






if __name__ == '__main__':
    test = Test()
    test.tests_for_animal_class()
    test.tests_for_herbivore_and_predator_classes()
    test.cell_tests()
    



