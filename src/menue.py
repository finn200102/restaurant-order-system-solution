"""The Menue Module for the Module class."""
__author__ = "7157747, Gellien, 8425470, Heidusch"
import csv


class Menu:
    """The menu class."""

    def __init__(self, filename: str):
        """Initialize the Menue class."""
        self.items: dict[str, float] = {}
        self.menu(filename)

    def menu(self, filename: str = "src/food.csv"):
        """Create the menu."""
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    name = row['name']
                    try:
                        price = float(row['price'].replace(',', '.'))
                        self.items[name] = price
                    except ValueError:
                        print(f"Konvertierungsfehler des Preises für {name}.")
        except FileNotFoundError:
            print(f"Fehler: Die Datei '{filename}' wurde nicht gefunden.")
        except KeyError:
            print("Fehler: Nicht die erwarteten Spalten 'name' und 'price'.")

    def save_menu(self, filename: str = "src/food.csv"):
        """Save the menu items to a CSV file."""
        try:
            with open(filename, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, ['name', 'price'], delimiter=';')
                writer.writeheader()
                for name, price in self.items.items():
                    writer.writerow({
                        'name': name,
                        'price': str(price).replace('.', ',')
                    })
        except IOError:
            print(f"Fehler: '{filename}' konnte nicht gespeichert werden.")

    def add_item(self, name: str, price: float) -> None:
        """Add an item to the menu."""
        self.items[name] = price
        self.save_menu()

    def get_item_price(self, name: str):
        """Get the price of an item."""
        return self.items.get(name)

    def display_menu(self):
        """Output the menu."""
        for idx, (name, price) in enumerate(self.items.items()):
            print(f"{idx}): {name}: {price:.2f} €")
