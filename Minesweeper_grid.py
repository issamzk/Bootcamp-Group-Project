import random
print("\nLets play Minesweeper!")

def board (rows_columns, bombs_amount):
        grid = list((" " * (rows_columns + 1)))
        grid[random.randint(0, (rows_columns - 1))] = "Ó"
        return grid

begin = False
while begin == False:
    try:
        rows_columns = int(input("\nHow many rows and columns would you like[min = 4]: "))
        bombs_amount = int(input(f"How many bombs would you like on the board[min = 1 | max < {rows_columns}: "))

        if rows_columns < 4 or rows_columns < 0:
            print("\nThe minimum amount of rows and columns must be greater than 4")
            continue
        elif bombs_amount <= 0:
            print("\nThe minimum amount of bombs must be greater than 0")
            continue
        elif bombs_amount >= rows_columns:
            print(f"\nThe maximum amount of bombs must be less than {rows_columns}")
            continue
        else:
            begin = True
    except ValueError:
        print("Please enter a valid integer.")

print("\n\n\n") 

for x in range(rows_columns):
    print("——————" * (rows_columns + 1))
    print(f"|{x + 1}", *board(rows_columns, bombs_amount),sep = "  |  ")
    
print("——————" * (rows_columns + 1))