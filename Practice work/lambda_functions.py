#1. Square of a number using lambda
# sq=lambda n:n*n
# print(sq(4))

#2. Check if number is even using lambda
# even_odd=lambda n:'even' if n%2==0 else 'odd'
# print(even_odd(5))

#3. Get maximum of two numbers using lambda
# maxnum=lambda a,b: a if a>b else b
# print(maxnum(2,6))

#4. Multiply two numbers using lambda
# pro=lambda a,b: a*b
# print(pro(2,4))

#5. Sort a list of tuples by second element using lambda
# l=[(1, 3), (2, 1), (4, 2)]
# print(sorted(l,key=lambda i:i[1]))  #O/P: [(2, 1), (4, 2), (1, 3)]

#6. Filter even numbers from a list using lambda and filter()
# l=[1,2,3,4,5,6]
# l1=list(filter(lambda i:i%2==0,l))
# print(l1) #[2, 4, 6]

#7. Square each element in a list using lambda and map()
# l=[1,2,3,4,5]
# l1=list(map(lambda i:i**2,l))
# print(l1)  #[1, 4, 9, 16, 25]

#8. Convert list of strings to uppercase using lambda
# a=['nihitha','leorah','keerthana']
# a1=list(map(lambda i:i.upper(),a))
# print(a1) #['NIHITHA', 'LEORAH', 'KEERTHANA']

#9. Sort list of dictionaries by key using lambda
# d=[{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}]
# print(sorted(d,key=lambda i:i['age']))  #[{'name': 'B', 'age': 20}, {'name': 'A', 'age': 30}]

#10. Return length of a string using lambda
# length=lambda s: len(s)
# print(len("Nihitha")) #7

#11. Check if string starts with a vowel using lambda
# vol='aeiouAEIOU'
# string=lambda s: True if s[0] in vol else False
# print(string("Hello")) #False

#12. Add 10 to each element using lambda and map()
# l=[1,2,3,4,5,6]
# l1=list(map(lambda i:i+10,l))
# print(l1) #[11, 12, 13, 14, 15, 16]

#13. Filter strings longer than 3 characters
# a=["a", "the", "lamp", "cat"]
# a1=list(filter(lambda i:len(i)>3,a))
# print(a1) #['lamp']

#14. Multiply each number by its index using lambda
# l=[1,2,3,4,5,6]
# for val,ind in enumerate(l):
#     print(val,ind)
# l1=list(map(lambda val:val[0]*val[1],enumerate(l)))
# print(l1) #[0, 2, 6, 12, 20, 30]

#15. Use lambda with reduce() to calculate product
from  functools import reduce
# l=[1,2,3,4]
# product=reduce(lambda pro,item:pro*item,l)
# print(product) #24

#16. Use lambda with filter to find multiples of 3
# l=[12,63,73,86]
# l1=list(filter(lambda i:i%3==0,l))
# print(l1) #[12, 63]

#18. Lambda to extract domain from email
# domain=lambda mail:mail.split('@')[1]
# print(domain('abc@gmail.com')) #gmail.com

#19. Use lambda to get last digit of a number
# last_digit=lambda n:n%10
# print(last_digit(12635)) #5

#20. Use lambda to check if year is a leap year
isleap=lambda year:"Leap" if year%400==0 or (year%4==0 and year%100!=0) else "Not Leap"
print(isleap(2020)) #Leap