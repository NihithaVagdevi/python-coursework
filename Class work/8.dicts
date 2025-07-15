#1. Defining
dict1={"name":"Nihitha","age":20,"course":"Python"}
print(dict1) #Output:{'name': 'Nihitha', 'age': 20, 'course': 'Python'}

#2. Dictionary Operations
#Accessing Values
print(dict1["name"])#Output:Nihitha
print(dict1["age"])#Output:20

#Difference Between dict[key] and dict.get(key)
#● dict[key] will raise a KeyError if the key does not exist.
#● dict.get(key, default_value) will return None or the specified
#default_value if the key is not found.
print(dict1.get("city", "Not Available")) #Output:Not Available

#2.2 Adding and Updating Items
dict1["age"]=21
dict1["city"]="Hyderabad"
print(dict1)#Output: {'name': 'Nihitha', 'age': 21, 'course': 'Python', 'city': 'Hyderabad'}

#2.3 Removing Items from a Dictionary
#Using pop(key)
age=dict1.pop("age")
print(age)#Output:21
print(dict1)#Output:{'name': 'Nihitha', 'course': 'Python', 'city': 'Hyderabad'}
#Using del
del dict1["city"]
print(dict1)#Output: {'name': 'Nihitha', 'course': 'Python'}
#Using popitem()
dict1.popitem()
print(dict1)#Output: {'name': 'Nihitha'}
#Using clear()
dict1.clear()
print(dict1)#Output: {}

#3. Dictionary Built-in Methods
#3.1 Dictionary Methods for Accessing Data
dict1={'name': 'Nihitha', 'age': 21, 'course': 'Python', 'city': 'Hyderabad'}
print(dict1.get("Qualification","Not Found"))#Output: Not Found
print(dict1.keys())#Output: dict_keys(['name', 'age', 'course', 'city'])
print(dict1.values())#Output: dict_values(['Nihitha', 21, 'Python', 'Hyderabad'])
print(dict1.items())#Output: dict_items([('name', 'Nihitha'), ('age', 21), ('course', 'Python'), ('city', 'Hyderabad')])
#3.2 Dictionary Methods for Adding and Updating Data
print(dict1.update({"city":"Warangal"}))
print(dict1)#Output:{'name': 'Nihitha', 'age': 21, 'course': 'Python', 'city': 'Warangal'}
print(dict1.setdefault("marks","not found"))#Output:not found

#4. Built-in Functions for Dictionaries
print(len(dict1))#Output:5
print(max(dict1))#Output:name
print(min(dict1))#Output:age
print(sorted(dict1))#Output: ['age', 'city', 'course', 'marks', 'name']

#5. Nested Dictionaries
students = {
"Alice": {"age": 21, "course": "CS"},
"Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"])#Output:CS

#6. Real-Time Problems Using Dictionaries
#Problem 1: Find the Student with the Highest Marks
students={
    "Alice":20,
    "Bob":30,
    "Charlie":25
}
print(len(students))#Output:3
top_student = max(students, key=students.get)
print(top_student)#Output:Bob