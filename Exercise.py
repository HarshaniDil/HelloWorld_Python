# Write a program to remove the duplicate in a list

list = [2,2,4,6,3,4,6,1]

for i in list:
    list.count(i)
    if list.count(i)>1:
        list.remove(i)
print(list)

numbers = [2,2,4,6,3,4,6,1]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
