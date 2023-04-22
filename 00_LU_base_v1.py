"""LU Base component
Components added after they have been created and tested"""

import random

# Functions go here...
def yes_no(question_text):
    while True:

        # Ask the user if they have played before.
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'.
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'.
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error.
        else:
            print("error, please answer 'yes' or 'no'")

#function to display instructions
def instructions():
    print("*** How To Play ***")
    print()
    print("The rules of the game will go here")
    print("Program continues")
    print()

#number checking function
def num_check(question, low, high):
    error = "That was not valid\n" \
            "Please enter a number between {} and {}\n".format(low,high)

    #keep asking until a valid amount
    while True:
        try:
            #ask for amount
            response = int(input(question))

            #check if number is in required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def generate_token(BALANCE):

    rounds_played = 0
    play_again = ""

    while play_again != "x":
        rounds_played += 1
        number = random.randint(1, 100)

        if 1 <= number <= 5:
            token = "unicorn"
            BALANCE += 4
        elif 6 <= number <= 36:
            token = "donkey"
            BALANCE -= 1
        else:
            if number % 2 == 0:
                token = "zebra"
                BALANCE -= 0.5
            else:
                token = "horse"
                BALANCE -= 0.5

        print(f"Rounds {rounds_played}, Tokens: {token}, Balance: ${BALANCE:.2f}")
        if BALANCE < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round\n<enter> to play"
                               " again or 'X' to exit ").lower()
        print()
    return BALANCE


# Main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")



starting_balance = num_check("How much would you like to pay with? $", 1, 10)
print(f"You are plaing with ${starting_balance}")

starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You have started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print("Goodbye")
