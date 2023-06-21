i = 0
car_start = False
while i < 1:
    user_control = input('>')
    command = user_control.lower()
    if command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit''')

    elif command == 'start':
        if not car_start:
            print('Car started...Ready to go!')
            car_start = True
        else:
            print('Car is already started...')

    elif command == 'stop':
        if not car_start:
            print('Car is already stopped.')
        else:
            print('Car stopped.')
            car_start = False

    elif command == 'quit':
        print('---Game Quitted---')
        break

    else:
        print('Sorry I dont understand that... (help)')






