'''
# Create a list with the range() function:
    range( [i, ] f [, p] )
        [] - represents the optional part of the syntax.
        i - initial value. Optional value with default 0.
        f - final value. Mandatory value.
        p - step or increment. Optional value with default 1.
        OBS: Arguments i and p are optional.

The range() function defines a range of integer values.
Associated with list(), it creates a list with the range values.
The range() function can have 1 to 3 arguments:
     range(n) 	
- Generates a sequence from 0 to n-1 from 1 to 1;
     range(i, n)
- Generates a sequence from i to n-1 from 1 to 1;
     range(i, n, p)
- Generates a sequence from i to n-1 with interval p between the numbers.
'''

lista1 = list(range(5))  
print(lista1) # OUTPUT: [0, 1, 2, 3, 4] ---> 5 elements

lista2 = list(range(3, 8))   
print(lista2) # OUTPUT: [3, 4, 5, 6, 7] ---> 5 elements
 
# Create a list
lista3 = list(range(2, 11, 3)) 
print(lista3) # OUTPUT: [2, 5, 8] ---> 3 elements
print(type(lista3)) # OUTPUT: <class 'list'>

# Did not create the list ---> To create a list, you need to use list() instead of range()
lista4 = range(5)     	
print(lista4) # OUTPUT: range(0, 5)      
print(type(lista4)) # OUTPUT: <class 'range'>

