# 1
def print_name():
    print("TasiNCoder")

print_name()


# 2
def print_two_args(a, b):
    print(a)
    print(b)

print_two_args(10, 20)


# 3
def print_unknown_args(*args):
    print(args)

print_unknown_args(1, 2, 3, 4, 5)


# 4
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_kwargs(name="Akshat", age=21, course="CSE")


# 5
def print_list(my_list):
    for item in my_list:
        print(item)

print_list([10, 20, 30, 40])


# 6
def max_of_four(a, b, c, d):
    return max(a, b, c, d)

print(max_of_four(10, 25, 5, 40))


# 7
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4, 5]))


# 8
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_list([1, 2, 3, 4]))


# 9
def check_range(num, start, end):
    return start <= num <= end

print(check_range(5, 1, 10))


# 10
def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(7)
