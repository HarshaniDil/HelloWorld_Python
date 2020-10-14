for item in 'python':
    print(item)

for item in range(10):
    print(item)

for item in ['Ishan', 'Mosh', 'Me']:
    print(item)

for item in range(4,9):
    print(item)

for item in range(5,10,2):
    print(item)

cost =0
for price in [10,20,30]:
    cost +=price
print(cost)

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers = [5,2,5,2,2]

for star in numbers:
    print('x' * star)
print('---------------------------------------')
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output +='x'
    print(output)