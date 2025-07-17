#Basic Examples of print()
#a) Printing Text
print("Hello, World!")#Output: Hello, World!
#b) Printing Multiple Items
name = "Alice"
age = 25
print("Name:", name, "Age:", age)#Output: Name: Alice Age: 25
#c) Using sep to Change the Separator
print("2024", "02", "07", sep="-")#Output: 2024-02-07
#d) Using end to Control Line Endings
print("Hello,", end=" ")
print("World!")#Output: Hello, World!

#Printing Special Characters
#a) New Line (\n):
print("Line 1\nLine 2")#Output:Line 1
                               #Line 2
#b)Tab (\t):
print("Name:\tAlice")#Output: Name:   Alice

#Output Formatting
#1.Using Commas (Simple Print Method)
name = "Alice"
age = 25
score = 95.5
print("Name:", name, "Age:", age, "Score:", score)#Output: Name: Alice Age: 25 Score: 95.5
#2.Using Modulo Operator (% Formatting)
name = "Bob"
age = 30
score = 88.75
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))#Output:Name: Bob | Age: 30 | Score: 88.75
#3️.Using f-strings (Formatted String Literals)
name = "Charlie"
age = 28
score = 92.389
print(f"Name: {name} | Age: {age} | Score: {score:.2f}")#Output: Name: Charlie | Age: 28 | Score: 92.39
#4️.Using str.format() Method
name = "Diana"
age = 22
score = 89.456
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,score))#Output: Name: Diana | Age: 22 | Score: 89.5
