temp = 28
if temp>35:
    print('Hot day')
elif temp >25:
    print('Normal day')
else:
    print('Cold day')

name = input('What is your name? ')
if len(name) < 3:
    print('name must be at least 3 characters')
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print('name looks good!')

weight = input("Weight: ")
L_or_K = input("(L)bs or (K)g: ")

if L_or_K == 'l' or L_or_K=='L':
    weight = int(weight) * 0.4
    print(f'You are {weight} kilos')

elif L_or_K == 'k' or L_or_K=='K':
    weight = int(weight) / 0.4
    print(f'You are {weight} pounds')

