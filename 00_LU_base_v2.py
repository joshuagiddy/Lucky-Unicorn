"""LU Base component
Components added after they have been created and tested"""


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

# Main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")



user_balance = num_check("How much would you like to pay with? $", 1, 10)
print(f"You are plaing with ${user_balance}")
