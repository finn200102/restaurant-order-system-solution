"""Tests for the Menue Class"""
from src.menue import Menu


m = Menu.menu("food.csv")
"""tests the output from the menu"""
m.displayMenu()

"""Tests the addition of items"""
m.addItem(str.upper("Vodka",15.0))
m.displayMenu()

"""tests the award of a prize"""
print(m.etItemPrice(str.upper("fanta (0.4)")))