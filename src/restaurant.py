"""The restaurant module for the Restaurant class."""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.order_item import OrderItem
from src.order import Order
from src.table import Table


class Restaurant:
    """This is the Restaurant class."""

    def __init__(self, menue):
        """Initialize the Restaurant class."""
        self.menue = menue
        self.tables = []

    def add_table(self, idx: int):
        """Add a table to the restaurant with idx.

        Args:
            idx (int): The table number id
        """
        if self.get_table(idx):
            print("this table already exists")
        else:
            self.tables.append(Table(idx))

    def get_table(self, idx):
        """Return the table with the idx.

        Args:
            idx (int): Table number
        """
        matches = [t for t in self.tables if t.table_number == idx]
        return matches[0] if matches else None

    def add_special_request_item_to_table(self, idx: int, order_item: int,
                                          order_id: int, special_request):
        """Add a special request to a specific order item at a table.

        Args:
        idx (int): Table index
        order_item (int): Index of the item in the order
        order_id (int): ID of the order
        special_request: Special request to be added to the item
        """
        print(
            f"Es wurde {special_request} zu dem Orderitem {order_item} "
            f"der Order {order_id} am Tisch {self.get_table(idx)} hinzugefügt"
        )
        self.get_table(idx).orders[order_id].items[order_item].special_request += (
            special_request
        )

    def add_order_to_table(self, idx: int, name: str,
                           special_request: list[str] = []):
        """Add an order to a table.

        Args:
            idx (int): The table number
            name (str): The name of the food
            special_requests (list[str]): A list of the special_requests
            base_price (float or int): The base price of the food
        """
        price = self.menue.get_item_price(name)
        if not price:
            raise ValueError(f"The name: {name} is not in the menue")
        order = Order()
        order.add_item(OrderItem(name, special_request, float(price)))
        self.get_table(idx).add_order(order)



    def remove_order_from_table(self, idx, order_idx):
        """Remove the order_idx order from table idx.

        Args:
            idx (int): Tavle number
            order_idx (idx): Order number
        """
        self.get_table(idx).remove_order(order_idx)

    def save_bill(self, idx, filepath="src/bills.txt"):
        """Save the bill to a txt.

        Args:
            idx (int): Table number
            filepath (str): Storage location for the bills
        """
        bill = self.get_table(idx).get_bill()
        print(f"Der finale Preis für den Tisch {idx} ist: {bill}")
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"table number: {idx}, price: {bill}\n")

    def display_tables(self):
        """Show the tables."""
        if not self.tables:
            print("Es sind keine Tische vorhanden!")
            return
        print("Folgende Tische sind vorhanden:")
        for table in self.tables:
            print(table.table_number)

    def display_orders(self, idx: int):
        """Show the Order of the table idx.

        Args:
            idx (int): The table number
        """
        if not self.tables:
            print("Es gibt noch keine Tische")
        elif self.get_table(idx) is None:
            print("Die Tisch nummer gibt es noch nicht.")
        elif not self.get_table(idx).orders:
            print(f"Es sind keine Bestellungen vorhanden am Tisch {idx}")
        else:
            print("Folgende Bestellungen sind vorhanden:")
            for i, order in enumerate(self.get_table(idx).orders):
                print(f"\nBestellung mit index: {i}:")
                print(order.list_items())

    def display_menue(self):
        """Display the menue."""
        self.menue.display_menu()
