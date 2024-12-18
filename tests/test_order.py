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


def test_get_total_price(order):
    """Test get total price of all order items"""
    total_price = order.get_total_price()
    assert total_price == 5.6 + 1.0
    print("test_get_total_price passed")


def test_add_special_requests_to_item(order):
    """Test add special requests to specific item of an order"""
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    order.add_special_requests_to_item(0, ["ketchup", "wine"])
    assert len(order.items[0].special_request) == 3
    print("test_add_special_request_to_item passed")



if __name__ == "__main__":
    order = Order()
    test_add_item(order)
    test_get_total_price(order)
    test_remove_item(order)
    test_add_special_requests_to_item(order)
    