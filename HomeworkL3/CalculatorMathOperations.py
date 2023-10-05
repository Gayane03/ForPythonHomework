#Create a calculator that will support basic math operations

def AddFunction(number1,number2):
    return number1+number2;

def SubFunction(number1,number2):
    return number1-number2;

def MulFunction(number1,number2):
     return number1*number2;

def DivFunction(number1,number2):
     if number2==0:
       return "Cannot divide by zero";
     else:
       return number1/number2;


print("Options:")
print("Enter 'add' for addition")
print("Enter 'subtract' for subtraction")
print("Enter 'multiply' for multiplication")
print("Enter 'divide' for division")
print("Enter 'quit' to end the program")

inputFunction = input("input opertation name : ");

if  inputFunction=="quit":
    print("-----");
elif inputFunction in ("add", "subtract", "multiply", "divide"):
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if inputFunction == "add":
            print("Result:", AddFunction(number1, number2))
    elif inputFunction == "subtract":
            print("Result:", SubFunction(number1, number2))
    elif inputFunction == "multiply":
            print("Result:", MulFunction(number1, number2))
    elif inputFunction == "divide":
            print("Result:", DivFunction(number1, number2))
else:
        print("Invalid input. Please enter a valid operation.")