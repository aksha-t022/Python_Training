# Q1
print("Q1 ArithmeticError Example")
try:
    result = 10 / 0  # ZeroDivisionError (subclass of ArithmeticError)
except ArithmeticError as e:
    print("ArithmeticError occurred:", e)

print("\n" + "="*50 + "\n")

# Q2
print("Q2 ValueError Example")
try:
    num = int("abc")  # Invalid conversion
except ValueError as e:
    print("ValueError occurred:", e)

print("\n" + "="*50 + "\n")

# Q3
print("Q3 Handling ArithmeticError")
try:
    x = 10 / 0
except ArithmeticError:
    print("Handled an ArithmeticError!")

print("\n" + "="*50 + "\n")

# Q4
print("Q4 Handling ValueError")
try:
    num = int("hello")
except ValueError:
    print("Handled a ValueError!")

print("\n" + "="*50 + "\n")

# Q5
print("Q5 Handling multiple exceptions in one try")
try:
    num = int("abc")  # ValueError
    result = 10 / 0   # ZeroDivisionError
except (ValueError, ArithmeticError) as e:
    print("Handled an exception:", e)

print("\n" + "="*50 + "\n")

# Q6
print("Q6 Calculator with exception handling")
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            print("Result:", num1 / num2)
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Error! Division by zero.")
    except Exception as e:
        print("An unexpected error occurred:", e)

calculator()

print("\n" + "="*50 + "\n")

# Q7
print("Q7 Calculator with finally block")
def calculator_finally():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            print("Result:", num1 / num2)
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Error! Division by zero.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("Operation complete!")

calculator_finally()

print("\n" + "="*50 + "\n")

# Q8
print("Q8 Try, except, else for division")
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter numbers only.")
else:
    print("Division successful! Result =", result)

print("\n" + "="*50 + "\n")

# Q9
print("Q9 Raise a ValueError")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print("ValueError occurred:", e)

print("\n" + "="*50 + "\n")

# Q10
print("Q10 Nested Try Except")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Inner Exception: Division by zero!")
except ValueError:
    print("Outer Exception: Invalid input! Enter numeric values.")
