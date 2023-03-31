"""Component 2 (How much) v1
Ask user how much they want to play with and check the input is a valid
integer between 1 and 2. If it is, this amount becomes a balance in their account
"""

balance = int(input("How much do you want to play with? (Must be between 1 and 10) $"))

while not 1<= balance <= 10:
    print("Enter a number between 1 and 10")
    balance = int(input("How much do you want to play with $"))

print(f"You are playing with ${balance}")