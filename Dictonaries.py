customer = {
    "name": "Harshani Dilrukshi",
    "age": 30,
    "is_verified" : True

}

print(customer["name"])
print(customer['age'])
print(customer.get("name"))
print(customer.get("birthday","May 20 1996"))

customer["name"] = "Imasha Madusani"
print(customer["name"])


print("--------------------------------------------------------------------")


phone_no = input('phone: ')
number= {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
    }
output = " "
for ch in phone_no:
    output += number.get(ch,"!") + " "

print(output)

print("---------------------------------------------------")















