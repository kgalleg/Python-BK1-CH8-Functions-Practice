# def create_person(first_name, last_name, age, occupation):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "age": age,
#         "occupation": occupation,
#     }

# melissa = create_person("Melissa", "Bell", 25, "Software Developer")





# KEY                      #Value
running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


def run(name):
        # for value in running_kids:
            print( f"{name} ran like a cheetah!")

for kid in running_kids:
    run(kid)
    


def swing(name):
    for value in name:
            print( f"{value} was swinging in the park!")

print(swing(swinging_kids))


def slide(name):
      for value in name:
            print( f"{value} slid down the slide!")

print(slide(sliding_kids))


def hide_and_seek(name):
      for value in name:
            print( f"{value} was playing hide and seek!")

print(hide_and_seek(hiding_kids))