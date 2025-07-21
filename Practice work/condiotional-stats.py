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
'''
#8. Check if character is vowel
n=input("Enter a char:")
if n.lower() in ['a','e','i','o','u']:
    print("Vowel")
else:
    print("Consonent")