import random
#import random: Imports Python's built-in random module to use its functions for generating random numbers,
# which is essential for simulating the slot machine's spin.
MAX_LINES = 4
MAX_BET = 200
MIN_BET = 1

ROWS = 3
COLS = 3
#MAX_LINES = 4: Defines the maximum number of lines a player can bet on.
#MAX_BET = 200: Sets the maximum amount a player can bet on each line.
#MIN_BET = 1: Sets the minimum amount a player can bet on each line.
#ROWS = 3 and COLS = 3: Define the dimensions of the slot machine, i.e., 3 rows and 3 columns.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#symbol_count: Defines how many times each symbol appears in the slot machine's "reel".
# For example, symbol "A" appears twice, "B" four times, etc.
#symbol_value: Assigns a payout value to each symbol. If a player wins with symbol "A", 
# they win 5 times their bet amount per line, "B" gives 4 times, etc.
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
#hecks if the player has won on any of the selected lines.
#columns: Represents the current symbols in each column after the spin.
#lines: The number of lines the player has bet on.
#bet: The amount bet per line.
#values: The payout values for each symbol.
#It iterates through each line to check if all symbols in that line are the same. If they are, 
# he winnings are calculated by multiplying the bet by the value of the symbol.
#winnings: Accumulates the total winnings.
#winning_lines: Stores the lines where the player won.

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
#Simulates the spinning of the slot machine.
#rows and cols: Dimensions of the slot machine.
#symbols: A dictionary of available symbols and their counts.
#It first creates a list of all symbols based on their frequency (all_symbols). 
#Then, for each column, it randomly selects a symbol (using random.choice), removes it from the list to avoid duplicates, and builds each column.
#columns: The final slot machine result, with each column containing a list of symbols.

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
#Asks the player to input a deposit amount.
#It ensures that the input is a valid number greater than zero.
# If not, it keeps asking the player until a valid input is provided.

def deposit():
    while True:
        amount = input("What would you like to deposit? R")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount
#Prompts the player to input the number of lines they want to bet on (between 1 and MAX_LINES).
#It validates that the input is within the allowed range.

def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? R")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between R{MIN_BET} - R{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount
#Asks the player how much they want to bet per line.
#It checks that the bet is between MIN_BET and MAX_BET

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: R{balance}")
        else:
            break

    print(
        f"You are betting R{bet} on {lines} lines. Total bet is equal to: R{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won R{winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
#Represents one spin of the slot machine.
#It first asks the player how many lines they want to bet on and how much to bet per line.
#If the total bet exceeds the player's balance, it prompts the player to input a valid amount.
#It then simulates the spin, prints the results, calculates the winnings, and returns the net result (winnings minus the total bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is R{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with R{balance}")


main()