"""Menue Module"""

import csv

class Menu:
    def __init__(self, filename: str):
        self.items: dict[str, float] = {}
        self.menu(filename)

    def menu(self, filename: str):
        """creates the menu"""
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    name = row['name']
                    try:
                        price = float(row['price'].replace(',', '.'))
                        self.items[name] = price
                    except ValueError:
                        print(f"Fehler beim Konvertieren des Preises für '{name}'.")
        except FileNotFoundError:
            print(f"Fehler: Die Datei '{filename}' wurde nicht gefunden.")
        except KeyError:
            print("Fehler: Die Datei hat nicht die erwarteten Spalten 'name' und 'price'.")

    def addItem(self, name: str, price: float) -> None:
        """Adds an item to the menu"""
        self.items[name] = price

    def getItemPrice(self, name: str):
        """gets the price of an item"""
        return self.items.get(name)

    def displayMenu(self):
        """outputs the menu"""
        for name, price in self.items.items():
            print(f"{name}: {price:.2f} €")

