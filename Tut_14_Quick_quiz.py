name = input("Enter your name > ")
len_name = len(name)
if len_name < 3:
    print("name must be at least 3 characters")
elif len_name > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")

