conditional statement 
syntax - if (condition): , elif(conditional), else :
it is work as 
if (condition):
    # statement 1
elif(condition):
    # statement 2 
else :
    # statement 3 
 example 1 
 write a program to check user is adult or not 
age = int(input("Enter your age:"))
if(age>=18):
    print("adult")
elif(age>=10):
    print("genz")
else:
    print("child")

example 2 
write a program in which have to give grade to student 
marks = int(input("enter your marks ="))
if(marks==100 or marks>=90):
    print("your grade is A ", marks)
elif(marks>= 80):
    print("your grade is B ", marks)
elif(marks>= 70):
    print("your grade is C ", marks)
elif(marks>= 50):
    print("your grade is D ", marks)
else :
    print(" your are fail ")

write a program to find the gratest number between 3 number which isenter by the user 
num1 = int(input(" Enter your 1st no : "))
num2 = int(input(" Enter your 2nd no : "))
num3 = int(input(" Enter your 3rd no : ")) 
if (num1 > num2 and num1> num3):
    print("your first number is greater :", num1 )
elif (num1 == num2 == num3 ):
        print (" all numbers are same ")
elif (num2 > num1 and num2> num3):
         print("your second  number is greater :", num2 )
else:
         print(" 3 number is the gratest no :", num3)    

wap program to find the multiple of 7 
num1 = int(input(" Enter your number : "))
if (num1%7==0):
    print(num1,"this  number is divisible of 7 ")
else :
    print(num1,"This number is not divisible by 7")
print("thank you for using")

# write a to find odd and even 
num = int(input(" Enter your number :"))
if(num%2==0):
    print(" this is even number ",num)
else:
    print("this number is odd", num )
print(" now you can code by your self, thank you ")

# login system 
username = input("enter your username:")
password = input("Enter your password:")
username1 = " ayush@123"
password1 =  "123456722"
if (username == username and password == password1 ):
    print("login sucessfull")
else :
    print("Invalid Credentials")

# discount  calculator 
val= int(input(" enter the shopping amount = "))
if(val >1000):
    finalval = val - 100
    print(" you are lucky yout got discount")
    print("final value is =", finalval)
else :
    print(" no discount ")
    print("final value = ", val)
