"""Datastructure for an order item"""
__author__ = "7157747, Gellien, 8425470, Heidusch"

class OrderItem:
    def __init__(self, name: str, special_request: str, base_price: float):
        self.name = name
        self.special_request = special_request
        self.base_price = base_price
        self.final_price = None