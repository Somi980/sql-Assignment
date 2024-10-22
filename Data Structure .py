#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question no 1: Discuss string slicing and provide examples.


# In[ ]:


String slicing in Python allows you to extract a substring from a string by specifying a range of indices. The syntax is:


# In[1]:


string[start:end:step]

start: The starting index (inclusive, default is 0).
end: The ending index (exclusive).
step: The interval between characters (default is 1).


# In[ ]:


Examples:


# In[ ]:


1: Basic Slicing:


# In[2]:


text = "Hello, World!"
print(text[0:5])  # Output: 'Hello'


# In[ ]:


2: Slicing with Step:


# In[ ]:


text = "abcdefg"
print(text[::2])  # Output: 'aceg' (every second character)


# In[ ]:


3: Negative Indexing:


# In[ ]:


text = "Python"
print(text[-6:-1])  # Output: 'Pytho' (negative indices count from the end)


# In[ ]:


4: Reversing a String:


# In[ ]:


text = "Hello"
print(text[::-1])  # Output: 'olleH'


# In[ ]:


Conclusion:
String slicing provides a flexible way to access parts of a string, using positive or negative indices and optional steps.


# In[ ]:


Question no: 2 Explain the key features of lists in Python.


# In[ ]:


Key Features of Lists in Python:

Ordered: Lists maintain the order of elements, meaning the position of each item is fixed.

Example: [1, 2, 3] - 1 is at index 0, 2 is at index 1, and so on.
Mutable: Lists are mutable, meaning their elements can be changed after creation.


# In[3]:


lst = [1, 2, 3]
lst[1] = 5  # lst becomes [1, 5, 3]


# In[ ]:


Heterogeneous Elements: A list can contain elements of different data types, such as integers, strings, or even other lists.

Example: [1, "hello", 3.14, [4, 5]]
Indexing and Slicing: Lists support indexing (both positive and negative) and slicing for accessing subsets of elements.

Example: lst[0] gives the first element, lst[-1] gives the last element.
List Comprehensions: Python supports list comprehensions, which provide a concise way to create lists.

Example: [x**2 for x in range(5)] results in [0, 1, 4, 9, 16]


# In[ ]:


Question no: 3  Describe how to access, modify, and delete elements in a list with examples.


# In[ ]:


Accessing Elements in a List:
You can access elements in a list using indexing or slicing.

Indexing: Access a single element using its index (starting from 0).


# In[ ]:


lst = [10, 20, 30, 40]
print(lst[1])  # Output: 20 (second element)
print(lst[-1])  # Output: 40 (last element)


# In[ ]:


Slicing: Access multiple elements by specifying a range.


# In[ ]:


print(lst[1:3])  # Output: [20, 30] (elements from index 1 to 2)


# In[ ]:


Modifying Elements in a List:
You can modify elements by directly assigning new values to specific indices.

Modifying by Index:


# In[ ]:


lst[2] = 35  # Modifies the element at index 2
print(lst)  # Output: [10, 20, 35, 40]


# In[ ]:


Modifying a Slice:


# In[ ]:


lst[1:3] = [25, 45]  # Replaces elements at index 1 and 2
print(lst)  # Output: [10, 25, 45, 40]


# In[ ]:


Deleting Elements in a List:
You can delete elements using the del statement, the remove() method, or the pop() method.

Using del: Deletes an element by its index.


# In[ ]:


del lst[1]  # Deletes the element at index 1
print(lst)  # Output: [10, 45, 40]


# In[ ]:


Using remove(): Removes the first occurrence of a specific value.


# In[ ]:


lst.remove(45)  # Removes the element with value 45
print(lst)  # Output: [10, 40]


# In[ ]:


Question no: 4 Compare and contrast tuples and lists with examples.


# In[ ]:


Mutability: Lists can be modified (adding, removing, or changing elements), while tuples are fixed once created.
Use Cases: Use lists for collections that may change over time. Use tuples for data that should remain constant, 
    such as coordinates or fixed configurations.
Performance: Tuples are generally faster to access and use less memory because they are immutable.


# In[ ]:


List:


# In[ ]:


my_list = [1, 2, 3, 4]
my_list[1] = 10  # Modifying element at index 1
print(my_list)  # Output: [1, 10, 3, 4]
my_list.append(5)  # Adding a new element
print(my_list)  # Output: [1, 10, 3, 4, 5]


# In[ ]:


Tuples:


# In[ ]:


my_tuple = (1, 2, 3, 4)
# my_tuple[1] = 10  # This would raise a TypeError because tuples are immutable
print(my_tuple)  # Output: (1, 2, 3, 4)


# In[ ]:


Question no: 5 Describe the key features of sets and provide examples of their use.
    Key Features of Sets in Python:

Unordered: Sets do not maintain any order of elements. Each time you print a set, 
    the elements might appear in a different order.

Example: {3, 1, 4} might be displayed as {1, 3, 4}.
Unique Elements: Sets automatically remove duplicates and only store unique elements.



# In[ ]:


my_set = {1, 2, 2, 3}
print(my_set)  # Output: {1, 2, 3}


# In[ ]:


Mutable: Sets are mutable, meaning you can add or remove elements after creation (except for frozensets, which are immutable).


# In[ ]:


my_set.add(4)  # Adds 4 to the set
my_set.remove(1)  # Removes 1 from the set


# In[ ]:


No Indexing or Slicing: Since sets are unordered, you cannot access elements by index or slice like lists or tuples.

Example: my_set[0] will raise a TypeError.


# In[ ]:


Examples of Set Use:
Removing Duplicates:


# In[ ]:


nums = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums)
print(unique_nums)  # Output: {1, 2, 3, 4}


# In[ ]:


Set Operations:


# In[ ]:


setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA.difference(setB))  # Output: {1, 2} (elements in setA but not in setB)
print(setA.symmetric_difference(setB))  # Output: {1, 2, 4, 5}


# In[ ]:


Conclusion:
Sets are useful when you need unique elements, perform mathematical operations, or want efficient membership tests. 
They offer high-performance operations for union,intersection, and difference, 
but do not support indexing or order-based operations.


# In[ ]:


Question no: 6  Discuss the use cases of tuples and sets in Python programming.


# In[ ]:


Use Cases of Tuples in Python:
Fixed Data: Tuples are ideal for storing data that should not be changed after creation. 
    Examples include coordinates, RGB color codes, or database records.

Example:


# In[ ]:


coordinates = (10, 20)
rgb_color = (255, 0, 0)


# In[ ]:


Return Multiple Values from Functions: Tuples are often used to return multiple values from a function.

Example:


# In[ ]:


def get_dimensions():
    return (1920, 1080)
width, height = get_dimensions()


# In[ ]:


Dictionary Keys: Since tuples are immutable, they can be used as keys in dictionaries
    (unlike lists which are mutable and can't be dictionary keys).

Example:


# In[ ]:


location_data = {("latitude", "longitude"): "Point A"}


# In[ ]:


Use Cases of Sets in Python:
Removing Duplicates: Sets automatically remove duplicate values, making them perfect for 
    filtering unique elements from a collection.

Example:


# In[ ]:


nums = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums)  # {1, 2, 3, 4}


# In[ ]:


Membership Testing: Sets offer a highly efficient way to test whether an item 
    is present or not, especially in large collections.

Example:


# In[ ]:


items = {"apple", "banana", "cherry"}
print("banana" in items)  # Output: True


# In[ ]:


Mathematical Set Operations: Sets are useful for performing operations like union, intersection,
    and difference between collections.

Example:


# In[ ]:


setA = {1, 2, 3}
setB = {3, 4, 5}
union_set = setA.union(setB)  # {1, 2, 3, 4, 5}


# In[ ]:


Question no:7 Describe how to add, modify, and delete items in a dictionary with examples.


# In[ ]:


Adding, Modifying, and Deleting Items in a Python Dictionary
1. Adding Items to a Dictionary
You can add new key-value pairs by assigning a value to a key. If the key already exists, the value is updated (modified).

Example:


# In[ ]:


# Creating a dictionary
student = {"name": "John", "age": 21}

# Adding a new key-value pair
student["grade"] = "A"
print(student)  # Output: {'name': 'John', 'age': 21, 'grade': 'A'}


# In[ ]:


2. Modifying Items in a Dictionary
To modify an existing item, simply assign a new value to an existing key.

Example:


# In[ ]:


# Modifying the value of an existing key
student["age"] = 22
print(student)  # Output: {'name': 'John', 'age': 22, 'grade': 'A'}


# In[ ]:


3. Deleting Items from a Dictionary
You can remove items from a dictionary using the del statement, pop() method, or popitem() method.

Using del: Removes the item by its key.


# In[ ]:


del student["grade"]
print(student)  # Output: {'name': 'John', 'age': 22}


# In[ ]:


Using pop(): Removes the item and returns the value of the key.


# In[ ]:


age = student.pop("age")
print(student)  # Output: {'name': 'John'}
print(age)  # Output: 22


# In[ ]:


Using popitem(): Removes and returns the last inserted key-value pair


# In[ ]:


student["major"] = "Physics"
last_item = student.popitem()
print(student)  # Output: {'name': 'John'}
print(last_item)  # Output: ('major', 'Physics')


# In[ ]:


Question no 8: Discuss the importance of dictionary keys belong immutable and provide examples
    Importance of Dictionary Keys Being Immutable in Python
In Python, dictionary keys must be immutable because dictionaries use a hashing mechanism to store and 
retrieve values efficiently. 
This hashing requires that the keys remain constant so that their hash value doesn't change
over time, ensuring fast lookups. If keys were mutable, changes to their values could break this hash-based mechanism, 
leading to unpredictable behavior or errors.

Key Reasons for Immutability of Dictionary Keys:
Hashable Keys for Efficient Lookups:

Python dictionaries use a hash table to store key-value pairs. Keys are hashed, and the resulting hash value
is used to quickly locate the associated value.
For this system to work reliably, keys must remain the same after being hashed. 
If mutable objects like lists were allowed as keys, changing the object after it was used as a key would change its
hash value, leading to incorrect lookups.
Consistency:

Immutable keys ensure that the dictionary remains stable throughout its lifecycle. 
The consistency provided by immutability prevents unexpected changes in key values, making the dictionary more reliable.
Avoiding Collisions:

If keys were mutable, modifying a key could result in two different keys having the same hash value, 
causing a collision and incorrect retrieval of values.


# In[ ]:


Examples of Immutable and Mutable Keys:
Immutable Keys (Allowed):

Strings, numbers, and tuples (with only immutable elements) can be used as dictionary keys.


# In[ ]:


my_dict = {
    "name": "Alice",  # String key
    42: "age",        # Integer key
    (1, 2): "coordinates"  # Tuple key (tuple is immutable)
}
print(my_dict)  # Output: {'name': 'Alice', 42: 'age', (1, 2): 'coordinates'}


# In[ ]:


Mutable Keys (Not Allowed):

Lists, dictionaries, and other mutable types cannot be used as dictionary keys 
because they can be modified, and their hash values would change.


# In[ ]:


my_dict = {}
my_list = [1, 2, 3]

# Using a list as a key will raise a TypeError because lists are mutable
# my_dict[my_list] = "value"  # This will raise a TypeError: unhashable type: 'list'


# In[ ]:


Example of Mutable Objects Leading to Errors:


# In[ ]:


# Trying to use a list as a key
try:
    my_dict = {[1, 2]: "value"}  # This will raise a TypeError
except TypeError as e:
    print(e)  # Output: unhashable type: 'list'


# In[ ]:


Immutable Tuple Example:


# In[ ]:


# Tuples can be keys, but all elements within the tuple must also be immutable
my_dict = {("x", 1): "point1", ("y", 2): "point2"}
print(my_dict[("x", 1)])  # Output: "point1"

