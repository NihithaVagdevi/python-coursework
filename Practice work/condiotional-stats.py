'''1. Positive or Negative
n=int(input("Enter a number:"))
if n>0:
    print("Positive number")
elif n<0:
    print("Negative number")
else:
    print("Zero")

#2. Even or Odd
n=int(input("Enter a number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")

#3. Divisible by 5
n=int(input("Enter a number:"))
if n%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

#4. Divisible by 3 and 7
n=int(input("Enter a number:"))
if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7")
else:
    print("Not Divisible by both 3 and 7")

#5. Check for Leap Year
year=int(input("Enter the year:"))
if (year%4==0) and (year%100!=0 or year%400==0):
    print("Leap year")
else:
    print("Not a leap year")

#6. Check Pass or Fail (Passing marks = 35)
marks=int(input("Enter the marks:"))
if marks>40:
    print("Pass")
else:
    print("Fail")

#7. Check if number is 3-digit
n=int(input("Enter 3 digit number:" ))
if (100<=abs(n)<=999):
    print("3 digit num")
else:
    print("Not a digit num")

#8. Check if character is vowel
n=input("Enter a char:")
if n.lower() in ['a','e','i','o','u']:
    print("Vowel")
else:
    print("Consonent")

#9. Check greatest of two numbers
a=int(input("Enter a num:"))
b=int(input("Enter a num: "))
if a>b:
    print(f'{a} is greater ')
else:
    print(f'{b} is greater')

#10. Check smallest of two numbers
a=int(input("Enter a num:"))
b=int(input("Enter a num: "))
if a<b:
    print(f'{a} is smaller')
else:
    print(f'{b} is smaller')

#11. Check if number is zero
a=int(input("Enter a num:"))
if a==0:
    print("Number is zero")
else:
    print("Number is not zero")

#12. Check if number is multiple of 10
a=int(input("Enter a number:"))
if a%10==0:
    print(f'{a} is multiple of 10')
else:
    print(f'{a} is not a multiple of 10')

#13. Check if age is eligible to vote (18+)
age=int(input("Enter the age:"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible")

#14. Check if number is between 1 and 100
a=int(input("Enter a number:" ))
if 1<=a<=100:
    print(f'{a} is in between 1 and 100')
else:
    print(f'{a} is not in between 1 and 100')

#15. Check if number is square of another
a=int(input("Enter a num:"))
b=int(input("Enter a num:"))
if b*b==a:
    print(f'{a} is square of {b}')
else:
    print(f'{a} is not square of {b}')

#16. Check if two strings are equal
a=input("Enter a string:")
b=input("Enter a string:")
if a==b:
    print("Strings are equal")
else:
    print("Strings are not equal")

#17. Check if a number is prime (basic logic)
a=int(input("Enter a num:"))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a, "is not Prime num")
            break
    else:
            print(a,"is a Prime num")
else:
    print(a,"is not a Prime")

#18. Check if number is positive and even
a=int(input("Enter a num:"))
if a>0 and a%2==0:
    print(f'{a} is Positive and a even number')
else:
    print(f'{a} is a Positive and not a even number')

#19. Check if character is uppercase
a=input("Enter a char:")
if a.isupper():
    print("Uppercase letter")
else:
    print(" Not Uppercase letter")

#20. Check if temperature is hot (>30°C)
a=int(input("Enter the temp:"))
if a>30:
    print("It's hot")
else:
    print("Temp is normal")

#1. Check if a number is a 4-digit even number
n=int(input("Enter a 4 digit number:"))
if (1000<=n<=9999) and (n%2==0):
    print("4-digit even number")
else:
    print("Not a 4-digit even number")

#2. Check if a character is a consonant
a=input("Enter a char:")
if a.lower() not in ['a','e','i','o','u']:
    print("Consonent")
else:
    print("Vowel")

#3. Check if a number is divisible by 2 or 3 but not both
n=int(input("Enter a number:"))
if (n%2==0) and (n%3==0):
    print("Divisible by both 2 and 3")
else:
    print("Divisible by 2 only")

#4. Check if a number is negative and odd
n=int(input("Enter a num:"))
if (n<0) and (n%2!=0):
    print("Negative and Odd number")
else:
    print("number")

#5. Check if a string starts with a vowel
a=input("Enter a string:")
if a[0] in'aeiouAEIOU':
    print("Starts with Vowel")
else:
    print("Starts with consonent")

#6. Check if three sides form a valid triangle
a=int(input("Enter the side of triangle:"))
b=int(input("Enter the side of triangle:"))
c=int(input("Enter the side of triangle:"))
if a+b>c and b+c>a and c+a>b:
    print("Valid triangle")
else:
    print("Not a valid triangle")

#7. Find the greatest among three numbers
a=int(input())
b=int(input())
c=int(input())
if a>b:
    print(f'{a} is greatest')
elif b>c:
    print(f'{b} is greatest')
else:
    print(f'{c} is greatest')

#8. Check if a year is a century year and leap year
year = int(input("Enter a year: "))

# Check if century year
if year % 100 == 0:
    print("It is a Century Year")
else:
    print("It is not a Century Year")

# Check if leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")

#9. Check if a character is a digit
a=input("Enter a digit:")
if a.isdigit():
    print("It is a digit")
else:
    print("It is not a digit")

#10. Check if a number is palindrome (integer)
a=int(input("Enter a num:"))
original=a
reverse=0
while a>0:
    reverse=reverse*10+a%10
    a=a//10
if original==reverse:
    print("It is a Palindrome")
else:
    print("Not a palindrome")

#11. Compare lengths of two strings
a=input("Enter a string:")
b=input("Enter a string:")
if len(a)>len(b):
    print("First string is longer")
else:
    print("Second string is longer")

#12. Check if a number is within a specific range (50 to 100) and divisible by 5
a=int(input("Enter a num:"))
if (50<a<100) and (a%5==0):
    print("In range and divisible by 5")
else:
    print("Not in range and not divisible")

#13. Validate if a password length is strong (8 or more characters)
password=input("Enter a password:")
if len(password)>=8:
    print("Strong password")
else:
    print("Not a strong password")

#14. Check if sum of two numbers is even
a=int(input("Enter a num1:"))
b=int(input("Enter a num2:"))
if ((a+b)%2==0):
    print("Sum is even")
else:
    print("Sum is odd")

#15. Check if the character is a special symbol (!, @, #, etc.)
ch=input("Enter a char:")
if not ch.isalnum():
    print("Special char")
else:
    print("Not a special char")

#16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)
temp=int(input("Enter temp:"))
if temp<15:
    print("Cold")
elif 15<temp<30:
    print("Moderate")
else:
    print("Hot")

#17. Check if a number lies outside the range 10 to 50
a=int(input("Enter a num:"))
if 10<a<50:
    print("Inside the range")
else:
    print("Outside the range")

#18. Check if number is a perfect square (basic method)
import math
a=int(input("Enter a num:"))
root=math.sqrt(a)
if root==int(root):
    print("Perfect square")
else:
    print("Not a perfect square root")

#19. Compare two ages and determine who is older or if same age
age1=int(input("Enter age1:"))
age2=int(input("Enter age2:"))
if age1>age2:
    print("First person is older")
elif age2>age1:
    print("Second person is older")
else:
    print("Same age")

#20. Check if an angle is acute, right, or obtuse
a=int(input("Enter angle:"))
if a<90:
    print("Acute angle")
elif a>90:
    print("Obtuse angle")
else:
    print("Right angle")
'''
#20. Check if an angle is acute, right, or obtuse
a=int(input("Enter angle:"))
if a<90:
    print("Acute angle")
elif a>90:
    print("Obtuse angle")
else:
    print("Right angle")
