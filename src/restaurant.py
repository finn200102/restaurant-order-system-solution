class Restaurant:
    def __init__(self, menue):
        """Initializes the Restaurant class"""
        self.menue = menue
        self.tables = []

    def add_table(self, table):
        """Add a table to the restaurant"""
        self.tables.append(table)
