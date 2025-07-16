## Creating a set with unique elements
my_set={1,2,3,4,5}
print(my_set)#Output: {1, 2, 3, 4, 5}
## Creating an empty set (use set() function, not {})
empty_set=set()
# Set with duplicate elements (duplicates are removed automatically)
set1={1,2,3,2,3,42,5,2}
print(set1)#Output: {1, 2, 3, 5, 42}

#2.Operations on Sets
#a. Membership Testing
set1={1,2,3,4,5}
print(3 in set1)#Output: True
print(4 not in set1)#Output: False
#b. Union (| or union() method)
set1={1,2,3,4,5}
set2={2,4,6,5,7}
print(set1|set2)#Output: {1, 2, 3, 4, 5, 6, 7}
#c. Intersection (& or intersection() method)
set1={1,2,3,4,5}
set2={2,4,6,5,7}
print(set1 & set2)#Output: {2, 4, 5}
#d. Difference (- or difference() method)
set1={1,2,3,4,5}
set2={2,4,6,5,7}
print(set1 - set2)#Output: {1, 3}
print(set2 - set1)#Output:{6,7}
#e. Symmetric Difference (^ or symmetric_difference() method)
set1={1,2,3,4,5}
set2={2,4,6,5,7}
print(set1 ^ set2)#Output: {1, 3, 6, 7}
#f. Subset (<= or issubset() method)
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1 <= set2)#Output: True
#g. Superset (>= or issuperset() method)
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1 >= set2)#Output: True
#h. Disjoint Sets (isdisjoint() method)
set1={1,2,3,4}
set2={5,6,7,8}
print(set1.isdisjoint(set2))#Output: True(Returns True if two sets have no common elements.)

#3.Built-in Methods for Sets
print(set1.add(5))#Output:
print(set1.remove(2))#Output:
print(set1.discard(5))#Output:
print(set1.pop())#Output:
print(set1.clear())#Output:
set1={1,2,3,4}#Output:
set2={5,6,7,8}#Output:
print(set1.union(set2))#Output:
print(set1.intersection(set2))#Output:
print(set1.difference(set2))#Output:{1, 2, 3, 4}
print(set1.symmetric_difference(set2))#Output:{1, 2, 3, 4, 5, 6, 7, 8}
print(set1.update(set2))#Output:
print(set1.intersection_update(set2))#Output:
print(set1.difference_update(set2))#Output:
print(set1.symmetric_difference_update(set2))#Output:
new_set=set1.copy()
print(new_set)#Output:{8, 5, 6, 7}

#4.Built-in Functions for Sets
print(len(set1))#Output:4
print(max(set1))#Output:8
print(min(set1))#Output:5
print(sum(set1))#Output:26
set1={3,1,9,4}
print(sorted(set1))#Output:[1, 3, 4, 9]
l1=[1,2,3]
print(set(l1))#Output: {1, 2, 3}