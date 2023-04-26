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


# function to display instructions
def instructions():
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount you want to play with between 1 and 10 dollars")
    print()
    print("It cost $1 to play each round but depending on what you win,"
          "you could earn some money back. These are the payment amounts:\n"
          "\tUnicorn: $5 (Increase by $4)\n"
          "\tHorse: 0.50 (Decrease by $0.50)\n"
          "\tZebra: 0.50 (Decrease by $0.50)\n"
          "\tDonkey: 0.00 (Decrease by $1.00)\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with"
          "more money than you started with\n")
    print("*" * 50)
    print()


# number checking function
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


def generate_token(balance):

    rounds_played = 1
    play_again = ""

    while play_again != "x":
        print(f"Round {rounds_played}\n")
        rounds_played += 1
        number = random.randint(1, 100)

        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations you get a Unicorn"))
            print()
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Bad lucky, you get a donkey"))
            print()
        else:
            if number % 2 == 0:
                balance -= 0.5
                print(formatter("Z", "Bad lucky, you get a zebra"))
                print()
            else:
                balance -= 0.5
                print(formatter("H", "Bad luck, you got a horse"))
                print()

        print(f"Your balance is now ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have ran out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round\n<enter> to play"
                               "again or 'X' to exit ").lower()
        print()
    return balance


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine go here...
print(formatter("-", "Welcome to the lucky Unicorn Game"))
print()
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")


starting_balance = num_check("How much would you like to pay with? $", 1, 10)
print(f"You are playing with ${starting_balance:.2f}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You have started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
