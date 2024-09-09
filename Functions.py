def printer(name, place):
    print(name, place)
printer("Tawseef", "Mymensingh")
printer("Ashrafi", "Khulna")
def function2(birthday, birth_month, birth_year):
    print(birthday, birth_month, birth_year)
function2(19, 10, 2010)
def weather(number):
    if number == 1:
        print("Summer in Bangladesh takes place between March, April and May")
    elif number == 2:
        print("Moonsoon in Bangladesh takes place between June, July and August")
    elif number == 3:
        print("Autumn in Bangladesh takes place between September and October")
    elif number == 4:
        print("Winter in Bangladesh takes place between November, December and January")
    elif number == 5:
        print("Spring in Bangladesh takes place between February")
print("Press number to know about seasons (1 = summer, 2 = moonsoon 3 = autumn, 4 = winter, 5 = spring)")
num = int(input("Enter number: "))
weather(num)
result = 0
def add(a, b):
    return a + b
def substract(c, d):
    return c - d
def multiply(e, f):
    return e * f
def divide(g, h):
    return g / h
print("Choose option (a/b/c/d)")
print("a is Add")
print("b is substract")
print("c is Multiply")
print("d is Divide")
choice = input("Enter choice: ")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(choice)
if choice == "a" :
    result1 = add(number1, number2)
    print(result1)  
elif choice == "b" :
    result2 = substract(number1, number2)
    print(result2)
elif choice == "c":
    result3 = multiply(number1, number2)
    print(result3)
elif choice == "d":
    result4 = divide(number1, number2)
    print(result4)
else:
    print("Invalid option")