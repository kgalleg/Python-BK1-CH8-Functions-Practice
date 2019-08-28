# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.

# piggyBank = {
#     "pennies": 342,
#     "nickels": 9,
#     "dimes": 32
# }
# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

# Given the coins shown above, the output would be 7.07 when you call calc_dollars()


def calc_dollars():
    piggy_bank = {
        "quarters":143,
        "dimes":22,
        "nickels":10,
        "pennies": 48
    }

    total_quarters = piggy_bank["quarters"] * .25
    total_dimes = piggy_bank["dimes"] * .10
    total_nickels = piggy_bank["nickels"] * .05
    total_pennies = piggy_bank["pennies"] * .01

    dollar_amount = total_pennies + total_nickels + total_dimes + total_quarters

    print('$',dollar_amount)

calc_dollars()






#I wasn't sure how to do it this way below...
    # for key, value in piggyBank.items():
    #     if key == "quarters":
    #         dollars += (value * .25)
    #     if key == "dimes":
    #         dollars += (value * .10)
    #     if key == "nickels":
    #         dollars +=(value * .05)
    #     if key == "pennies":
    #         dollars += (value * .01)



