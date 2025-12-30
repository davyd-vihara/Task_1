import pytest
import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@allure.epic("Stellar Burgers")
@allure.feature("Ingredient")
class TestIngredient:
    """Тесты для класса Ingredient."""

    @allure.story("Создание ингредиента")
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300.5),
        (INGREDIENT_TYPE_FILLING, "sausage", 0),
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        """Проверка инициализации ингредиента с различными параметрами."""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @allure.story("Получение типа ингредиента")
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    ])
    def test_get_type(self, ingredient_type, name, price):
        """Проверка метода get_type."""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_type() == ingredient_type
        assert isinstance(ingredient.get_type(), str)

    @allure.story("Получение названия ингредиента")
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ])
    def test_get_name(self, ingredient_type, name, price):
        """Проверка метода get_name."""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_name() == name
        assert isinstance(ingredient.get_name(), str)

    @allure.story("Получение цены ингредиента")
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200.5),
        (INGREDIENT_TYPE_FILLING, "cutlet", 0),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 150.75),
    ])
    def test_get_price(self, ingredient_type, name, price):
        """Проверка метода get_price."""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_price() == price
        assert isinstance(ingredient.get_price(), (int, float))








