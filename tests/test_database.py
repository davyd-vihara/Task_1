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
        
        # Используем методы для проверки
        buns = database.available_buns()
        ingredients = database.available_ingredients()
        
        assert len(buns) == 3
        assert len(ingredients) == 6
        assert isinstance(buns, list)
        assert isinstance(ingredients, list)

    @allure.story("Проверка булочек в базе данных")
    @pytest.mark.parametrize("index,expected_name,expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_buns_in_database(self, index, expected_name, expected_price):
        """Проверка корректности булочек в базе данных через метод available_buns."""
        database = Database()
        
        # Используем метод для получения булочек
        buns = database.available_buns()
        
        assert isinstance(buns[index], Bun)
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

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
        """Проверка корректности ингредиентов в базе данных через метод available_ingredients."""
        database = Database()
        
        # Используем метод для получения ингредиентов
        ingredients = database.available_ingredients()
        
        assert isinstance(ingredients[index], Ingredient)
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price

    @allure.story("Получение доступных булочек")
    def test_available_buns(self):
        """Проверка метода available_buns."""
        database = Database()
        
        # Используем метод для получения булочек
        buns = database.available_buns()
        
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        # Проверяем, что метод возвращает корректные данные
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    @allure.story("Получение доступных ингредиентов")
    def test_available_ingredients(self):
        """Проверка метода available_ingredients."""
        database = Database()
        
        # Используем метод для получения ингредиентов
        ingredients = database.available_ingredients()
        
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        # Проверяем, что метод возвращает корректные данные
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING

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
        # Используем методы для проверки результатов
        buns = database.available_buns()
        ingredients = database.available_ingredients()
        assert len(buns) == 3
        assert len(ingredients) == 6

    @allure.story("Проверка создания булочек при инициализации")
    @patch('praktikum.database.Bun')
    def test_bun_creation_on_init(self, mock_bun):
        """Проверка создания булочек во время инициализации через метод available_buns."""
        mock_bun_instance = Mock()
        mock_bun.return_value = mock_bun_instance
        
        database = Database()
        
        # Проверяем, что Bun был вызван с правильными параметрами
        assert mock_bun.call_count == 3
        # Используем метод для проверки результатов
        buns = database.available_buns()
        assert len(buns) == 3
        # Проверяем аргументы каждого вызова
        assert mock_bun.call_args_list[0][0] == ("black bun", 100)
        assert mock_bun.call_args_list[1][0] == ("white bun", 200)
        assert mock_bun.call_args_list[2][0] == ("red bun", 300)

    @allure.story("Проверка создания ингредиентов при инициализации")
    @patch('praktikum.database.Ingredient')
    def test_ingredient_creation_on_init(self, mock_ingredient):
        """Проверка создания ингредиентов во время инициализации через метод available_ingredients."""
        mock_ingredient_instance = Mock()
        mock_ingredient.return_value = mock_ingredient_instance
        
        database = Database()
        
        # Проверяем, что Ingredient был вызван 6 раз
        assert mock_ingredient.call_count == 6
        # Используем метод для проверки результатов
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        # Проверяем первые несколько вызовов с правильными параметрами
        call_args_list = mock_ingredient.call_args_list
        assert call_args_list[0][0] == (INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert call_args_list[1][0] == (INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        assert call_args_list[2][0] == (INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        assert call_args_list[3][0] == (INGREDIENT_TYPE_FILLING, "cutlet", 100)
        assert call_args_list[4][0] == (INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        assert call_args_list[5][0] == (INGREDIENT_TYPE_FILLING, "sausage", 300)

