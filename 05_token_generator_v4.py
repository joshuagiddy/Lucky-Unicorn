"""Component 3 v4 random token generator
Calculates percentages into getting %5 chance of Unicorn, %30 percent chance
of getting donkey and %65 percent chance of getting either zebra or horse"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE


#Test Loop
for item in range(10):
    number = random.randint(1,100)


#adjust balance
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1
    else:
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5
        else:
            token = "horse"
            balance -= .5


    print(f"Token: {token}, Balance: {balance:.2f}")

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")


