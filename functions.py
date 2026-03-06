# =========================================
# PYTHON FUNCTIONS - BASIC TO ADVANCED GUIDE
# Everything is explained using comments
# =========================================


# -----------------------------------------
# 1. What is a Function?
# -----------------------------------------
# A function is a reusable block of code
# that performs a specific task.
#
# Syntax:
#
# def function_name(parameters):
#     code
#     return value


def greet():
    # This function prints a greeting
    print("Hello, welcome to Python functions!")


greet()  # calling the function



# -----------------------------------------
# 2. Function with Parameters
# -----------------------------------------

def greet_user(name):
    # name is a parameter
    print("Hello", name)


greet_user("Rahul")
greet_user("Aman")



# -----------------------------------------
# 3. Function with Return Value
# -----------------------------------------

def add_numbers(a, b):
    # return sends value back to caller
    result = a + b
    return result


sum_result = add_numbers(5, 10)
print("Sum:", sum_result)



# -----------------------------------------
# 4. Default Parameters
# -----------------------------------------

def greet(name="Guest"):
    # If no argument is passed
    # default value will be used
    print("Hello", name)


greet("Rohit")
greet()



# -----------------------------------------
# 5. Multiple Parameters
# -----------------------------------------

def introduce(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


introduce("Aman", 22, "Delhi")



# -----------------------------------------
# 6. Keyword Arguments
# -----------------------------------------

def student(name, age):
    print("Name:", name)
    print("Age:", age)


# Order does not matter with keywords
student(age=21, name="Ravi")



# -----------------------------------------
# 7. Arbitrary Arguments (*args)
# -----------------------------------------

def add_all_numbers(*numbers):
    # *args allows multiple inputs
    total = 0

    for num in numbers:
        total += num

    print("Total:", total)


add_all_numbers(1, 2, 3)
add_all_numbers(10, 20, 30, 40)



# -----------------------------------------
# 8. Arbitrary Keyword Arguments (**kwargs)
# -----------------------------------------

def student_info(**data):
    # **kwargs accepts key=value pairs
    for key, value in data.items():
        print(key, ":", value)


student_info(name="Rahul", age=20, city="Mumbai")


# Program to add two numbers using a function

def add_numbers(a, b):
    # This function takes two numbers as input
    # and returns their sum
    result = a + b
    return result

# taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# calling the function
sum_result = add_numbers(num1, num2)

print("Sum is:", sum_result)


# Program to check if a number is even or odd using function
def check_even_odd(number):
    # % is modulus operator
    # it returns remainder
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))

result = check_even_odd(num)

print("The number is:", result)


