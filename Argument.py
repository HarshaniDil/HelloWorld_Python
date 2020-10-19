def new_message(f_name,l_name):
    print(f"Hai {f_name} {l_name}")
    print("This is the message body")
    print("Thank you")

new_message("John",l_name="Smith") #keyword argument

#count(price=10, discount=5, total=8)

def square(number):
    return number*number

print(square(3))