import csv
from typing import Set
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> None:
        with open(source_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Ignora o cabeçalho

            current_dish = None
            for row in reader:
                dish_name, dish_price, ing_name, ing_quantity = row

                # Cria o prato se for um prato novo
                if current_dish is None or current_dish.name != dish_name:
                    current_dish = Dish(dish_name, float(dish_price))
                    self.dishes.add(current_dish)

                # Adiciona o ingrediente à receita do prato
                ingredient = Ingredient(ing_name)
                current_dish.add_ingredient_dependency(
                    ingredient, int(ing_quantity)
                    )
