'''
str ; list ; typle; complex ; int ; float ; '
'bool ; bytes ; bytearray    ; memoryview ; nonetype ; range'
'frozenset ; set ; dict'
'''
''''
1. str (String)
Description: A sequence of characters enclosed in single (' '), double (" "), or triple (''' ''' or """ """) quotes.

Use Case: Used for text manipulation.

Example:

python
Copy
name = "Python"
print(name[0])  # Output: P
print(len(name))  # Output: 6
2. list
Description: An ordered, mutable (changeable) collection of items. Items can be of different types.

Use Case: Used for storing and manipulating sequences of data.

Example:

python
Copy
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds "orange" to the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
3. tuple
Description: An ordered, immutable (unchangeable) collection of items. Similar to a list but cannot be modified after creation.

Use Case: Used for fixed data that shouldn't change.

Example:

python
Copy
coordinates = (10, 20)
print(coordinates[0])  # Output: 10
4. complex
Description: Represents complex numbers in the form a + bj, where a is the real part and b is the imaginary part.

Use Case: Used in mathematical computations involving complex numbers.

Example:

python
Copy
z = 3 + 4j
print(z.real)  # Output: 3.0
print(z.imag)  # Output: 4.0
5. int (Integer)
Description: Represents whole numbers (positive or negative) without a fractional component.

Use Case: Used for counting, indexing, and mathematical operations.

Example:

python
Copy
num = 42
print(num + 8)  # Output: 50
6. float (Floating-Point Number)
Description: Represents real numbers (numbers with a decimal point).

Use Case: Used for calculations requiring precision.

Example:

python
Copy
pi = 3.14159
print(pi * 2)  # Output: 6.28318
7. bool (Boolean)
Description: Represents truth values: True or False.

Use Case: Used in conditional statements and logical operations.

Example:

python
Copy
is_python_fun = True
if is_python_fun:
    print("Python is fun!")  # Output: Python is fun!
8. bytes
Description: An immutable sequence of bytes (integers between 0 and 255).

Use Case: Used for binary data, such as reading/writing files in binary mode.

Example:

python
Copy
data = b"Hello"
print(data[0])  # Output: 72 (ASCII value of 'H')
9. bytearray
Description: A mutable sequence of bytes (similar to bytes but can be modified).

Use Case: Used when you need to modify binary data.

Example:

python
Copy
data = bytearray(b"Hello")
data[0] = 74  # Change 'H' to 'J'
print(data)  # Output: bytearray(b'Jello')
10. memoryview
Description: Provides a view of the memory of an object (e.g., bytes or bytearray) without copying the data.

Use Case: Used for efficient memory access in large datasets.

Example:

python
Copy
data = bytearray(b"Hello")
view = memoryview(data)
print(view[0])  # Output: 72
11. NoneType
Description: Represents the absence of a value or a null value. The only possible value is None.

Use Case: Used to indicate that a variable has no value.

Example:

python
Copy
result = None
if result is None:
    print("No result found.")  # Output: No result found.
12. range
Description: Represents an immutable sequence of numbers, commonly used for looping.

Use Case: Used in for loops to iterate over a sequence of numbers.

Example:

python
Copy
for i in range(5):
    print(i)  # Output: 0 1 2 3 4
13. frozenset
Description: An immutable version of a set. It cannot be modified after creation.

Use Case: Used when you need a set that shouldn't change.

Example:

python
Copy
frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})
14. set
Description: An unordered, mutable collection of unique elements.

Use Case: Used for operations like union, intersection, and difference.

Example:

python
Copy
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}
15. dict (Dictionary)
Description: An unordered, mutable collection of key-value pairs.

Use Case: Used for storing and retrieving data using keys.

Example:

'''         
import random
print(random.randrange(1,10))