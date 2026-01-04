import pytest
import allure
from praktikum.bun import Bun


@allure.epic("Stellar Burgers")
@allure.feature("Bun")
class TestBun:
    """Тесты для класса Bun."""

    @allure.story("Создание булочки")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("sesame bun", 150.5),
        ("", 0),
    ])
    def test_bun_initialization(self, name, price):
        """Проверка инициализации булочки с различными параметрами."""
        bun = Bun(name, price)
        
        assert bun is not None
        assert isinstance(bun, Bun)

    @allure.story("Получение названия булочки")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_get_name(self, name, price):
        """Проверка метода get_name."""
        bun = Bun(name, price)
        
        assert bun.get_name() == name
        assert isinstance(bun.get_name(), str)

    @allure.story("Получение цены булочки")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 0),
        ("sesame bun", 150.75),
    ])
    def test_get_price(self, name, price):
        """Проверка метода get_price."""
        bun = Bun(name, price)
        
        assert bun.get_price() == price
        assert isinstance(bun.get_price(), (int, float))





