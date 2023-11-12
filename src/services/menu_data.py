import csv
from typing import Set
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        with open(source_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:

                # Cria o prato se for um prato novo
                if row["dish"] not in self.dishes:
                    self.dishes.add(Dish(row["dish"], float(row["price"])))

                # Adiciona o ingrediente à receita do prato
                for dish in self.dishes:
                    if dish.name == row["dish"]:
                        dish.add_ingredient_dependency(
                            Ingredient(row["ingredient"]),
                            int(row["recipe_amount"])
                        )
