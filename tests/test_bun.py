import pytest
import allure
from praktikum.bun import Bun


@allure.epic("Stellar Burgers")
@allure.feature("Bun")
class TestBun:
    """Тесты для класса Bun."""

    @allure.story("Создание булочки")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),  # Стандартное название (латиница)
        ("Булочка", 200),  # Кириллица
        ("bun123", 150.5),  # Латиница с числами
        ("bun!@#", 0),  # Латиница со спецсимволами, граничная цена
        ("", 0),  # Пустая строка, граничная цена
    ])
    def test_bun_initialization(self, name, price):
        """Проверка инициализации булочки с различными параметрами."""
        bun = Bun(name, price)
        
        assert bun is not None
        assert isinstance(bun, Bun)

    @allure.story("Получение названия булочки")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),  # Стандартное название (латиница, пробелы)
        ("Булочка", 200),  # Кириллица
        ("bun123", 150),  # Латиница с числами
        ("bun!@#", 100),  # Латиница со спецсимволами
        ("", 0),  # Пустая строка (граничное значение)
        ("a", 50),  # Минимальная длина (граничное значение)
    ])
    def test_get_name(self, name, price):
        """Проверка метода get_name."""
        bun = Bun(name, price)
        
        assert bun.get_name() == name
        assert isinstance(bun.get_name(), str)

    @allure.story("Получение цены булочки")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 0),  # Граничное значение - минимальная цена
        ("white bun", 100),  # Целое число
        ("red bun", 200.5),  # Дробное число
        ("sesame bun", 150.75),  # Дробное число с двумя знаками
        ("bun", 0.01),  # Минимальное положительное дробное (граничное значение)
        ("bun", 999999.99),  # Большое значение (граничное значение)
    ])
    def test_get_price(self, name, price):
        """Проверка метода get_price."""
        bun = Bun(name, price)
        
        assert bun.get_price() == price
        assert isinstance(bun.get_price(), (int, float))





