from Predator import Predator
from Sex import Sex

class Lion(Predator):

    def __init__(self, sex : Sex, id_number : int = -1, animal_cannot_move : bool = False) -> None:
        super().__init__(food_points=5, life_points=4, cell_speed=3,
         animal_id=id_number, animal_cannot_move=animal_cannot_move,
         sex=sex, max_food_points=5
        )

    def info(self) -> str:
        output = f'L-{self._Animal__animal_id}('
        if self._Animal__animal_sex == Sex.FEMALE:
            output += 'fem,'
        else:
            output += 'mal,'
        output += f'{self._Animal__food_points},{self._Animal__life_points})'
        return output

    def get_class_name(self) -> str:
        return 'L-'
