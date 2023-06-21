user_weight = int(input("Weight: "))
user_unit = input("(L)bs or (K)g: ")

if user_unit.lower() == "l":
    converted_weight = 0.45 * user_weight
    print(f"You are {converted_weight} kilos")
elif user_unit == "k":
    converted_weight = user_weight / 0.45
    print(f"You are {converted_weight} pounds")
else:
    print("Invalid Unit")
