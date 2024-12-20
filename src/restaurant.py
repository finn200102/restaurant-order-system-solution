from src.order_item import OrderItem
from src.order import Order
from src.table import Table
class Restaurant:
    def __init__(self, menue):
        """Initializes the Restaurant class"""
        self.menue = menue
        self.tables = []

    def add_table(self, idx: int):
        """Add a table to the restaurant with idx
        
        Args:
            idx (int): The table number id
        """
        self.tables.append(Table(idx))

    def get_table(self, idx):
        """Returns the table with the idx"""
        matches =  [t for t in self.tables if t.table_number == idx]
        return matches[0] if matches else None
    
    def list_orders(self, idx: int):
        """Prints a list of the orders

        Args:
            idx (int): The table number
        """
        if self.get_table(idx).orders:
            for order in self.get_table(idx).orders:
                pass

        
    def add_special_request_item_to_table(self, idx: int, order_item: int, order_id: int, special_request):
        print(f"Es wurde {special_request} zu dem Orderitem {order_item} der Order {order_id} am Tisch {self.get_table(idx).table_number} hinzugefügt")
        self.get_table(idx).orders[order_id].items[order_item].special_request += special_request
        
        


    def add_order_to_table(self, idx: int, name: str, special_request: list[str]):
        """Adds an order to a table
        
        Args:
            idx (int): The table number
            name (str): The name of the food
            special_requests (list[str]): A list of the special_requests (can be empty)
            base_price (float or int): The base price of the food
        """
        price = self.menue.get_item_price(name)
        if not price:
            raise ValueError(f"The name: {name} is not in the menue")
        order = Order()
        order.add_item(OrderItem(name, special_request, float(price)))
        self.get_table(idx).add_order(order)

    def remove_order_from_table(self, idx, order_idx):
        """Remove the order_idx order from table idx"""
        self.get_table(idx).remove_order(order_idx)
    
    def save_bill(self, idx, filepath="src/bills.txt"):
        """Saves the bill to a txt"""
        bill = self.get_table(idx).get_bill()
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"table number: {idx}, price: {bill}\n")

    def display_tables(self):
        """Shows the Tables of the restaurant"""
        if not self.tables:
            print("Es sind keine Tische vorhanden!")
            return
        print("Folgende Tische sind vorhanden:")
        for table in self.tables:
            print(table.table_number)

    def display_orders(self, idx: int):
        """Shows the Order of the table idx
        
        Args:
            idx (int): The table number
        """
        if self.tables == []:
            print("Es gibt noch keine Tische")
        elif self.get_table(idx) == None:
            print("Die Tisch nummer gibt es noch nicht.")
        elif not self.get_table(idx).orders:
            print(f"Es sind keine Bestellungen vorhanden am Tisch {idx}")
        else:
            print("Folgende Bestellungen sind vorhanden:")
            for idx, order in enumerate(self.get_table(idx).orders):
                print(f"\nBestellung mit index: {idx}:")
                print(order.list_items())

    def display_menue(self):
        """Displays the menue"""
        self.menue.display_menu()