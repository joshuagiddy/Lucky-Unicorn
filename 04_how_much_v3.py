"""Component 2 (How much)
Chaning v3 into a function
Also need to change user_balance to more generic variable name 'response' and to
change the condition and position of the number comparison into the loop
to make the function recyclable"""

def num_check(question, low, high):
    error = "That was not valid\n" \
            "Please enter a number between {} and {}\n".format(low, high)

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


#Main routine
user_balance = num_check("How much would you like to pay with? $", 1, 10)
print(f"You are plaing with ${user_balance}")

