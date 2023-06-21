phone = input('Phone: ')
num_text = ""
numbers = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}
for num in phone:
    num_text += numbers.get(num) + ' '
print(num_text)
