name = ['John','Ishan','Harshani','Mosh']
print(name)
print(name[0:2])
print(name[1:])
print(name[:3])
print(name[2])
print(name[-1])
print(name[-2])
name[1] = 'Dog'
print(name)

number = [15,62,7,3,74]
max = number[0]

for numbers in number:
    if max<numbers:
        max=numbers
print(f"maximum number is {numbers}")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1] =20
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][1])

for row in matrix:
    for item in row:
        print(item)
print("-----------------------------------------")

for column in matrix:
    for item in column:
        print(item)
print('-------------------------------------------------------')

number = [5,2,1,5,7,4]
number.append(20) # Then 20 is added as last index in the array
print(number)

number.insert(0,50) # Then 50 is added as zero index in the array
print(number)

number.insert(1,20) # Then 20 is added as second index in the array
print(number)

number.remove(20) # the first 20 is removed from the list
print(number)

number.remove(20)
print(number)

number.pop() # then last element of the list is removed
print(number)


print(number.index(1)) # index is used for check whether any specifi number in the list
# Then it return the index of the number

# There is another way to check where to find any number is the list
#It return True of False

print(4 in number)
print(50 in number)


print(number.count(5)) # how many times 5 is in the list

number.sort()
print(number)

number.reverse()
print(number)

number2 = number.copy()
print(number2)

number.append(45)
print(number)

print(number2)















