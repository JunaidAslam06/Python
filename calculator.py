def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice= input("Choose what to do from 1-4: ")
number1= float(input("Enter first number: "))
number2= float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {add(number1, number2)}")
elif choice == '2':
    print(f"Result: {subtract(number1, number2)}")
elif choice == '3':
    print(f"Result: {multiply(number1, number2)}")
elif choice == '4':
    print(f"Result: {divide(number1, number2)}")
else:
    print("Invalid choice")