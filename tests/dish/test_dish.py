import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    # Testa se a classe Dish pode ser instanciada corretamente
    dish = Dish("farinha", 15.99)
    assert dish.name == "farinha"
    assert dish.price == 15.99
    assert dish.recipe == {}

    # Testa se o método mágico __repr__ funciona como esperado
    dish1 = Dish("farinha", 15.99)
    dish2 = Dish("farinha", 15.99)
    dish3 = Dish("Pizza", 12.99)
    assert repr(dish1) == "Dish('farinha', R$15.99)"
    assert repr(dish1) == repr(dish2)
    assert repr(dish1) != repr(dish3)

    # Testa se o método mágico __eq__ funciona como esperado
    assert dish1 == dish2
    assert dish1 != dish3

    # Testa se o método mágico __hash__ funciona como esperado
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # Testa se o método add_ingredient_dependency funciona corretamente
    ingredient1 = Ingredient("farinha")
    dish.add_ingredient_dependency(ingredient1, 1)
    assert dish.recipe == {ingredient1: 1}

    # Testa se são levantados erros ao criar pratos inválidos
    with pytest.raises(TypeError):
        Dish("Invalid Dish", "invalid_price")

    with pytest.raises(ValueError):
        Dish("Invalid Dish", -5.0)

    # Testa receita do prato devolve a quantidade correta de um ingrediente
    assert dish.recipe.get(ingredient1) == 1

    # Testa se o método get_restrictions funciona corretamente
    assert dish.get_restrictions() == {Restriction.GLUTEN}

    # Testa se o método get_ingredients funciona corretamente
    assert dish.get_ingredients() == {Ingredient("farinha")}
