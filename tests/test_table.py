"""Tests for the src/table.py Table class"""
from src.table import Table
from src.order import Order
from src.order_item import OrderItem


def test_add_order(table):
    """Test the add_order method"""
    order = Order()
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    table.add_order(order)
    assert table.orders[0] == order
    print("test_add_order passed")

def test_get_bill(table):
    """Test the get_bill method"""
    order = Order()
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    order2 = Order()
    order_item2 = OrderItem("Cola", [], 7.6)
    order2.add_item(order_item2)
    table.add_order(order)
    table.add_order(order2)
    assert table.get_bill() == 6.6 + 7.6
    print("test_get_bill passed")


def test_remove_order(table):
    """Test the remove_order method"""
    order = Order()
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    table.add_order(order)
    assert table.remove_order(0) == True
    assert table.orders == []
    print("test_remove_order passed")


if __name__ == "__main__":
    table = Table(table_number=1)
    test_add_order(table)
    table2 = Table(table_number=1)
    test_get_bill(table2)
    table3 = Table(table_number=1)
    test_remove_order(table3)