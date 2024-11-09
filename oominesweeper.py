import random
import sys
import os

# clears the terminal (hopefully)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# optimized uncovering 0s: pick random spots until you find a 0 > check all adjacent 0s and add them to a list >
# > check if the list(s) contains all the 0s > if not repeat

# difficulties:
EASY = [9, 9, 10]
INTERMEDIATE = [16, 16, 40]
EXPERT = [16, 30, 99]
DEBUG = [3, 3, 1]

class Game:
    def __init__(self):
        self.difficulty = ""
        self.seed = None

    # takes a string as an input and, if it's in a valid format, returns a list with the board size and mines
    def custom_difficulty(self):
        print("\ntype rows, columns, mines\n")
        while True:
            self.difficulty = input("(example: 10, 20, 35): ")
            self.difficulty = self.difficulty.split(", ")
            try:
                self.difficulty = [int(item) for item in self.difficulty]
            except:
                print("\ninvalid input! please input a difficulty in this format:\n rows, columns, mines")
                continue
            if self.difficulty[0] > 70 or self.difficulty[1] > 70:
                print("\nboard is too big! please stay below 70 rows or columns (yes 69 works).\n")
                continue
            if self.difficulty[2] >= self.difficulty[0] * self.difficulty[1]:
                print("\ntoo many mines! chill out!\n")
                continue
            break
        return(self.difficulty)

    # takes an input, tried to turn it into an integer and sets it as the custom seed or, if input = 0, randomizes the seed
    def set_seed(self):
        while True:
            print("\ntype seed (0 to randomize): ")
            custom_seed = input("type a number: ")
            try:
                custom_seed = int(custom_seed)
            except:
                print("\nplease type a number.\n")
                continue
            self.seed = custom_seed
            if custom_seed != 0:
                random.seed(custom_seed)
            else:
                random.seed(random.randrange(0, 1000000000))
            break

    # asks for input to set the GAME_DIFFICULTY constant to one of the difficulties or runs the
    # function to set a custom difficulty
    def set_difficulty(self):
        print("\nchoose difficulty\n 1) easy: 9x9, 10 mines\n 2) intermediate: 16x16, 40 mines\n 3) expert: 30x16, 99 mines\n 4) custom\n")
        while True:
            self.difficulty = input("select difficulty (type a number): ")
            if self.difficulty == "exit":
              sys.exit()

            try:
                self.difficulty = int(self.difficulty)
            except:
                print("\nplease select a valid difficulty.\n")
                continue

            if self.difficulty not in range(1, 5):
                print("\nplease select a valid difficulty.\n")
                continue
            elif self.difficulty == 1:
                self.difficulty = EASY
            elif self.difficulty == 2:
                self.difficulty = INTERMEDIATE
            elif self.difficulty == 3:
                self.difficulty = EXPERT
            elif self.difficulty == 4:
                self.difficulty = self.custom_difficulty()

            break
        return(self.difficulty)

    # returns the coordinates for valid adjacent cells according to what case the input coordinates are
    def adjacency_check(self, row, column):
        if case_board.board_matrix[row][column] == 0:
            return([
                [row, column + 1],
                [row + 1, column],
                [row + 1, column + 1],
                [row, column - 1],
                [row - 1, column],
                [row - 1, column - 1],
                [row + 1, column - 1],
                [row - 1, column + 1]
            ])
        elif case_board.board_matrix[row][column] == 1:
            return([
                [row, column + 1],
                [row + 1, column],
                [row + 1, column + 1]
            ])
        elif case_board.board_matrix[row][column] == 2:
            return([
                [row + 1, column],
                [row, column - 1],
                [row + 1, column - 1]
            ])
        elif case_board.board_matrix[row][column] == 3:
            return([
                [row, column - 1],
                [row - 1, column],
                [row - 1, column - 1]
            ])
        elif case_board.board_matrix[row][column] == 4:
            return([
                [row, column + 1],
                [row - 1, column],
                [row - 1, column + 1]
            ])
        elif case_board.board_matrix[row][column] == 5:
            return([
                [row, column + 1],
                [row + 1, column],
                [row + 1, column + 1],
                [row, column - 1],
                [row + 1, column - 1]
            ])
        elif case_board.board_matrix[row][column] == 6:
            return([
                [row + 1, column],
                [row, column - 1],
                [row - 1, column],
                [row - 1, column - 1],
                [row + 1, column - 1]
            ])
        elif case_board.board_matrix[row][column] == 7:
            return([
                [row, column + 1],
                [row, column - 1],
                [row - 1, column],
                [row - 1, column - 1],
                [row - 1, column + 1]
            ])
        elif case_board.board_matrix[row][column] == 8:
            return([
                [row, column + 1],
                [row + 1, column],
                [row + 1, column + 1],
                [row - 1, column],
                [row - 1, column + 1]
            ])

class Board(Game):
    def __init__(self, board_type):
        super().__init__()
        self.board_type = board_type
        self.difficulty = game.difficulty
        self.game = game
        self.board_list = []
        self.board_matrix = []

    # creates a list of game.difficulty[0] * game.difficulty[1] length filled with zeroes and, if specified,
    # game.difficulty[2] mines, shuffles it, separates it in game.difficulty[0] rows and appends them to self.board_matrix
    def generate(self, mines_present = False):
        if mines_present == True:
            self.mines = game.difficulty[2]
        self.board_rows = game.difficulty[0]
        self.board_columns = game.difficulty[1]
        self.board_list.clear()
        self.board_matrix.clear()
        self.board_list = [0 for spaces in range(self.board_rows * self.board_columns)]
        if self.mines != 0:
            for index in range(self.mines):
                self.board_list.append(1)
                self.board_list.remove(0)
            random.shuffle(self.board_list)
        board_list_index = 0
        for row in range(self.board_rows):
            board_constructor = []
            for column in range(self.board_columns):
                board_constructor.append(self.board_list[board_list_index])
                board_list_index += 1
            self.board_matrix.append(board_constructor)

    # prints each row in the matrix in a separate line
    def print_matrix(self):
        for row in range(len(self.board_matrix)):
            print(self.board_matrix[row])

class GameLogicBoard(Board):
    def __init__(self, board_type):
        super().__init__(board_type)
        self.mines = 0

class NumberBoard(GameLogicBoard):
    def __init__(self, board_type):
        super().__init__(board_type)
        self.game = game

    # assings values based on which part of the board each cell is, needed for number assignment
    def cell_case_check(self):
        self.board_matrix[0] = [5 for x in self.board_matrix[0]] # top edge
        for row_index in range(self.board_rows - 1): # right edge
            self.board_matrix[row_index][-1] = 6
        self.board_matrix[-1] = [7 for x in self.board_matrix[-1]] # bottom edge
        for row_index in range(self.board_rows - 1): # left edge
            self.board_matrix[row_index][0] = 8
        self.board_matrix[0][0] = 1 # top left
        self.board_matrix[0][-1] = 2 # top right
        self.board_matrix[-1][-1] = 3 # bottom right
        self.board_matrix[-1][0] = 4 # bottom left

    # checks each cell against the specified main board and if it's a mine it checks what case the cell is
    # before incrementing adjacent cells according to the case to avoid errors and negative indexes
    # could probably optimize the case check but i'm not gonna do that rn
    def set_proximity(self, main, cases):
        row_index = 0
        for row in main.board_matrix:
            column_index = 0
            for cell in row:
                if cell == 1:
                    for coordinate in self.adjacency_check(row_index, column_index):
                        self.board_matrix[coordinate[0]][coordinate[1]] += 1
                column_index += 1
            row_index += 1

class DisplayBoard(GameLogicBoard):
    def __init__(self, board_type, actions):
        super().__init__(board_type)
        self.actions = actions

    # same as Board.generate but fills the matrix with spaces instead of zeroes
    def generate(self, mines_present = 0):
        if mines_present != 0:
            self.mines = game.difficulty[2]
        self.board_rows = game.difficulty[0]
        self.board_columns = game.difficulty[1]
        self.board_list.clear()
        self.board_matrix.clear()
        self.board_list = [" " for spaces in range(self.board_rows * self.board_columns)]
        board_list_index = 0
        for row in range(self.board_rows):
            board_constructor = []
            for column in range(self.board_columns):
                board_constructor.append(self.board_list[board_list_index])
                board_list_index += 1
            self.board_matrix.append(board_constructor)

    # creates a string according to the contents of display_board and prints it with correct formatting
    def display(self):
        displayed_board = ""
        row_index = 0
        for row in self.board_matrix:
            displayed_board += f"\n{row_index}  " if len(str(row_index)) < 2 else f"\n{row_index} "
            for cell in row:
                if cell == action_flag.action_type:
                    displayed_board += f"\033[41m \033[37m{cell} \033[0m"
                elif cell == 0:
                    displayed_board += f"\033[40m \033[30;40m{cell} \033[0m"
                elif cell in range(1, 9):
                    displayed_board += f"\033[40m \033[37m{cell} \033[0m"
                elif cell == action_uncertain.action_type:
                    displayed_board += f"\033[44m \033[37m{cell} \033[0m"
                else:
                    displayed_board += f"\033[100m \033[37m{cell} \033[0m"
            row_index += 1
        column_numbers = "    "
        for index in range(game.difficulty[1]):
            column_numbers += f"{index}  " if len(str(index)) < 2 else f"{index} "
        print(column_numbers)
        print(displayed_board)
        print(f"flags remaining: {action_flag.flags_remaining}")

    # reveals all the numbers and mines on the board
    def board_reveal(self):
        displayed_board = ""
        row_index = 0
        for row in self.board_matrix:
            column_index = 0
            displayed_board += f"\n{row_index}  " if len(str(row_index)) < 2 else f"\n{row_index} "
            for cell in row:
                if action_board.board_matrix[row_index][column_index] == action_flag.action_type:
                    displayed_board += f"\033[41m \033[37m{action_board.board_matrix[row_index][column_index]} \033[0m"
                elif main_board.board_matrix[row_index][column_index] == 1:
                    displayed_board += f"\033[41m \033[30mx \033[0m"
                elif number_board.board_matrix[row_index][column_index] == 0:
                    displayed_board += f"\033[40m \033[30;40m  \033[0m"
                elif number_board.board_matrix[row_index][column_index] in range(1, 9):
                    displayed_board += f"\033[40m \033[37m{number_board.board_matrix[row_index][column_index]} \033[0m"
                elif action_board.board_matrix[row_index][column_index] == action_uncertain.action_type:
                    displayed_board += f"\033[40m \033[37m{number_board.board_matrix[row_index][column_index]} \033[0m"
                else:
                    displayed_board += f"\033[41m \033[30mx \033[0m"
                column_index += 1
            row_index += 1
        column_numbers = "    "
        for index in range(game.difficulty[1]):
            column_numbers += f"{index}  " if len(str(index)) < 2 else f"{index} "
        print(column_numbers)
        print(displayed_board)

class Action(Game): # (lawsuit)
    def __init__(self, action_type, main, actions, numbers, display):
        super().__init__()
        self.action_type = action_type
        self.main = main
        self.actions = actions
        self.numbers = numbers
        self.display = display
        self.game = game

    # sets the cell in the specified board to the action_type of the Action object that called the method
    def action(self, row, column):
        self.actions.board_matrix[row][column] = self.action_type
        self.display.board_matrix[row][column] = self.action_type

class Sweep(Action):
    def __init__(self, action_type, main, actions, numbers, display, cases):
        super().__init__(action_type, main, actions, numbers, display)
        self.cases = cases

    # pretty much Action.action but modifies the display board with the contents of the number board instead of the action board
    def clean_sweep(self, row, column):
        if self.actions.board_matrix[row][column] == "f":
            return()
        self.actions.board_matrix[row][column] = self.action_type
        self.display.board_matrix[row][column] = self.numbers.board_matrix[row][column]

    # sweeps the current cells then calls itself on all adjacent cells if the current cell is 0 
    def recursive_sweep(self, row, column):
        if self.numbers.board_matrix[row][column] == 0 and self.actions.board_matrix[row][column] == 0:
            self.clean_sweep(row, column)
            for coordinate in self.adjacency_check(row, column):
                self.recursive_sweep(*coordinate)
        else:
            self.clean_sweep(row, column)
            return()

    # if the flags adjacent to a cell are equal to the number of the cell, calls recursive_sweep on all the blank adjacent cells
    def clear_number(self, row, column):
        adjacent_flags = 0
        adjacent_cells = []
        for coordinate in self.adjacency_check(row, column):
            if self.actions.board_matrix[coordinate[0]][coordinate[1]] == "f": adjacent_flags += 1
            adjacent_cells.append(coordinate)
        if adjacent_flags >= self.numbers.board_matrix[row][column]:
            for coordinate in adjacent_cells:
                self.recursive_sweep(*coordinate)
        else:
            return(print("\ncell has already been swept!\n"))

    # ends the game if the swept cell is a mine, otherwise sets the corresponding action_board cell to the sweep value
    def sweep(self, row, column):
        if self.main.board_matrix[row][column] == 1:
            display_board.board_reveal()
            print("\nyou hit a mine! try again?\n 0: exit\n 1: retry with same settings\n 2: change settings and retry\n")
            game_restart()
        elif self.actions.board_matrix[row][column] == self.action_type:
            self.clear_number(row, column)
        elif self.actions.board_matrix[row][column] == "f":
            print("\ncell is flagged!\n")
        else:
            if self.numbers.board_matrix[row][column] == 0:
                self.recursive_sweep(row, column)
            else:
                self.clean_sweep(row, column)


class Flag(Action):
    def __init__(self, action_type, main, actions, sweep, numbers, display):
        super().__init__(action_type, main, actions, numbers, display)
        self.flags_remaining = main.mines
        self.mines_remaining = main.mines
        self.sweep = sweep

    # flags the specified cell if it's not already a flag or swept, otherwise unflags the cell or does nothing
    def flag(self, row, column):
        if self.actions.board_matrix[row][column] == self.action_type:
            self.actions.board_matrix[row][column] = 0
            self.display.board_matrix[row][column] = 0
            self.flags_remaining += 1
        elif self.actions.board_matrix[row][column] == self.sweep.action_type:
            print("\ncell has already been swept!\n")
        elif self.flags_remaining != 0:
            self.action(row, column)
            self.flags_remaining -= 1
            if self.main.board_matrix[row][column] == 1:
                self.mines_remaining -= 1
        elif self.flags_remaining == 0:
            print("\nno flags remaining! double check your flags!\n")

class Uncertain(Action):
    def __init__(self, action_type, main, actions, sweep, numbers, display):
        super().__init__(action_type, main, actions, numbers, display)
        self.sweep = sweep

    # marks or unmarks the specified cell with "?"
    def mark(self, row, column):
        if self.actions.board_matrix[row][column] == self.action_type:
            self.actions.board_matrix[row][column] = 0
        else:
            self.action(row, column)

# asks for input to decide if to change settings before restarting
def game_restart(retry = True):
    while True:
        if retry == True:
            retry = input("type a number: ")
        try:
            retry = int(retry)
        except:
            print("please input a valid option.")
            continue
        if retry not in range(0, 3):
            print("please input a valid option.")
            continue
        break
    if retry == 0:
        print("\nthanks for playing!\n")
        sys.exit()
    elif retry == 1:
        generate_boards()
        action_flag.mines_remaining = game.difficulty[2]
        action_flag.flags_remaining = game.difficulty[2]
    elif retry == 2:
        random.seed(random.randrange(10))
        game.difficulty = game.set_difficulty()
        generate_boards()
        action_flag.mines_remaining = game.difficulty[2]
        action_flag.flags_remaining = game.difficulty[2]

# instancing the game object that handles difficulty and seed
game = Game()
game.set_seed()
game.difficulty = game.set_difficulty()

# instancing all the necessary boards
main_board = Board("main")
action_board = GameLogicBoard("action")
number_board = NumberBoard("number")
case_board = NumberBoard("case")
display_board = DisplayBoard("display", action_board)

# runs the generate method on all the boards and the methods needed for the number board
def generate_boards():
    main_board.generate(True)
    action_board.generate()
    number_board.generate()
    case_board.generate()
    display_board.generate()
    case_board.cell_case_check()
    number_board.set_proximity(main_board, case_board)

generate_boards()

# instancing all the action objects specifying the names of the boards
action_sweep = Sweep("s", main_board, action_board, number_board, display_board, case_board)
action_flag = Flag("f", main_board, action_board, action_sweep, number_board, display_board)
action_uncertain = Uncertain("?", main_board, action_board, action_sweep, number_board, display_board)

# needed for the input handler
VALID_ACTIONS = ("s", "f", "?")

# first sweep
def first_sweep():
    while True:
        display_board.display()
        print("\nchoose cell to sweep (first one is guaranteed to be a 0)\n")
        user_input = input("input action (row, column; eg. 2, 4): ")
        user_input = user_input.split(", ")
        try:
            user_input[0] = int(user_input[0])
            user_input[1] = int(user_input[1])
        except:
            print("\ninvalid input!\n")
            continue
        if user_input[0] not in range(main_board.board_rows) or user_input[1] not in range(main_board.board_columns):
            print("\ninput is outside of board!\n")
            continue
        if len(user_input) > 2:
            print('\ninvalid input! please type coordinates in format (row, column) eg.: 0, 4\n')
            continue
        while number_board.board_matrix[user_input[0]][user_input[1]] != 0 or main_board.board_matrix[user_input[0]][user_input[1]] == 1:
            random.seed(random.randrange(0, 1000000000))
            generate_boards()
        action_sweep.sweep(*user_input[:2])
        break

first_sweep()

# input handler
while True:
    if action_flag.mines_remaining == 0:
        display_board.board_reveal()
        print("\nyou won! try again?\n 0: exit\n 1: retry with same settings\n 2: change settings and retry\n")
        game_restart()
        first_sweep()
        continue
    #cls() doesn't work through colab
    display_board.display()
    print("\nwhat will you do?\n s = sweep (default if no action is specified)\n f = flag\n ? = uncertain\n") # move to displayer
    user_input = input("input action (row, column, action eg. 2, 4, f): ")
    user_input = user_input.split(", ")
    try:
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
    except:
        print("\ninvalid input!\n")
        continue
    if user_input[0] not in range(main_board.board_rows) or user_input[1] not in range(main_board.board_columns):
        print("\ninput is outside of board!\n")
        continue
    if len(user_input) < 3:
        user_input.append("s")
    elif user_input[2] not in VALID_ACTIONS:
        print("\nplease input a valid action!\n")
        continue
    if user_input[2] == "s":
        action_sweep.sweep(*user_input[:2])
    elif user_input[2] == "f":
        action_flag.flag(*user_input[:2])
    elif user_input[2] == "?":
        action_uncertain.mark(*user_input[:2])