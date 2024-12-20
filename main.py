"""This it the main loop module for the restaurant managment system"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.restaurant import Restaurant
from src.menue import Menu


def convert_arg(arg):
    """Converts the input value of type string to the right type"""
    # Check if input looks like a list
    if arg.startswith('[') and arg.endswith(']'):
        # Remove brackets and split by comma
        items = arg[1:-1].split(',')
        # Convert each item in the list recursively
        return [convert_arg(item.strip()) for item in items]

    try:
        return int(arg)  # Try integer first
    except ValueError:
        try:
            return float(arg)  # Then try float
        except ValueError:
            return str(arg)  # Keep as string if nothing else works

def main():
    """The main loop of the management sytem"""
    menue = Menu("src/food.csv")
    restaurant = Restaurant(menue=menue)
    commands = {
        "at": restaurant.add_table,  # add table
        "aot": restaurant.add_order_to_table, # add order to table
        "sb": restaurant.save_bill, # save bill to txt
        "rot": restaurant.remove_order_from_table, # remove order from table
        "asr": restaurant.add_special_request_item_to_table, # add special request item to table
        "dt": restaurant.display_tables, # displays the tables
        "do": restaurant.display_orders, # display the orders at a table
        "dm": restaurant.display_menue, # display the menue
    }
    def print_commands():
        """Prints out the possible comands with description"""
        print("For each of the following commands the functions docstring will be printed")
        print("Commands are given in the style: command, value1, value2")
        for command, func in commands.items():
            print(f"\ncommand: {command}\ndocstring: {func.__doc__}\n")
    print("Commands are given in the style: command, value1, value2")
    while True:

        command = input("Please give me your comand:\n")
        if command == "q":
            print("You quit the restaurant managment system.")
            break
        if command == "h":
            print_commands()
        else:
            try:
                command = command.split(", ")
                args = [convert_arg(arg) for arg in command[1:]]
                resp = commands[command[0]](*args)
                if resp:
                    print(resp)
            except KeyError:
                print("This command is not implemented, show possible commands with: h")
            except ValueError as ve:
                print(ve)
            except TypeError as te:
                print(te)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
