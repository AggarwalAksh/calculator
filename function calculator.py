def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def times(x,y):
    return x * y
def divide(x,y):
    return x / y
print("Please select an option")
print("1.add")
print("2.subtract")
print("3.times")
print("4.divide")
while True:

     choice = input("Choose between 1,2,3,4")
     print(choice)
     if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter a number"))
        num2 = float(input("Enter another number"))
        if choice == '1':
            print(choice)
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', times(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))

