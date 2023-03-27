"""LU Yes / No
Puts the code created in v2 into a loop to making coding easier
and more efficient.
"""

show_instructions = ""
while show_instructions != "x":
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
