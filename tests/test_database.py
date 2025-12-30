import pytest
import allure
from unittest.mock import Mock, patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@allure.epic("Stellar Burgers")
@allure.feature("Database")
class TestDatabase:
    """Тесты для класса Database."""

    @allure.story("Инициализация базы данных")
    def test_database_initialization(self):
        """Проверка инициализации базы данных с данными по умолчанию."""
        database = Database()
        
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
        assert isinstance(database.buns, list)
        assert isinstance(database.ingredients, list)

    @allure.story("Проверка булочек в базе данных")
    @pytest.mark.parametrize("index,expected_name,expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_buns_in_database(self, index, expected_name, expected_price):
        """Проверка корректности булочек в базе данных."""
        database = Database()
        
        assert isinstance(database.buns[index], Bun)
        assert database.buns[index].get_name() == expected_name
        assert database.buns[index].get_price() == expected_price

    @allure.story("Проверка ингредиентов в базе данных")
    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_ingredients_in_database(self, index, expected_type, expected_name, expected_price):
        """Проверка корректности ингредиентов в базе данных."""
        database = Database()
        
        assert isinstance(database.ingredients[index], Ingredient)
        assert database.ingredients[index].get_type() == expected_type
        assert database.ingredients[index].get_name() == expected_name
        assert database.ingredients[index].get_price() == expected_price

    @allure.story("Получение доступных булочек")
    def test_available_buns(self):
        """Проверка метода available_buns."""
        database = Database()
        
        buns = database.available_buns()
        
        assert buns == database.buns
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    @allure.story("Получение доступных ингредиентов")
    def test_available_ingredients(self):
        """Проверка метода available_ingredients."""
        database = Database()
        
        ingredients = database.available_ingredients()
        
        assert ingredients == database.ingredients
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    @allure.story("Инициализация с мок-объектами")
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_initialization_with_mocks(self, mock_ingredient, mock_bun):
        """Проверка инициализации базы данных с использованием мок-объектов."""
        # Настраиваем мок-объекты
        mock_bun_instance1 = Mock(spec=Bun)
        mock_bun_instance2 = Mock(spec=Bun)
        mock_bun_instance3 = Mock(spec=Bun)
        mock_bun.side_effect = [mock_bun_instance1, mock_bun_instance2, mock_bun_instance3]
        
        mock_ingredient_instance = Mock(spec=Ingredient)
        mock_ingredient.side_effect = [mock_ingredient_instance] * 6
        
        database = Database()
        
        # Проверяем, что Bun был вызван 3 раза
        assert mock_bun.call_count == 3
        # Проверяем, что Ingredient был вызван 6 раз
        assert mock_ingredient.call_count == 6
        # Проверяем, что булочки и ингредиенты добавлены в списки
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    @allure.story("Проверка создания булочек при инициализации")
    @patch('praktikum.database.Bun')
    def test_bun_creation_on_init(self, mock_bun):
        """Проверка создания булочек во время инициализации."""
        mock_bun_instance = Mock()
        mock_bun.return_value = mock_bun_instance
        
        database = Database()
        
        # Проверяем, что Bun был вызван с правильными параметрами
        assert mock_bun.call_count == 3
        assert len(database.buns) == 3
        # Проверяем аргументы каждого вызова
        assert mock_bun.call_args_list[0][0] == ("black bun", 100)
        assert mock_bun.call_args_list[1][0] == ("white bun", 200)
        assert mock_bun.call_args_list[2][0] == ("red bun", 300)

    @allure.story("Проверка создания ингредиентов при инициализации")
    @patch('praktikum.database.Ingredient')
    def test_ingredient_creation_on_init(self, mock_ingredient):
        """Проверка создания ингредиентов во время инициализации."""
        mock_ingredient_instance = Mock()
        mock_ingredient.return_value = mock_ingredient_instance
        
        database = Database()
        
        # Проверяем, что Ingredient был вызван 6 раз
        assert mock_ingredient.call_count == 6
        assert len(database.ingredients) == 6
        # Проверяем первые несколько вызовов с правильными параметрами
        call_args_list = mock_ingredient.call_args_list
        assert call_args_list[0][0] == (INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert call_args_list[1][0] == (INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        assert call_args_list[2][0] == (INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        assert call_args_list[3][0] == (INGREDIENT_TYPE_FILLING, "cutlet", 100)
        assert call_args_list[4][0] == (INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        assert call_args_list[5][0] == (INGREDIENT_TYPE_FILLING, "sausage", 300)

