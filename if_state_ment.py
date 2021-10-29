temperature = 25

# if temperature > 30:
#     print("it's very hot day")
# else:
#     print("it is cold")

# if temperature > 30:
#     print("it's very hot day")
# elif temperature > 20:
#     print("It's nice day")
# else:
#     print("it is cold")

# exercise

weight = input("Weight: ")
get_extention = input("(K)g or (L)bs: ").upper()

if get_extention == "K":
    print("Weight in Kg: ", weight)
elif get_extention == "L":
    print("Weight in Liter", weight)
else:
    print("Your unit is not correct")