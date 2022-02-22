from Animal import Animal

class Predator(Animal):
    def __init__(self, food_points, life_points, cell_speed, animal_id,
                sex, max_food_points, animal_cannot_move ) -> None:
        super().__init__(food_points, life_points, cell_speed, animal_id,
                        sex, max_food_points, animal_cannot_move
        )

    def get_animal_class_name(self):
        return 'Predator'
