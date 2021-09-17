# Adds two numbers
def adder(a,b):
    return a+b

# Divides two numbers
def divider(a,b):
    if b == 0:  
        return -1
    else:
        return a/b

# Multiply two numbers
def multiplier(a,b):
    return a*b


print("Hello! Please write two numbers you want to add")
a = int(input("First Number:"))
b = int(input("Second Number:"))


print(adder(a,b))
print(divider(a,b))
print(multiplier(a,b))
