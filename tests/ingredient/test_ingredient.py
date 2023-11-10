from src.models.ingredient import Ingredient


# Req 1
def test_ingredient():
    # Testa se a classe Ingredient pode ser instanciada corretamente
    ingredient = Ingredient("Cenoura")
    assert ingredient.name == "Cenoura"
    assert ingredient.restrictions == set()

    # Testa se o método mágico __repr__ funciona como esperado
    ingredient1 = Ingredient("Cenoura")
    ingredient2 = Ingredient("Cenoura")
    ingredient3 = Ingredient("Brócolis")
    ingredient = Ingredient("Cenoura")
    assert repr(ingredient) == "Ingredient('Cenoura')"

    # Testa se o método mágico __eq__ funciona como esperado
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    # Testa se o método mágico __hash__ funciona como esperado
    ingredient3 = Ingredient("Brócolis")
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
