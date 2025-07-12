# Empty Tuple
empty_tuple = ()
print(empty_tuple)
# Single-element Tuple (note the trailing comma)
single_tuple = (5,)
print(single_tuple) #Output: (5,)
# Multi-element Tuple
my_tuple = (1, "apple", 3.5) 
print(my_tuple) #Output: (1, 'apple', 3.5)
# Without parentheses (implicit tuple creation)
implicit_tuple = 1, 2, 3
print(implicit_tuple) #Output: (1, 2, 3)

#2. Accessing Tuple Elements
#a. Indexing
tup=(10,20,30,40)
print(tup[2]) #Output:30
#b. Negative Indexing
print(my_tuple[-1]) #Output:3.5
#c. Slicing
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4]) #Output: (20, 30, 40)

#3. Operations on Tuples
#a. Concatenation
tup1=(1,2,3)
tup2=(4,5,6)
tup=tup1+tup2
print(tup) #Output: (1, 2, 3, 4, 5, 6)
tup=tup1+(7,8,9)
print(tup) #Output: (1, 2, 3, 7, 8, 9)
#b. Repetition
my_tuple = (1, 2)
print(my_tuple*4) #Output: (1, 2, 1, 2, 1, 2, 1, 2)
#c. Membership Testing
#4. Tuple Methods
print(3 in my_tuple) #Output:True
print(4 not in my_tuple) #Output:True
#d. Tuple Unpacking
a=("Nihitha","nihitha@gmail.com","Nihitha@123")
name,mail,pwd=a
print(name)#Output:Nihitha
print(mail)#Output:nihitha@gmail.com
print(pwd)#Output:Nihitha@123

#4. Tuple Methods
my_tuple = (10, 20, 30, 40, 50,20,40,12)
print(my_tuple.count(20))#Output:2
print(my_tuple.index(20))#Output:1

#5. Built-in Functions for Tuples
my_tuple = (10, 20, 30, 40, 50,20,40,12)
print(len(my_tuple))#Output:8
print(max(my_tuple))#Output:50
print(min(my_tuple))#Output:10
print(sum(my_tuple))#Output:222
my_list = [10, 20, 30, 40, 50,20,40,12]
print(tuple(my_list))#Output: (10, 20, 30, 40, 50, 20, 40, 12)

#6. Immutability and Tuple Behaviour
nested_tuple = (1, [2, 3])
nested_tuple[1][0] = 100
print(nested_tuple) #Output: (1, [100, 3])