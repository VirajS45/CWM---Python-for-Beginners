number = [2, 25, 6, 10, 99]
max_num = number[0]
for num in number:
    if max_num < num:
        max_num = num
print(f"Max Number: {max_num}")

