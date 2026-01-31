try:
    num = int(input("Enter a number: "))
    if num == 0:
        raise Exception("Division by zero is not allowed.") 
    result = 10 / num
    print(f"Result is: {result}")
except ValueError:
    print("Invalid input!")
except Exception:
    print("Invalid input!")
finally:
    print("akshat") 