from Animal import Animal

class Predator(Animal):
    def __init__(self, food_points, life_points) -> None:
        super().__init__(food_points, life_points)

    def get_animal_class_name(self):
        return 'Predator'

    def get_max_food_points(self):
        pass

    def get_class_name(self):
        pass