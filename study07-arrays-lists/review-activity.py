'''
Create a list that has these values ( 5, 1, 3, 4, 6, 7, 0 )
A ) Make this list a descending list;
B ) Add the value 2 and 4 to the list;
C ) Show the size of the list;
D ) Print to the screen the position of the value 5;
E ) Print to the screen the amount of value 4;
F ) Delete position two from the list and add the value 10 in its place;
G ) Print the list.
'''

arr = [5, 1, 3, 4, 6, 7, 0]

# A) Make the list a descending list
arr.sort(reverse=True)
print("Descending list:", arr)

# B) Add values 2 and 4 to the list
arr.append(2)
arr.append(4)
print("List after adding 2 and 4:", arr)

# C) Show the size of the list
size = len(arr)
print("Size of the list:", size)

# D) Print the position of the value 5
position_5 = arr.index(5)
print("Position of value 5:", position_5)

# E) Print the count of value 4
count_4 = arr.count(4)
print("Count of value 4:", count_4)

# F) Delete position two from the list and add the value 10 in its place
del arr[2]
arr.insert(2, 10)
print("List after deleting position 2 and adding 10:", arr)

# G) Print the list
print("Final list:", arr)
