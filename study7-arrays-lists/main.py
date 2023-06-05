import statistics

'''
What are Arrays in programming? 
    They are 'numeric lists', often called just "lists"
    They're an indexed homogeneous one-dimensional data structure
    Application structures that work with similar datasets 
    that can reference each element of the set by an index number.

In Python a very common data structure is the list. 
These lists are objects that can contain other objects, that is,
we can consider lists as variables that can contain several values.

Reminder: A simple variable can hold only one value at a given time. 
Lists, on the other hand, can store different values.
Making a metaphor: 
    If the variable corresponds to the space of a house, a list 
    represents a street, and can then contain several houses.
'''

# Syntax:
# list = [element1, element2, ... , elementn]

numeric_list = [0, 1, 2, 3, 4, 5] # 6 position vector

print(numeric_list)

# Manually changing the value in each index
numeric_list[0] = 5
numeric_list[1] = 10
numeric_list[2] = 15
numeric_list[3] = 20
numeric_list[4] = 25
numeric_list[5] = 30

print(numeric_list)

#  INDEX:       0       1         2         3            4
names_list = ["João", "Maria", "Carlos", "Eduardo", "Cristiane"]

# Accessing the list
print(names_list)
# Accessing an unique value by calling its index on the list
print(names_list[2])

# Special Array Functions
# .insert() ------->  <array_name>.insert(<index>, <value>)
# If the position doesn't exist, the element will be added at the end
if (names_list[2] == "Carlos"):
    # Adds "Fulano" to the names_list
    names_list.insert(2, "Fulano") # Now "Carlos" has index 3 and "Fulano" has index 2
print(names_list)

# Getting the list size with len()
print("List size: ",len(names_list))

# Removing a value from the list ---> array.remove(x)
# Removes the first item found in the list with value equal to 'x'.
# If the value x does not exist, a ValueError exception is raised.
names_list.remove("Eduardo")
print(names_list)

# Adding an element to the end of the list (In JS, it's similar. But the method name is .push instead of .append)
names_list.append("Beltrano")
print(names_list)

# Removing an index (position) from the list
del names_list[(len(names_list)) - 1] # In this case, I deleted the last position
print(names_list)

# Creating a list inside another list and accessing it
extended_list = [1, 3, "blabla", [7, 2, 6, 8, 1], False]
print(extended_list[3][2]) # OUTPUT: 6--^
nested_list = extended_list[3]
print(nested_list)

# Adding elements from a list inside another list using extend()
random_list1 = [] 
random_list1.append('item1')
random_list1.append('item2')
random_list1.append('item3')
random_list1.append('item4')

random_list2 = ["a", "b", "c"]
random_list1.extend(random_list2)
random_list2.extend(random_list2)
print(random_list1)
print(random_list2)

# Ways of creating an empty list
list_one = [] 
list_two = list()		# Using a Constructor: list()
print(list_one)
print(list_two)

# Usando índices negativos
example_list = [10, 20, 30, 40] 
#             0    1    2    3   ---> Index / list position, positive counting
#             -4   -3  -2   -1   ---> Index / list position, negative counting
print(example_list[1])
print(example_list[-3]) 


### Querying/Consulting a list
'''
- array.index()
- Retorna o índice do primeiro item cujo valor é igual a 'x'. 
- O primeiro índice da lista é zero.
- The optional start and end arguments are interpreted as in slice notation and are used 
to limit the search to a specific substring of the list.
- The returned index is calculated against the start of the complete string instead of 
the start argument.
- Raises a ValueError if the item 'x' does not exist.
'''
print(example_list.index(40)) 
print(example_list.index(20, 0, 2)) # Searches between indexes 0 and 2

# x in array
# Returns true or false
#Ex.1
if 30 in example_list:
   print('Value is present on the list')
else:
   print('Value is NOT present on the list')
#Ex.2
if 80 in example_list:
   print('Value is present on the list')
else:
   print('Value is NOT present on the list')

# array.count(x)
# Returns the number of times item 'x' appears in the list.
# Ex. 1: 
array = [1, 2, 2, 2, 3, 4, 5]
print("The value '2' appears", array.count(2), "times on the list.")
# OUTPUT: The value '2' appears 3 times on the list.  
# Ex. 2:
print("The value '9' appears", array.count(9), "times on the list.")
# OUTPUT: The value '9' appears 0 times on the list.

#array.pop( [i] )
# Removes and returns the item at index 'i'.
# Similar to array.remove(x), but in this case, it checks for the index and then removes.
# Meanwhile array.remove(x) checks for the value and then removes.
arr1 = [1, 2, 3, 4, 5]
print("Old arr1 list:", arr1)
var = arr1.pop(1)
print("Popped value from index1:", var) # OUTPUT: 2
print("Popped value from index1:", arr1.pop(1)) # OUTPUT: 3
print("New arr1 list:", arr1) # OUTPUT: [1, 4, 5]

# If no index is specified, pop() removes and returns the last item in the list.
arr2 = [1, 2, 3, 4, 5]
print("Old arr2 list:", arr2)
print("Popped value from last index:", arr2.pop()) # OUTPUT: 5
print("New arr2 list:", arr2) # OUTPUT: [1, 2, 3, 4]

# array.clear()
# Removes all the values and indexes from the list, clearing it.
arr3 = ['1', '2', '3', '4', '5']
print("old arr3 list:", arr3)
arr3.clear()
print("Cleared arr3 list:", arr3) # OUTPUT: []

### SORTING LISTS
# (1) array.sort(key = None, reverse = False)
# Sort list items in place (arguments can be used for custom sorting).
# Change the original list and return None.
arr4 = [4, 1, 5, 2, 3]
check_return = arr4.sort()
print(arr4) # OUTPUT: 	[1, 2, 3, 4, 5]
print("Returns:", check_return)

# (2) sorted(array)
# Returns the elements of the list in ascending order and doesn't change the original list.
arr5 = [3, 4, 1, 5, 2]
sorted_arr5 = sorted(arr5)
print(sorted_arr5) # OUTPUT: [1, 2, 3, 4, 5]
print(arr5) # OUTPUT: [3, 4, 1, 5, 2]

# (3) array.reverse()
# Inverts the elements of the list.
# Change the original list and return None.
arr6 = [1, 2, 7, 3, 4, 5]
print("arr6:", arr6) # OUTPUT: [1, 2, 7, 3, 4, 5]
arr6.reverse()
print("reversed arr6:", arr6) # OUTPUT: [5, 4, 3, 7, 2, 1]

# (4) reversed(array)
# Returns the elements of the list in descending order and doesn't change the original list.
# By doing it this way, it returns the result in the new list: arr7
reversed_array6 = list(reversed(arr6)) # built-ins
print("re-reversed arr6:", reversed_array6) # OUTPUT: [1, 2, 7, 3, 4, 5]
print("arr6", arr6) # OUTPUT: [5, 4, 3, 7, 2, 1]

# More Examples of use for the SORTING FUNCTIONS
lista = [1, 2, 3, 4, 5]
print(list(reversed(lista))) # OUTPUT: [5, 4, 3, 2, 1]
print(lista) # OUTPUT: [1, 2, 3, 4, 5]
nova_lista = list(reversed(lista)) # Doesn't change the original list, returns the result in the new list 
print(nova_lista) # OUTPUT: [5, 4, 3, 2, 1]
print(lista) # OUTPUT: [1, 2, 3, 4, 5]

### REVIEWING: Python's Most Useful Array Functions
L = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# len() ---> FUNCTION. Returns the size of the list
print("Size of the list L: ", len(L))

# min() ---> FUNCTION. Returns the lowest value from the list
print("Lowest value in the list: ", min(L))

# max() ---> FUNCTION. Returns the highes value from the list
print("Highest value in the list: ", max(L))

# sum() ---> FUNCTION. Returns the sum of elements in the list
print("Sum of all elements in the list: ", sum(L))

# append() ---> METHOD. Adds a new value to the end of the list.
L.append(100)
print("Adding new element 100: ", L)

# extend() ---> METHOD. Inserts a list at the end of another list.
L.extend([110, 120, 130])
print("Adding three new elements to the list: ", L)

# del list_name[index] ---> KEYWORD. Removes an element from the list, given its index.
del L[1]
print("Deleting index1 of the list: ", L)

# value in list_name ---> KEYWORD. Checks whether a value belongs to the list, returns True or False.
check_list = 30 in L
print("Checking if the value '30' is on the list: ", check_list)

# sort() ---> METHOD. Sorts in ascending order.
L.sort()
print("Ordering the list:", L)

# reverse() ---> METHOD. Inverts the elements of a list.
L.reverse()
print("Reversing the list:", L)


# Calculating the Arithmetic Average
import statistics

# Way1
lista = [2, 3, 4, 5]
media = sum(lista) / len(lista)
print(media)

# Way2
lista = [2, 3, 4, 5]
media = statistics.mean(lista)
print(media)

# Way3
from statistics import mean
lista = [2, 3, 4, 5]
media = mean(lista)
print(media)


### EXTRA:

# (1) Checking for the char[] array (array inside another array)
'''
In the languages_list[3][1], languages_list[3] returns the string "Pascal". 
Then, languages_list[3][1] accesses the character at index 1 of the string "Pascal", which is "a".

In Python, you can use indexing on strings to access individual characters. 
In this case, languages_list[3] returns the string "Pascal", and 
languages_list[3][1] further accesses the character at index 1 within that string. 
Indexing in Python starts from 0, so the character at index 1 in the string "Pascal" is "a".

If you want to access a specific character in the string "Pascal", you can use 
indexing like: languages_list[3][index], where index is the 
position of the character you want to access.

'''
languages_list = ["Python", "Java", "C", "Pascal", "PHP"]

print(languages_list[3]) # OUTPUT: Pascal 

print(languages_list[3][1])  # OUTPUT: a


# (2) array.copy()
# Returns a copy of the list
list1 = [1, 2, 3, 4, 5]

copy = list1.copy()
print(copy) # OUTPUT: [1, 2, 3, 4, 5]

# (3) tuple(array)
# Returns the elements of the list in tuple format
list2 = [1, 2, 3, 4, 5]
t1 = tuple(list2)
print(t1) # OUTPUT: (1, 2, 3, 4, 5)

# (4) Link
list3 = [1, 2, 3, 4, 5]

list4 = list3 # Linked
list5 = list3.copy()
print("List 4: ",list4)
list3.append(3)
print("List 4: ",list4)
print("List 5: ",list5)

# (5) map(function, array) ------------> Super useful!! <3 
# It is a Python built-in function, that is, a function implemented directly in
# the Python interpreter, which can be used without importing a specific module.
# Applies a function to each element of a list, returning a new list
# containing the elements resulting from the application of the function.
import math
list6 = [1, 4, 9, 16, 25]
# This will make a new list that calculates the square root of each element in list6
list7 = list(map(math.sqrt, list6))
print (list7) # OUTPUT: [1.0, 2.0, 3.0, 4.0, 5.0]

def add_tax(price):
   return price * 1.1
prices = [1000, 1500, 1250, 2500]


prices_with_tax = []
for price in prices:
   prices_with_tax.append(add_tax(price))
print(prices_with_tax)

def add_tax(price):
   return price * 1.1
prices = [1000, 1500, 1250, 2500]


prices_with_tax2 = list(map(add_tax, prices)) # map(add_tax, prices)
print (prices_with_tax2)
# <map object at 0x1011df010>

# (6) Performing Operations with Arrays
# Concatenating Lists (+) 
# Concatenate all elements of two lists:
# Ex. 1:
a = [0,1,2]
b = [3,4,5] 
c = a + b # Adding a + b like: [0, 1, 2] + [3, 4, 5] = [0, 1, 2, 3, 4, 5]
print(c) # OUTPUT: [0, 1, 2, 3, 4, 5] 
# Ex. 2:
a = [0, 1, 2]
b = [2, 3, 4, 5] 
c = a + b 
print(c) # OUTPUT: [0, 1, 2, 2, 3, 4, 5] 

# Repetition (*) 
L = [1, 2] 
R = L * 4  
print(R) # OUTPUT: [1, 2, 1, 2, 1, 2, 1, 2] 
print(L) # OUTPUT: [1, 2] 
 
# (7) lista.extend(iterable)
# Extends the list by adding all elements of the iterable.
lista = [1,2,3,4,5]

lista.extend([6,7,8]) 
print(lista) # OUTPUT: [1,2,3,4,5,6,7,8]
lista = [1,2,3,4,5]
lista2 = [9, 8, 7, 6]
lista.extend(lista2)
print(lista) # OUTPUT: [1, 2, 3, 4, 5, 8, 7, 6, 5]

 	
### ADDING USER INPUT TO LISTS
for c in range(5):
  n_lista = int(input('Enter some numbers: '))
  lista.append(n_lista)
print(lista)

lista_notas = []
#lista_notas = list()

# Another example of use
for c in range(5):
   notas = int(input("Enter some grades: "))
   lista_notas.append(notas)

print(lista_notas)
media = sum(lista_notas)/5
print("The average based on the given notes:", media)

"""
phrase = 'John Doe'
ph_list = list (phrase)
# print (phrase)
# print (ph_list)
for i in range(2):
 ph_list.pop() #?

print(ph_list)
new_phrase ="".join(ph_list)
print(ph_list)
print(new_phrase)
ph_list. insert (2, ph_list.pop (8))
ph_list. insert(3, ph_list.pop (10))
ph_list. insert(4, ph_list.pop(3))

"""

'''
a = 'abcdef'
a_1 = list(a)
''.join(a_1[::-1])
# "fedcba"
''.join(a_1[::2])
# 'ace'
''.join(a_1[::])
# "abcdef"
'''

# Finding all the vogals in a phrase
f = input("Say something:\n")
v =['a', 'o', 'u', 'i', 'e']
found = []
for letter in f:
   if letter in v:
       if letter not in found:
           found.append(letter)

for vogal in found:
   print(vogal, end=" ")

