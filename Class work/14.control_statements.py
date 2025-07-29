'''
#
moves=34
winning_point=int(input("Enter winning point:"))
while moves>0:
    if moves==winning_point:
        print("Congrats! You won the game")
        break
    print(f'{moves} are left. You have chance to win')
    moves-=1
else:
    print("Game over")

#Ascii values
s="python programming"
ind=0
n=len(s)
while ind<len(s):
    print(ord(s[ind]))
    ind+=1

#5 4 3 2 1
n=5
while n>0:
    print(n)
    n=n-1

#Multiples of 3
n=1
while n<10:
    print(n*3)
    n+=1

#Square of a num
n=1
while n<7:
    print(n*n)
    n+=1

#Sum of numbers in a list
l=list(map(int,input("Enter nums:").split()))
s=0
ind=0
while ind<len(l):
    s=s+l[ind]
    ind+=1
print(s)

#Sum of each digit in a number
n=int(input("Enter a num:"))
s=0
while n>0:
    s+=(n%10)
    n//=10
print(s)

#Plaindrome num
n=int(input())
temp=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n//=10
if rev==temp:
    print("Palindrome num")
else:
    print("Not a palindrome")

#Palindrome of a string
n=input()
if n==n[::-1]:
    print(True)
else:
    print(False)

#Palindrome
n=input()
full=len(n)-1
length=len(n)//2
ind=0
while ind<=length:
    if n[ind]!=n[full]:
        print("Not plaindrome")
        break
    ind+=1
    full-=1
else:
    print('Palindrome')

#Nested Loops
#Patterns
1)
for j in range(5):
    for i in range(5):
        print("*",end=" ")    
    print()
O/P:
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *

2)
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print("*",end=' ')
    print()
#O/p:
Enter the size: 7
* * * * * * * 
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * * 
* * * * * * *

#3)
n=int(input("Enter the num:"))
for row in range(n):
    for col in range(n):
        print(row,end='')
    print()
#O/P:
Enter the num:7
0000000
1111111
2222222
3333333
4444444
5555555
6666666

#4)
n=int(input())
for row in range(n):
    for col in range(n):
        print(col,end='')
    print()
O/P:
5
01234
01234
01234
01234
01234

#5)
n=int(input())
for row in range(n):
    for col in range(row+1):
        print(col,end='*')
    print()
O/P:
7
0
01
012
0123
01234
012345
0123456

#6)
n=int(input())
for row in range(n):
    for col in range(n-row):
        print("*",end='')
    print()
O/P:
*****
****
***
**
*

#7)
n=int(input())
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()
O/P:
5
        * 
      * *
    * * *
  * * * *
* * * * *

#8)
n=int(input())
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()
O/P:
5
* * * * * 
  * * * *
    * * *
      * *
        *

n=int(input())
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()
for row in range(n):
    for col in range(n-row-1):
        print("*",end=' ')
    print()
O/p:
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 


#10)
n=int(input())
for row in range(n):
    if row<=n//2:
        for col1 in range(row+1):
            print('*',end='')
    else:
        for col2 in range(n-row):
            print('*',end='')
    print()
O/P:
10
*
**
***
****
*****
******
****
***
**
*

#11)
n=int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
O/P:
10
* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *

# n = int(input("enter size : "))
# for row in range(n):
#   for col in range(n):
#     if row==0 or col == 0 or row==n-1 or col==n-1 or row==n//2 :
#       print("*",end=' ')
#     else:
#       print(' ',end=' ')
#   print()  


O/P:
enter size : 5
* * * * * 
*       *
* * * * *
*       *
* * * * *

#12)
n=int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2 or col==n//2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
O/P:
11
* * * * * * * * * * * 
*         *         *
*         *         *
*         *         *
*         *         *
* * * * * * * * * * *
*         *         *
*         *         *
*         *         *
*         *         * 
* * * * * * * * * * *

#13)
n=int(input())
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
O/P:
8
* * * * * * * * 
            *
          *
        *
      *
    *
  *
* * * * * * * *

#15)
n=int(input())
for row in range(n):
    for col in range(n):
        if row==col or col+row==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
O/P:
10
*                 * 
  *             *
    *         *
      *     *
        * *
        * *
      *     *       
    *         *
  *             *
*                 *
'''
