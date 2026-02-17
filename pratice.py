# Type finding 
name = " ayush sahu"
age = 25
mobile_no = 123456789
roll_no = True 
print(type(name)) #output will be <class 'str' >
print(type(age)) #output will be <class 'int'>
print(type(roll_no))#output will be <class 'bool'>

write a program to sum 2 no  :
a = int(input("Enter your 1st no: "))
b = int(input("Enter your 2nd no: "))
print("Sum =", a + b)
# Always make sure that indentation is correct 

arthmetic operator ( +,-,*,/,%)
#write a program to add the sum of 2 no 
a = int(input(" Enter your 1st number :"))
b = int(input(" Enter your 2nd number :"))
print("sum = " , a + b) # dont forget comma 

write a program to add the sum of 3 no 
a = int(input(" Enter your 1st no :"))
b = int(input(" Enter your 2nd no :"))
c = int(input(" Enter your 3rd no :"))
print(" Sum of 3 no are :" , a + b + c) # dont forget comma and gives proper indention 


# write a program to give the multiple of 2 number 
a = int(input(" Enter your 1st no :"))
b = int(input(" Enter your 2nd no :"))
print("Multiply of 2 Numbers are" , a*b)


#write a program to multiple 3 number 
a = int(input(" Enter your 1st no :"))
b = int(input(" Enter your 2nd no :"))
c = int(input("Enter your 3rd no :"))
print(" Multiple of 3 numbers are", a*b*c)

#realtional operator 
write a program to check number using assingment operator 
a = 3 
b = 4 
print (a!=b) # true 
print (a==b)#false
print(a>=b)#false
print(a<=b)#true 
print(a>b)#false 
print(a<b)#true 

#write a program to check user is eligible for driving or not
age = int(input(" Enter your age :"))
if(age>=18): # realtional operators 
    print("you can drive")
else:
    print("you cannot drive a car")
 
 
#write a program to check grade of student using marks as input
marks = int(input( " Enter your marks : "))
if(marks == 100 or marks >= 95):
    print(" your grade is A+")
if(marks>= 80):
    print(" your grade is A")
if(marks>=70):
    print(" your grade is B")
if (marks>=60):
    print(" Your grade is C")
if (marks >= 50):
    print("your grade  is D")
else:
    print (" you are fail")

#assignment operator ( = , +=, -=,*=,/=,%=)
 write a program to add , multiple , divide , module of 2 number using assingment operator 
a = int(input("Enter your 1st number : "))
b = int(input(" Enter your 2nd number : "))
a += b 
print("Sum is ", a)
a*=b # output 12 bcz the value of a became 6 
print("multiple is ", a)
a/=b
print("Divide is ",a)
a%=b
print("Reminder is", a)

#logical operator (not , or , and )
not = always gives oppostie result 
a = 30
b = 20
print(not (a==b)) # True  bcz gives always opposite result
print(not False) # always remember T of true and F of false is always captial 
print(not(a>b)) # false 

# and = both value will be true 
a = 18

if (a >=18 and a==18):
    print("you can drive ")
else:
    print("you cannot drive ")

or = if one value or condition is true 

a = 11

if (a >=18 or  a==18):
    print("you can drive ")
else:
    print("you cannot drive ") # output you cannot drive 

# wap to take 2 float number as input and print their average 
a = float(input("Enter your 1st decimal value :"))
b = float(input("Enter your 2nd decimal value :"))
sum = a +b 
average = sum /2
print("Average of 2 decimal value is :", average)

#wap to take input 2 number a and b print true if a is greater than b if not print false 
a = int(input("Enter a 1st number : "))
b = int(input(" Enter a 2nd number :"))
if(a>=b ):
    print("true")
else:
    print("false") 


