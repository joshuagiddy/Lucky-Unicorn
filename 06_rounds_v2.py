"""Component 4 - game mechanics and looping v2
tokens are allocated from a random radint of 1, 100.
Gives us feedback on our balance and number of rounds.
"""
import random

# Main routine
TEST_AMOUNT = 5
BALANCE = TEST_AMOUNT

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

print("Thanks for playing")
print(f"You have started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${BALANCE:.2f}")
print("Goodbye")
        


