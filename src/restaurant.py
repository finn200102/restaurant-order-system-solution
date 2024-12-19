class Restaurant:
    def __init__(self, menue):
        """Initializes the Restaurant class"""
        self.menue = menue
        self.tables = []

    def add_table(self, table):
        """Add a table to the restaurant"""
        self.tables.append(table)

    def get_table(self, idx):
        """Returns the table with the idx"""
        matches =  [t for t in self.tables if t.table_number == idx]
        return matches[0] if matches else None
    
    def save_bill(self, idx, filepath):
        """Saves the bill to a txt"""
        bill = self.get_table(idx).get_bill()
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"table number: {idx}, price: {bill}\n")