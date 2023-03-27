"""LU Yes / No
simplifies the input by converting it to the lower case. Also excepts y or n as
abbreviation. Prints result of user choice as well as input - for testing"""

# Ask the user if they have played before.
show_instructions = input("Have you played this game before?:").lower()
#If they say yes, output 'Program Continues'.
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")
#If they say no, output 'Display Instructions'.
elif show_instructions == "no" or show_instructions == "n":
    print("Display Instructions")
#Otherwise - show error.
else:
    print("error, please answer 'yes' or 'no'")

print(f"You entered '{show_instructions}'")
