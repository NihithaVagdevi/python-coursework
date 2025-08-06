# u=lambda n: n+10
# print(u(10))#O/P:20

# cube=lambda n:n**3
# print(cube(5)) #O/P: 125

# s=lambda s: s[0]
# print(s("python"))#O/P:p
# print(s("language"))#O/P:l

# add= lambda a,b: a+b
# print(add(20,53)) #O/P: 73

# greater=lambda a,b: a if a>b else b
# print(greater(12,74)) #O/P: 74

# even_odd=lambda n: "Even" if n%2==0 else "Odd"
# print(even_odd(3))#O/P: Odd

# sum=lambda a,b,c: a+b+c
# print(sum(12,3,45))#O/P: 60

#map
# s='python programming'

# update=list(map(lambda i: i.upper(),s))
# print(update)#O/P: ['P', 'Y', 'T', 'H', 'O', 'N', ' ', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']

# asci=list(map(lambda i: ord(i),s))
# print(asci)#O/P: [112, 121, 116, 104, 111, 110, 32, 112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]

# vow='aeiouAEIOU'
# frmt=list(map(lambda i: '*' if i in vow else '0',s))
# print(frmt)#O/P: ['0', '0', '0', '0', '*', '0', '0', '0', '0', '*', '0', '0', '*', '0', '0', '*', '0', '0']

# l=[1,2,3,4,5,6,7,8,9,10]
# list_upd=list(map(lambda i: i+1,l))
# print(list_upd) #O/P: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# t=(20,62,74,28,98,72,54)
# rem=tuple(map(lambda i:i//10,t))
# print(rem) #O/P: (2, 6, 7, 2, 9, 7, 5)

# s={'python','language','html','css'}
# setup=set(map(lambda i:i.upper(),s))
# print(setup)#O/P: {'CSS', 'HTML', 'LANGUAGE', 'PYTHON'}

# d={1:'ab',2:'bc',3:'cd',4:'de',5:'ef'}
# d_update=list(map(lambda i: d[i].title(),d))
# print(d_update)

#filter
# s='python programming'
# vol='aeiouAEIOU'
# frmt=list(filter(lambda i: i in vol,s))
# print(frmt)#O/P:['o', 'o', 'a', 'i']

# frmt1=list(filter(lambda i: i not in vol,s))
# print(frmt1)#O/P: ['p', 'y', 't', 'h', 'n', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g']

# l=[1,2,3,4,5,6]
# lst=list(filter(lambda i: i%2==0,l))
# print(lst)#O/P: [2, 4, 6]

# lst=list(filter(lambda i: i%2!=0,l))
# print(lst)#O/P: [1, 3, 5]

# t=(10,24,33,39,50,60)
# t_up=tuple(filter(lambda i:i%10==0,t))
# print(t_up)#O/P:(10, 50, 60)

# s={'python','language','html','css'}
# setup=set(filter(lambda i:i.startswith('p'),s))
# print(setup)#O/P:{'python'}

# products={'mouse':18,'laptops':64,'earphones':0}
# pro=list(filter(lambda i: products[i]>0,products))
# print(pro)#O/P: ['mouse', 'laptops']

#reduce
from  functools import reduce
# l=[1,2,3,4]
# sum=reduce(lambda s,a:s+a,l)
# print(sum)#O/P: 10

# s={'python','language','html','css'}
# sup=reduce(lambda n,name: n+' '+name,s)
# print(sup)#O/P: python css html language

# t=(1,2,3,4,5)
# pro=reduce(lambda pro,item:pro*item,t)
# print(pro)#O/P: 120

# d={'python':18,'html':64,'css':0}
# sum=reduce(lambda s,i:)
# print(sum)
