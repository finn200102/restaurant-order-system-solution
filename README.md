# Restaurant Order System

A Python-based restaurant management system for handling tables, orders, and bills.

## System Requirements

- Python 3.10 or higher
- Standard Python libraries
- Platform independent

## Installation

1. Clone the repository or unzip the project files

```bash
git clone [repository-url]
```

2. Install in development mode with dependencies:

```bash
pip install -e .
```

## Usage

1. Ensure `food.csv` menu file is present in the project directory
2. Run the main script in the project directory

```bash
python main.py
```

### Available Commands

- `at, [table_number]` - Add new table
- `aot, [table_number], [food_item], [special_request]` - Add order to table
- `sb, [table_number]` - Save bill for table
- `rot, [table_number], [order_index]` - Remove order from table
- `asr, [table_number], [item_index], [order_index], [special_request]` - Add special request
- `h` - Show help
- `q` - Quit program

## Project Structure

- `src/` - Source code directory
- `tests/` - Test files
- `src/food.csv` - Menu data
- `src/bills.txt` - Generated bills per table

## Testing

Run tests using:

```bash
python tests/{filenames}
```

## Known Issues

No known issues at this time.
