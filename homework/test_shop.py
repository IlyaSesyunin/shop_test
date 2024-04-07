"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999)
        assert product.check_quantity(1000)
        assert product.check_quantity(1001) is False
        assert product.check_quantity(0)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)

        assert product.check_quantity(0)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1

        cart.add_product(product, 99)
        assert cart.products[product] == 100

        cart.add_product(product, 5)
        assert cart.products[product] == 105

    def test_remove_product(self, product, cart):
        cart.add_product(product, 100)
        cart.remove_product(product, 99)
        assert cart.products[product] == 1

        cart.remove_product(product)
        cart.add_product(product, 99)
        cart.remove_product(product, 100)
        assert product not in cart.products

        cart.add_product(product, 99)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear(self, product, cart):
        cart.add_product(product, 100)
        cart.clear()
        assert product not in cart.products

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 100)
        assert cart.get_total_price() == 10000

        cart.remove_product(product, 100)
        cart.clear()
        assert cart.get_total_price() == 0

    def test_buy(self, product, cart):
        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 900

        product.quantity -= 900
        cart.add_product(product, 100)
        with pytest.raises(ValueError):
            cart.buy()
