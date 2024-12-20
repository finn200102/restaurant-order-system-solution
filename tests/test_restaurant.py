"""Test for the src/restaurant.py Restaurant class"""
from src.restaurant import Restaurant
from src.table import Table
from src.menue import Menu
from src.order import Order
from src.order_item import OrderItem


def test_add_table():
    """Test the add_table function"""
    menue = Menu("src/food.csv")
    restaurant = Restaurant(menue=menue)
    restaurant.add_table(1)
    assert restaurant.tables[0].table_number == 1
    print("test_add_table passed")

def test_get_table():
    """Test the get_table function"""
    menue = Menu("src/food.csv")
    restaurant = Restaurant(menue=menue)
    restaurant.add_table(1)
    assert restaurant.get_table(1).table_number == 1
    print("test_get_table passed")

def test_save_bill():
    """Test the save_bill function"""
    menue = Menu("src/food.csv")
    restaurant = Restaurant(menue=menue)
    restaurant.add_table(1)
    restaurant.add_order_to_table(1, "pommes", ["marmelade"], 5.6)
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