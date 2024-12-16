"""Tests for the Order class"""
from src.order import Order
from src.order_item import OrderItem


def test_add_item(order):
    """Test adding one item to an Order"""
    order_item = OrderItem("pommes", "marmelade", 5.6)
    order.add_item(order_item)
    assert order.items[0].name == "pommes"
    print("test_add_items passed")


if __name__ == "__main__":
    order = Order()
    test_add_item(order)