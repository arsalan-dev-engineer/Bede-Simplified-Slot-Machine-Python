
import random
from prettytable import PrettyTable

# creating a spin_game function
spin_game = PrettyTable()
# column names
spin_game.field_names = ["Spin Num.", "Spins", "Stake Amount", "Win Amount", "Total Balance"]
# random library will select an item from the win_combinations list
win_combinations = ["*P*", "AAA", "BBB", "PPP", "ABP", "*AB"]
deposit_amount = 0
# each spin turn will increment
spin_num = 0


def main():
    '''this function is the main menu, the user can play the game as many times and they can leave whenever they want'''
    while True:
        print("\n---------- Bede Game -----------------------------------------\n")
        print("Welcome to Bede Spinning Game.\nSelect an option:\n")
        # try will be used for exception handling
        try:
            choice = int(input("1. Play Spinning Game\n" +
                               "2. Exit Game\n"))
            # will call the choice function is user inputs 1
            if choice == 1:
                opening_balance()

            # program will end if user inputs 2
            elif choice == 2:
                print("Goodbye!\n")
                break

            # if user presses any numbers that are not 1 or 2, console will print below
            elif choice != 1 or 2:
                print("Please select options: 1 or 2\n")

        except ValueError:
            # program will print onto console instead of returning an error and ending program
            print("Please select options: 1 or 2\n")


def opening_balance():
    '''this function will collect an input from the user and will use the input as the opening balance'''
    global deposit_amount

    da = float(input("\nPlease deposit monday you would like to play with: "))
    deposit_amount += da
    # calling the spin function
    spin()


def spin():
    '''this function is used to execute calculations'''
    
    # defining global variables so they can be used outside the function
    global deposit_amount
    global spin_num

    # while loop will continue as long as the condition is true
    while deposit_amount > 0:
        try:
            sa = float(input("\nEnter stake amount: "))
            # deposit minus stake amount
            deposit_amount -= sa

            # random library will pick an item from the win_combinations list
            c = random.choice(win_combinations)
            win_amount = 0

            if c == "*P*":
                # winning amount formula
                wa = (0 + 0.8 + 0) * 10
                # win amount is stake amount + winning amount
                win_amount = sa + wa
                # increment by 1 for spin number
                spin_num += 1
                
            elif c == "AAA":
                wa = (0.4 + 0.4 + 0.4) * 10
                win_amount = sa + wa
                spin_num += 1
            
            elif c == "BBB":
                wa = (0.6 + 0.6 + 0.6) * 10
                win_amount = sa + wa
                spin_num += 1

            elif c == "PPP":
                wa = (0.8 + 0.8 + 0.8) * 10
                win_amount = sa + wa
                spin_num += 1

            elif c == "ABP":
                print("No matching symbols")
                spin_num += 1

            elif c == "*AB":
                print("No matching symbols")
                spin_num += 1

            else:
                break
            
            # balance will increment winnings
            deposit_amount += win_amount

            if deposit_amount < 0:
                deposit_amount == 0
                # will return a 0 string if total balance is less than 0
                spin_game.add_row([f"{spin_num}", f"{c}", f"${sa:.2f}", f"${win_amount:.2f}", "$0.00"])
            else:
                # below will add rows to the prettytable function
                spin_game.add_row([f"{spin_num}", f"{c}", f"${sa:.2f}", f"${win_amount:.2f}", f"${deposit_amount:.2f}"])

            print()
            # printing spin_game prettytable
            print(spin_game)
            print()

            # error handling, if user enters a string, below exception will be raised
        except ValueError:
            print("Input Money only!")

    # reseting variables to 0 after game has ended
    deposit_amount = 0
    spin_num = 0
    # removing all rows from the spin_game function
    spin_game.clear_rows()
    
    print("\n---------- Game over! ----------------------------------------\n")
    print("\nReturning to main menu\n")
    

# program will begin with this function
main()