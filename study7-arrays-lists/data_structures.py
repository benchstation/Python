### DIFFERENT TYPES OF DATA STRUCTURES IN PYTHON
array = []
matrix_example = [[0, 1], [0, 2], [0, 3]]

### TUPLES
# Tuples are immutable, like constant lists.
# Tuples can be stored inside lists, lists inside tuples, dictionaries inside tuples, etc.
tupla = ()
# Here's an example of a tuple in Python:
tuple_example = (0, 2, 5, "Hi!")

### DICTIONARIES
dictionary = {}
# In Python, dictionaries are a built-in data structure that allows you to store and retrieve data using key-value pairs. 
# They are also sometimes referred to as 'associative arrays' or 'hash maps' in other programming languages.
# A dictionary is an unordered collection of elements, where each element is represented by a key-value pair. 
# The key serves as a unique identifier for the value it is associated with. 
# This allows for efficient retrieval of values based on their corresponding keys.
# Dictionaries are defined using curly braces ({}) and key-value pairs separated by colons (:). 
# Here's an example of a dictionary in Python:
dictionary_example = {
    "Grade1": "5.2",
    "Grade2": "5.4",
    "Grade3": "6.4"
}
# In this example, "Grade1", "Grade2", and "Grade3" are the keys, and "5.2", "5.4", and "6.4" are the corresponding values. 
# You can access the values in a dictionary by specifying the key in square brackets ([]). 
# For example:
print(dictionary_example["Grade1"])     # Output: "5.2"
print(dictionary_example["Grade2"])     # Output: "5.4"
print(dictionary_example["Grade3"])     # Output: "6.4"

# Dictionaries are mutable, meaning you can modify, add, or remove key-value pairs. 
# They provide a flexible and efficient way to store and retrieve data based on unique keys.

list_example = [123, "hi", 5.4, True, dictionary_example]
x = list_example[4]

print("A tuple:", tuple_example)
print("A dictionary:", dictionary_example)
print("A matrix:", matrix_example)
print("Grade1 from the dictionary:", x["Grade1"])

# Printing all elements of a list
for i in list_example:
    print(i)

# Printing all indices of a list
for i in range(len(list_example)):
    print(i)


### MATRIX
'''
In Python, a matrix is a two-dimensional data structure represented as a nested list. 
It consists of rows and columns, where each element is accessed using two indices: one for the row and one for the column.

The above example, matrix_example = [[0, 1], [0, 2], [0, 3]], represents a matrix. 
It is a nested list with three rows and two columns. 
Each element in the matrix is accessed using two indices. 
For example, matrix_example[0][1] would retrieve the value 1, which is in the first row and second column.

Matrices are commonly used in various numerical and scientific computations, such as linear algebra, image processing, and machine learning. 
Python provides several libraries, such as NumPy, that offer efficient matrix operations and functionalities.
'''

# Visual representation of the matrix [[0, 1], [0, 2], [0, 3]] :
'''
+---+---+
| 0 | 1 |
+---+---+
| 0 | 2 |
+---+---+
| 0 | 3 |
+---+---+
'''
