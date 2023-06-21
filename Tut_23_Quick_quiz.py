numbers = [2, 4, 7, 8, 2, 0, 3, 2, 8, 2, 7, 9, 2]
non_duplicate = []
for number in numbers:
    exists = non_duplicate.count(number)
    if exists == 0:
        non_duplicate += [number]
print(non_duplicate)

