# #1.Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)

# #2. Print all even numbers from 1 to 50.
# for i in range(2,51,2):
#     print(i)

# #3.Print all odd numbers between 1 and 100.
# for i in range(1,100,2):
#     print(i)

# #4.Print the square of numbers from 1 to 20.
# for i in range(1,21):
#     print(i*i)#i**2

# #5.Print the multiplication table of a given number.
# n=int(input("Enter a num:"))
# for i in range(1,11):
#     print(f'{n}*{i}={n*i}')

# #6.Calculate the sum of first N natural numbers.
# n=int(input("Enter a num:"))
# total=0
# for i in range(1,n+1):
#     total+=i
# print("Sum=",total)

# #7.Count how many vowels are in a given string.
# text=input("Enter a string:")
# count=0
# for char in text:
#     if char.lower() in "aeiou":
#         count+=1
# print(count)

# #8.Print each character of a string on a new line.
# text=input("Enter a string:")
# for char in text:
#     print(char)

# #9.Print all elements in a list using a for loop.
# l=list(map(int,input("Enter elements").split(",")))
# for i in l:
#     print(i)

# #10.Find the factorial of a given number.
# n=int(input("Enter a num"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# #11.Print numbers from 10 to 1 in reverse.
# for i in range(10,0,-1):
#     print(i)

# #12.Print all uppercase letters in a given string.
# text=input("Enter a string:")
# for char in text:
#     if char.isupper():
#         print(char)

# #13.Count how many digits are in a given string.
# text=input("Enter a string:")
# count=0
# for char in text:
#     if char.isdigit():
#         count+=1
# print(count)

# #14.Print all elements in a list of numbers greater than 50.
# l=list(map(int,input("Enter elements:").split(",")))
# for i in l:
#     if i>50:
#         print(i)

# #15.Reverse a string using a for loop.
# text=input("Enter a string:")
# rev=" "
# for char in text:
#     rev=char+rev
# print(rev)

# #16.Find the sum of all elements in a list.
# l=list(map(int,input("Enter elements:").split(",")))
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# #17.Print the first 10 multiples of a given number.
# n=int(input())
# for i in range(1,11):
#     print(n*i)


# #1. Print Numbers from 1 to N (Using for loop)
# n=int(input())
# for i in range(1,n+1):
#     print(i,end=' ')#O/P:10  1 2 3 4 5 6 7 8 9 10 

# #2. Print Even Numbers from 1 to N (Using for loop)
# n=int(input())
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,end=' ')#O/P:2 4 6 8 10 12 14 16 18 20 

# #3. Sum of Numbers from 1 to N (Using for loop)
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# #4. Print Odd Numbers from 1 to N (Using for loop)
# n=int(input())
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i,end=' ') #O/P:1 3 5 7 9 11 13 15 17 19 21 23 25 27 29

# #5. Find Factorial of a Number (Using for loop)
# n=int(input())
# fact=1
# for i in range(2,n+1):
#     fact*=i
# print(fact) 

# #6. Print Multiplication Table of N (Using for loop)
# n=int(input())
# for i in range(1,n+1):
#     print(f'{n} * {i} ={n*i}')

# #7. Check Prime Number (Using for loop)
# n = int(input("enter a number : "))
# c =  0
# for i in range(2,n):   
#     if n % i == 0:
#         c += 1
#         break 
# if c == 0:
#     print("prime")
# else:
#     print("not a prime")

# #8. Sum of Digits of a Number (Using while loop)
# n=int(input())
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n=n//10
# print(sum)

# #Fibonacci numbers
# n=int(input())
# a=0
# b=1
# print("Fib seq:")
# for i in range(n):
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c

# #10. Count Numbers Divisible by 3 (Using for loop)
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if i%3==0:
#         print(i,end=' ')
#         c+=1
# print("\nCount",c)

# #11. Check if a Number is Palindrome (Using while loop)
# num = int(input("Enter a number: "))
# original = num
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# if original == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# #12. Print Multiples of 5 up to N (Using for loop)
# n=int(input())
# for i in range(1,n+1):
#     if i%5==0:
#         print(i)

# #13. Find the Maximum of Three Numbers (Using for loop)
# l=list(map(int,input().split()))
# if len(l)!=3:
#     print("Enter 3 nums")
# else:
#     max=l[0]
#     for i in l:
#         if i>max:
#             max=i
#     print(max)

# #14. Print Reverse of a Number (Using while loop)
# n=int(input())
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

# #15. Sum of First N Natural Numbers (Using for loop)
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total+=i
# print(total)

# #16. Print Numbers from N to 1 (Using while loop)
# n=int(input())
# while n>=1:
#     print(n,end=' ')
#     n-=1

# #17. Find Sum of Prime Numbers up to N (Using for loop)
# n=int(input())
# sum_primes=0
# for num in range(2,n+1):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         sum_primes+=num
# print(sum_primes)

#18. Find the Product of Digits of a Number (Using while loop)
# n=int(input())
# product=1
# while n>0:
#     digit=n%10
#     product*=digit
#     n=n//10
# print(product)

#19. Print Numbers Divisible by Both 3 and 5 (Using for loop)
# n=int(input())
# print("Numbers diviible by both 3 and 5:")
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print(i,end=' ')

#20. Find GCD of Two Numbers (Using while loop)
# a=int(input())
# b=int(input())
# while b!=0:
#     a,b=b,a%b
# print(a)

# #Patterns
# #1.Right angled
# n=int(input())
# for row in range(1,n+1):
#     for col in range(row):
#         print("*",end=' ')
#     print()
# #o/p:
# 5
# * 
# * *
# * * *
# * * * *
# * * * * *

# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# #o/p:
# Enter number of rows: 5
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows = int(input("Enter number of rows (for top half): "))

# # Top half
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "* " * i)

# # Bottom half
# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i) + "* " * i)
# #o/p:
# Enter number of rows (for top half): 3
#   * 
#  * *
# * * *
#  * *
#   *

