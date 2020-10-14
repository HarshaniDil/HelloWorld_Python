i = 1
while i<=5:
    print(i)
    i = i+1
print('Done')

x = 1
while x<5:
    print('*' * x)
    x = x+1

num = 9
chance = 1
while chance <= 3:
    guessNum = int(input('Guess: '))
    chance = chance + 1

    if guessNum == num:
        print('You win!')
        break
else:
    print('Sorry you failed')

Started = False
while True:
    command = input(">").upper()
    if command == 'HELP':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command == 'START':
        if Started:
            print("Car is already started")
        else:
            Started = True
            print('car started... Ready to go!')
    elif command == 'STOP':
        if not Started:
            print('car is already stopped')
        else:
            Started = False
            print("Car is already stopped")
    elif command == 'QUIT':
        break 
    else:
        print("I don't understand that.......")





