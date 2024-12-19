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
    menue = Menu("src/food.csv")
    restaurant = Restaurant(menue=menue)
    restaurant.add_table(table)
    assert restaurant.tables[0] == table
    print("test_add_table passed")

def test_get_table():
    """Test the get_table function"""
    order = Order()
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    table = Table(1)
    table.add_order(order)
    menue = Menu("src/food.csv")
    restaurant = Restaurant(menue=menue)
    restaurant.add_table(table)
    assert restaurant.get_table(1) == table
    print("test_get_table passed")

def test_save_bill():
    """Test the save_bill function"""
    order = Order()
    order_item = OrderItem("pommes", ["marmelade"], 5.6)
    order.add_item(order_item)
    table = Table(1)
    table.add_order(order)
    menue = Menu("src/food.csv")
    restaurant = Restaurant(menue=menue)
    restaurant.add_table(table)
    total_price = restaurant.get_table(1).get_bill()
    restaurant.save_bill(1, "src/bills.txt")
    with open("src/bills.txt", "r", encoding="utf-8") as f:
        assert "table number: 1, price: 6.6" in f.read()
    with open("src/bills.txt", 'w', encoding='utf-8') as f:
        pass
    print("test_save_bill passed")



if __name__ == "__main__":
    test_add_table()
    test_get_table()
    test_save_bill()