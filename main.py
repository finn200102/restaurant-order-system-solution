"""This it the main loop module for the restaurant managment system"""
from src.restaurant import Restaurant
from src.menue import Menu


def convert_arg(arg):
    """Converts the input value of type string to the right type"""
    try:
        return int(arg)  # First try integer
    except ValueError:
        try:
            return float(arg)  # Then try float
        except ValueError:
            return str(arg)    # Keep as string if nothing else works


def main():
    """The main loop of the management sytem"""

    menue = Menu("src/food.csv")    
    restaurant = Restaurant(menue=menue)
    commands = {
        "at": restaurant.add_table,  # add table
        "aot": restaurant.add_order_to_table, # add order to table
    }
    while True:
        print("Commands are given in the style: command, value1, value2")
        command = input("Please give me your comand:\n")
        if command == "q":
            print("You quit the restaurant managment system.")
            break
        else:
            try:
                command = command.split(", ")
                args = [convert_arg(arg) for arg in command[1:]]
                resp = commands[command[0]](*args)
                if resp:
                    print(resp)
            except KeyError:
                print("This command is not implemented or not correct , show possible commands with: h")

        



if __name__ == "__main__":
    main()