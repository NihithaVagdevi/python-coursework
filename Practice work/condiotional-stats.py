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
'''
