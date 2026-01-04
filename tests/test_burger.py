import pytest
import allure
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def create_test_ingredients():
    """Создает стандартный набор тестовых ингредиентов."""
    return (
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 150),
    )


def create_burger_with_ingredients():
    """Создает бургер с булочкой и двумя ингредиентами для тестов."""
    burger = Burger()
    bun = Bun("black bun", 100)
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    
    return burger


@allure.epic("Stellar Burgers")
@allure.feature("Burger")
class TestBurger:
    """Тесты для класса Burger."""

    @allure.story("Инициализация бургера")
    def test_burger_initialization(self):
        """Проверка инициализации пустого бургера."""
        burger = Burger()
        
        assert burger.bun is None
        assert burger.ingredients == []
        assert isinstance(burger.ingredients, list)

    @allure.story("Установка булочек")
    @pytest.mark.parametrize("bun_name,bun_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_set_buns(self, bun_name, bun_price):
        """Проверка установки булочек для бургера."""
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        
        burger.set_buns(bun)
        
        assert burger.bun == bun
        assert burger.bun.get_name() == bun_name
        assert burger.bun.get_price() == bun_price

    @allure.story("Добавление ингредиентов")
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 150),
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        """Проверка добавления ингредиента в бургер."""
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        
        burger.add_ingredient(ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient
        assert burger.ingredients[0].get_name() == name

    @allure.story("Добавление нескольких ингредиентов")
    def test_add_multiple_ingredients(self):
        """Проверка добавления нескольких ингредиентов."""
        burger = Burger()
        ingredient1, ingredient2, ingredient3 = create_test_ingredients()
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        
        assert len(burger.ingredients) == 3
        assert burger.ingredients[0] == ingredient1
        assert burger.ingredients[1] == ingredient2
        assert burger.ingredients[2] == ingredient3

    @allure.story("Удаление ингредиента")
    def test_remove_ingredient(self):
        """Проверка удаления ингредиента по индексу."""
        burger = Burger()
        ingredient1, ingredient2, ingredient3 = create_test_ingredients()
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        
        burger.remove_ingredient(1)
        
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient1
        assert burger.ingredients[1] == ingredient3

    @allure.story("Перемещение ингредиента")
    @pytest.mark.parametrize("index,new_index,expected_order", [
        (0, 1, [1, 0, 2]),
        (2, 0, [2, 0, 1]),
        (1, 2, [0, 2, 1]),
    ])
    def test_move_ingredient(self, index, new_index, expected_order):
        """Проверка перемещения ингредиента в бургере."""
        burger = Burger()
        ingredient0, ingredient1, ingredient2 = create_test_ingredients()
        
        burger.add_ingredient(ingredient0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        burger.move_ingredient(index, new_index)
        
        assert len(burger.ingredients) == 3
        # Проверяем, что ингредиент переместился на новую позицию
        moved_ingredient = [ingredient0, ingredient1, ingredient2][index]
        assert burger.ingredients[new_index] == moved_ingredient

    @allure.story("Расчет цены бургера")
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_price", [
        (100, [100, 200], 500),  # 100*2 + 100 + 200 = 500
        (200, [100], 500),  # 200*2 + 100 = 500
        (150, [50, 75, 25], 450),  # 150*2 + 50 + 75 + 25 = 450
        (100, [], 200),  # 100*2 + 0 = 200
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected_price):
        """Проверка расчета цены бургера с мок-объектами."""
        burger = Burger()
        
        # Создаём мок-объект для булочки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = "test bun"
        burger.bun = mock_bun
        
        # Создаём мок-объекты для ингредиентов
        mock_ingredients = []
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            mock_ingredients.append(mock_ingredient)
        
        burger.ingredients = mock_ingredients
        
        result_price = burger.get_price()
        
        assert result_price == expected_price
        mock_bun.get_price.assert_called_once()
        for mock_ingredient in mock_ingredients:
            mock_ingredient.get_price.assert_called_once()

    @allure.story("Расчет цены бургера с реальными объектами")
    def test_get_price_with_real_objects(self):
        """Проверка расчета цены бургера с реальными объектами."""
        burger = create_burger_with_ingredients()
        
        expected_price = 100 * 2 + 100 + 200  # 500
        assert burger.get_price() == expected_price

    @allure.story("Получение чека")
    def test_get_receipt(self):
        """Проверка формирования чека бургера."""
        burger = create_burger_with_ingredients()
        
        receipt = burger.get_receipt()
        
        assert isinstance(receipt, str)
        assert "black bun" in receipt
        assert "hot sauce" in receipt
        assert "cutlet" in receipt
        assert "Price:" in receipt
        assert str(burger.get_price()) in receipt
        assert "(==== black bun ====)" in receipt

    @allure.story("Получение чека с мок-объектами")
    def test_get_receipt_with_mocks(self):
        """Проверка формирования чека с использованием мок-объектов."""
        burger = Burger()
        
        # Создаём мок-объект для булочки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200
        burger.bun = mock_bun
        
        # Создаём мок-объекты для ингредиентов
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "sour cream"
        mock_ingredient1.get_price.return_value = 150
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "dinosaur"
        mock_ingredient2.get_price.return_value = 200
        
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        
        receipt = burger.get_receipt()
        
        assert isinstance(receipt, str)
        assert "white bun" in receipt
        assert "sour cream" in receipt
        assert "dinosaur" in receipt
        assert "Price:" in receipt
        mock_bun.get_name.assert_called()
        mock_ingredient1.get_type.assert_called()
        mock_ingredient1.get_name.assert_called()
        mock_ingredient2.get_type.assert_called()
        mock_ingredient2.get_name.assert_called()

