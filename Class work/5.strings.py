s1 = 'Hello'
s2 = "World"
s3 = '''This is a multi-line
string example.'''
print(s1)
print(s2)
print(s3)

#Operations
#1. Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # Output: Hello World
#2. Repetition
print("Python! " * 3) # Output: Python! Python! Python!
#3. Indexing
text = "Python"
print(text[0]) # Output: P (1st character)
print(text[-1]) # Output: n (last character)
#4. Slicing
print(text[0:3]) # Output: Pyt (from index 0 to 2)
print(text[:4]) # Output: Pyth (default start is 0)
print(text[2:]) # Output: thon (from index 2 to end)
#5. Membership
print('Pyt' in text) # Output: True
print('Java' not in text) # Output: True
print("Python" not in text)#Output: False

#Built-in String Functions
# 1. len()
text = "Hello World"
print(len(text)) # Output: 11 (also includes whitespace)
# 2. max() and min()
print(max("abcXYZ")) # Output: 'c' (highest ASCII value) 
print(min("abcXYZ")) # Output: 'X' (lowest ASCII value) capital letters first in ASCII
# 3. sorted()
print(sorted("python")) # Output: ['h', 'n', 'o', 'p', 't','y']
# 4. chr() and ord()
print(ord('A')) # Output: 65 (ASCII value of 'A')
print(chr(97)) # Output: 'a' (character for ASCII value 97)

# Case Conversion Methods
x="Python"
print(x.lower())# Output: python
print(x.upper())# Output: PYTHON
print(x.capitalize())# Output:Python
print(x.title())# Output: Python
print(x.swapcase())# Output: pYTHON
print(x.casefold())# Output: python

# Alignment & Formatting Methods
x="Python Programming"
print(x.center(30,"*"))# Output: ******Python Programming******
print(x.ljust(30,"-"))# Output: Python Programming------------
print(x.rjust(30,"-"))# Output: ------------Python Programming
print("42".zfill(5))#Output: 00042

# Search & Find Methods
x="Hello"
print(x.find('l')) # Output:2 (Returns the index of first occurrence, -1 if not found.)
print(x.rfind('l')) # Output:3 (Returns the last occurrence of the substring.)
print(x.index('e')) # Output:1 (Like find(), but raises an error if not found.)
print(x.rindex('o')) # Output:4 (Like rfind(), but raises an error if not found.)
print(x.count('H')) # Output:1 (Counts how many times sub appears.)