"""Tests for the Order class"""
from src.order import Order
from src.order_item import OrderItem


def test_add_item(order):
    """Test adding one item to an Order"""
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    assert order.items[0].name == "pommes"
    print("test_add_items passed")


def test_remove_item(order):
    """Test removing one item of an Order"""
    assert order.remove_item(0) == True # remove index 0
    print("test_remove_item passed")


def get_total_price(order):
    """Test get total price of all order items"""
    total_price = order.get_total_price()
    assert total_price == 5.6 + 1.0
    print("get_total_price passed")



if __name__ == "__main__":
    order = Order()
    test_add_item(order)
    get_total_price(order)
    test_remove_item(order)
    