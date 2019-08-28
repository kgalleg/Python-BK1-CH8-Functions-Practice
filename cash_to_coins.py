# #Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

# dollarAmount = 8.69

# piggyBank = {
#     "pennies": 0,
#     "nickels": 0,
#     "dimes": 0,
#     "quarters": 0
# }

# # Your magic Python code here
# That should produce the following output.

# >>> print(piggyBank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }


def calc_dollars():

    dollar_amount = 8.69

    piggy_bank = {
        "quarters":0,
        "dimes":0,
        "nickels":0,
        "pennies": 0
    }

    cents_amount = dollar_amount *100
    q_quarters = int(cents_amount/25)

    piggy_bank["quarters"] = q_quarters
    cents_amount = (cents_amount % 25)
    d_dimes = int(cents_amount/10)

    piggy_bank["dimes"] = d_dimes
    cents_amount = (cents_amount % 10)
    n_nickels = int(cents_amount/5)

    piggy_bank["nickels"] = n_nickels
    cents_amount = (cents_amount % 5)
    p_pennies = int(cents_amount)

    piggy_bank["pennies"] = p_pennies


    print('quarters',piggy_bank)


calc_dollars()







#another Way to do the same thing as above

# dollarAmount = 8.69

# piggyBank = {
#     "pennies": 0,
#     "nickels": 0,
#     "dimes": 0,
#     "quarters": 0
# }

# def convert_to_change(dollarAmount, quarters, dimes, nickels, pennies):
#     piggyBank["pennies"] = int((dollarAmount - (dollarAmount - pennies*.01))/.01)
#     piggyBank["nickels"] = int((dollarAmount - (dollarAmount - nickels*.05))/.05)
#     piggyBank["dimes"] = round((dollarAmount - (dollarAmount - dimes*.1))/.1)
#     piggyBank["quarters"] = (dollarAmount - (dollarAmount - quarters*.25))/.25

#     print(piggyBank)

# convert_to_change(dollarAmount, 34, 1, 1, 4)