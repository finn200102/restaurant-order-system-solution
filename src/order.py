"""The Order module for the Order class."""
__author__ = "7157747, Gellien, 8425470, Heidusch"


class Order:
    """This is the Order class."""

    def __init__(self):
        """Initilize the Order class."""
        self.items = []

    def add_item(self, order_item):
        """Add an order to the items list.

        Args:
            order_items(OrderItem): an instance of the OrderItem class
        """
        self.items.append(order_item)
        formatted = self.order_item_to_string(order_item)
        print(f"Das folgende Gericht wurde aufgenommen:{formatted}")

    def list_items(self):
        """Return all the items of the order."""
        items = [f"Orderitem {idx}: " + self.order_item_to_string(item)
                 for idx, item in enumerate(self.items)]
        return "".join(items)

    def order_item_to_string(self, order_item):
        """Return an OrderItem object as a string.

        Args:
            order_item(OrderItem): an OrderItem object
        """
        return (
            f"\nName: {order_item.name}\n"
            f"Specialrequests: {order_item.special_request}\n"
            f"Baseprice: {order_item.base_price}\n"
                )

    def remove_item(self, idx: int):
        """Remove an item of the order.

        Args:
            idx(int): The index of the OrderItem in self.items
        """
        if 0 <= idx < len(self.items):
            formatted = self.order_item_to_string(self.items[idx])
            print(f"Das folgende Gericht wurde entfernt:{formatted}")
            self.items.pop(idx)
            return True
        return False

    def add_special_requests_to_item(self, idx: int, special_requests):
        """Add list of special requests to a specific orderitem of the order.

        Args:
            idx (int): The index of the OrderItem in self.items
            special_requests (list[str]): A list of the special_requests
        """
        self.items[idx].special_request += special_requests
        print(
             f"Es wurde '{special_requests}' zu dem folgenden "
             f"Gericht hinzugefügt: "
             f"{self.order_item_to_string(self.items[idx])}"
            )

    def get_total_price(self):
        """Calculate and returns the total price of the order."""
        summ = sum(
            item.base_price + len(item.special_request)
            for item in self.items
        )
        print(f"Der Gesamtbetrag ist: {summ}")
        return summ
