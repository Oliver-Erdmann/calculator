def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("add")
print("subtract")
print("multiply")
print("divide")

while True:
    choice = input("Which one")
    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 'add':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == 'subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == 'multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == 'divide':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Want to do it again? (Y/N)")
        if next_calculation == "N":
            break
    else:
        print("Invalid Input")