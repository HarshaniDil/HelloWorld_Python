def findmax(numbers):

    maximum = numbers[0]
    for i in numbers:
        if i > maximum:
            maximum = i
    return maximum


