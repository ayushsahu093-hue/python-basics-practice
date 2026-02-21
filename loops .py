# Hi these file is only made for begginers 
# while loops basic syantax 
# while condition:
# statement 
# # Print numbers from 1 to 10 using a while loop
num = 1

while num <= 10:
    print(num)
    num += 1
# Print odd numbers from 1 to 20 using a while loop
num = 1

while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1
#Find the factorial of a number using a while loop
number = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print("Factorial =", factorial)

 #Calculate the sum of digits of a number using a while loop
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("Sum of digits =", sum_of_digits)

# Keep asking the user to enter a number until they enter 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter a number (0 to stop): "))

print("Program ended.")

#Reverse a number using a while loop
number = int(input("Enter a number: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reversed number =", reverse)

# these below questions are use for loops 
# Print numbers from 1 to 10 using a for loop
# for i in range(1, 11):
#     print(i)

# Print even numbers between 1 and 20 using a for loop
for i in range(2, 21, 2):
    print(i)

#rint the multiplication table of 5 using a for loop
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# Find the sum of numbers from 1 to 100 using a for loop
sum = 0
for i in range(1, 101):
    sum = sum + i

print("Sum =", sum)

# Print numbers from 10 to 1 (reverse order) using a for loop
for i in range(10, 0, -1):
    print(i)

# Count how many numbers between 1 and 50 are divisible by 3
count = 0

for i in range(1, 51):
    if i % 3 == 0:
        count = count + 1

print("Total numbers divisible by 3 =", count)


