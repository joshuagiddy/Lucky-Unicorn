"""Component 2 (How much) v1
Use try/accept and pull error message out of the loop
"""

error = "Please enter a whole number between 1 and 10\n"
valid = False
while not valid:
    try:
        balance = int(input("How much do you want to play with? (Must be between 1 and 10) $"))

        if 0 < balance <= 10:
            print(f"You are playing with ${balance}")
        else:
            print(error)

    except ValueError:
        print(error)


