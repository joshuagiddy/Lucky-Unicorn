"""Component 3 random tokens v1
Generates random tokens in random order"""

import random

tokens = ["unicorn", "zebra", "donkey", "horse"]

#Testing loop
for item in range (20):
    token = random.choice(tokens)
    print(token)