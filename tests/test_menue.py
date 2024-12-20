"""Tests for the Menu Class"""
from src.menue import Menu

# Create a Menu instance
m = Menu("src/food.csv")  # Initialize with filename

# Test the menu display
m.display_menu()

# Test adding an item
m.add_item("Vodka", 15.0)
m.display_menu()

# Test getting an item price
print(m.get_item_price("FANTA (0.4)"))
