try:
    age = int(input("Age: "))
    income = 5000
    results = income/age
    print(results)
    
except ZeroDivisionError:
    print("age is not zero")

except ValueError:
    print("Invalide input")