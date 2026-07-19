# #conditional statements 
#if-elif-else

light = "pink"
if light=="red":
    print("Stop")
elif light=="green":
    print("GO")
elif light=="yellow":
    print("Wait")
else:
    print ("Invalid color")

#if-else

age = 95
if(age >= 18):
    if(age>=80):
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You cannot drive")
 
#practice questions
num =  int(input("Enter a number: "))
if num > 0:
    print("positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>=b and a>=c:
    print("A is greater.")
elif b>a and b>=c:
    print("B is greater. ")
else:
    print("C is greater. ")

year =  int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Its a leap year.")
else:
    print("Its not a leap year.")

num = int(input("Enter a number: "))
if num%2==0:
    print("Its a even number")
else:
    print("Its an odd number")

marks = int(input("Enter marks: "))
if marks >=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Grade D")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    print("A is greater")
elif b>a:
    print("B is greater")
else:
    print("Both are equal number")

str1 = input("Enter the character: ").lower()
if str1=='a' or str1=='e' or str1=='i' or str1=='o' or str1=='u':
 print("VOWEL")
else:
 print("Consonant")

name = input("Enter name :")
password = input("Enter your password: ")
if name =="admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

age = int (input("Enter your age :"))
if age>=65:
    print("price: $12")
elif age>=18:
    print("Ticket price:$20")
elif age>=5:
    print("Ticket price:$10")
else:
    print("Ticket price:free")