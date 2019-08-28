#Python Functions Book 1 Chapter 8

# Python functions are the same as JavaScript functions, but the syntax is different and white space matters.

# Let's say that again: WHITE SPACE MATTERS.

# Remember how we hounded you about proper formatting in the client side course? Now, you have to do it for real or your code won't work. When writing a function You must indent the contents of the function.

# Look at how the same function is written in the two different syntaxes.

# const createPerson = (firstName, lastName, age, occupation) => {
#     return {
#         firstName,
#         lastName,
#         age,
#         occupation
#     }
# }

# melissa = createPerson("Melissa", "Bell", 25, "Software Developer")


# Function and variable names are snake case instead of camel case
def create_person(first_name, last_name, age, occupation):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation,
    }

melissa = create_person("Melissa", "Bell", 25, "Software Developer")

