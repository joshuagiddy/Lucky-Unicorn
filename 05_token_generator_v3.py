"""Component 3 random tokens v3
Generates user balance on the generated tokens in random order"""

import random

tokens = ["unicorn", "zebra", "donkey", "horse"]
balance = 100

#Testing loop
for item in range(100):
    token = random.choice(tokens)
    print(token, end='\t')

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    print(f"Token: {token}, Balance: ${balance}")


