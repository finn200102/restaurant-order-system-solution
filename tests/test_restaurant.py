from src.restaurant import Restaurant
from src.table import Table
from src.menue import Menu
from src.order import Order
from src.order_item import OrderItem


def test_add_table():
    """Test the add_table function"""
    order = Order()
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    table = Table(1)
    table.add_order(order)
    menue = Menu("food.csv")
    restaurant = Restaurant(menue=menue)
    restaurant.add_table(table)
    assert restaurant.tables[0] == table
    print("test_add_table passed")


if __name__ == "__main__":
    test_add_table()