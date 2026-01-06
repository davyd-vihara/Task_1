import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def test_ingredients():
    """Фикстура для создания стандартного набора тестовых ингредиентов."""
    return (
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 150),
    )


@pytest.fixture
def burger_with_ingredients():
    """Фикстура для создания бургера с булочкой и двумя ингредиентами для тестов."""
    burger = Burger()
    bun = Bun("black bun", 100)
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    
    return burger

