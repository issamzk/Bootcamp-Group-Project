import random
print("\nLets play Minesweeper!")

#Function which takes input and creates lists to form the grid and inserts bombs at random
def board (rows_columns, bombs_amount):
        grid = list((" " * (rows_columns + 1)))
        grid[random.randint(0, (rows_columns - 1))] = "Ó"
        return grid

#While loop to take input from user
begin = False
while begin == False:
    rows_columns = int(input("\nHow many rows and columns would you like[min = 4]: "))
    bombs_amount = int(input(f"How many bombs would you like on the board[min = 1 | max < {rows_columns}: "))
       
    #Test if input is valid
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

#Create a break for the grid
print("\n\n\n") 

#creating the x-axis numbering
x_axis = list((" " * (rows_columns + 1)))
for x in range(rows_columns):
    x_axis [x] = x + 1
print("——————" * (rows_columns + 1))
print("| ", * x_axis, sep = "  |  ")

#prints grid and y-axis numbering, calls to function board()
for x in range(rows_columns):
    print("——————" * (rows_columns + 1))
    print(f"|{x + 1}", *board(rows_columns, bombs_amount),sep = "  |  ")
 #Bottom  line of grid   
print("——————" * (rows_columns + 1))
