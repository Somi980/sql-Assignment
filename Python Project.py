#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Ques no 1:Explain the key features of Python that make it a popular choice for programming.

Python is one of the most popular programming languages due to its versatility, simplicity, and efficiency. Here are some of the key features that make Python a top choice:

1.Easy to Learn and Use: Python has a clean and simple syntax that closely resembles English, making it beginner-friendly. 
    This reduces the learning curve for new programmers.

2.Interpreted Language: Python is an interpreted language, meaning that 
    code is executed line-by-line, which helps with debugging and allows developers to test and iterate code quickly.

3.Cross-Platform Compatibility: Python is platform-independent,
    which means code written in Python can run on various operating systems like Windows, macOS, and Linux without 
    requiring modifications.

4.Extensive Standard Library: Python comes with a vast standard library that
    includes modules and functions for handling everything from file I/O, networking, regular expressions, 
    to web service tools, and many others. This saves time for developers by providing pre-built functionality.

5.Dynamic Typing: In Python, you don't need to declare the data type of variables.
    This feature provides more flexibility, especially during rapid development.

6.Large and Active Community: Python has a large, active community, 
    which means abundant resources such as tutorials, libraries, frameworks, and forums are available for developers.

7.Vast Ecosystem of Libraries and Frameworks: Python's ecosystem includes powerful libraries and frameworks for 
    a wide range of tasks, including web development (e.g., Django, Flask), data analysis (e.g., pandas, NumPy),
    machine learning (e.g., TensorFlow, scikit-learn), and more.

8.Readability and Maintainability: Python emphasizes code readability with its clear syntax and indentation, 
    which makes the code easier to maintain and update.

9.Strong Integration Capabilities: Python can easily integrate with other languages such as
    C, C++, and Java. It also supports a wide range of APIs and web services, making it suitable 
    for building complex applications.

These features collectively contribute to Python’s wide adoption in areas like
web development, data science, automation, artificial intelligence, and more.


# In[ ]:


Ques no 2:  Describe the role of predefined keywords in Python and provide examples of how they are used in a 
programe
    Predefined keywords, also known as reserved keywords, are words that have specific meanings in Python and cannot be used as variable names, function names, or identifiers. These keywords define the structure and syntax of the Python language and are integral to writing valid Python code. Each keyword performs a particular function within the language.

Here’s a description of the role of predefined keywords and how they are used in a program:

Key Roles of Predefined Keywords in Python:
Control Flow: Keywords such as if, else, elif, for, and while help control the flow of execution in a program.
Data Types and Values: Keywords like True, False, None represent boolean values and the absence of value.
Function and Class Definitions: def is used to define a function, and class is used to define a class.
Exception Handling: Keywords such as try, except, and finally are used to handle exceptions and errors in the program.
Logical and Comparison Operations: Keywords such as and, or, not, in, and is are used for logical and comparison operations.
Examples of Common Python Keywords:
1. if, elif, else (Control Flow):
These keywords are used to execute code conditionally.

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
    
    In this example, if, elif, and else control the flow of the program based on the value of x.

2. for, while (Loops):
These keywords are used to repeat a block of code multiple times.
# Using 'for' loop
for i in range(3):
    print(i)

# Using 'while' loop
count = 0
while count < 3:
    print(count)
    count += 1
3. def (Function Definition):
This keyword is used to define a function.
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
Here, def is used to define a function named greet.

4. class (Class Definition):
This keyword is used to define a class in object-oriented programming.
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Buddy")
print(dog.bark())
5. try, except, finally (Exception Handling):
These keywords help handle exceptions to prevent program crashes
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")
Here, try block attempts to divide by zero, except catches the error, and finally executes code regardless of the exception.
Summary:
Predefined keywords in Python are integral to its syntax and function. 
They define the structure of the language and perform essential tasks such as controlling the 
flow of a program, defining functions, and handling exceptions. 
Understanding how to use these keywords is crucial for writing effective Python programs.


# In[ ]:


Ques no:3 Compare and contrast mutable and immutable objects in Python with examples
Mutable Objects:
Mutable objects can be changed after they are created, meaning you can alter their contents without changing their identity (memory address).

Example 1: List (Mutable Object)


# In[1]:


my_list = [1, 2, 3]
print("Original list:", my_list)

my_list.append(4)
print("Modified list:", my_list)


# In[ ]:


Example 2: Dictionary (Mutable Object)


# In[2]:


my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print("Modified dictionary:", my_dict)


# In[ ]:


Immutable Objects:
Immutable objects cannot be changed after creation. Any modification results in a new object being created, while the original object remains unchanged.

Example 1: String (Immutable Object)


# In[3]:


my_str = "Hello"
print("Original string:", my_str)

new_str = my_str + " World"
print("New string:", new_str)
print("Original string remains unchanged:", my_str)


# In[ ]:


Example 2: Tuple (Immutable Object)


# In[4]:


my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

# Attempting to change an element in a tuple will raise an error
# my_tuple[0] = 4  # This would raise a TypeError


# In[ ]:


Summary of Key Differences:
Mutable objects (e.g., lists, dictionaries) can be changed in-place, 
which makes them suitable for tasks where modifications are frequent.
Immutable objects (e.g., strings, tuples) cannot be modified after creation.
Any attempt to change them results in the creation of a new object.
Mutability also affects how objects behave when passed into functions, with mutable objects allowing
changes to persist outside the function, while immutable objects do not.


# In[ ]:


Ques no:4 Discuss the different types of operators in Python and provide examples of how they are used
    Python provides a rich set of operators that allow you to perform operations on variables and values. 
    Operators are symbols that trigger operations like addition, comparison, or logical decision-making. 
    Here’s an overview of the different types of operators in Python with examples:



# In[ ]:


1. Arithmetic Operators


# In[5]:


a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.33
print(a // b) # Output: 3
print(a % b)  # Output: 1
print(a ** b) # Output: 1000


# In[ ]:


2. Comparison (Relational) Operators


# In[ ]:


Comparison operators compare two values and return a Boolean value (True or False).


# In[19]:


x = 5
y = 10

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= 5)  # Output: True
print(x <= 10) # Output: True


# In[ ]:


3. Logical Operators
Logical operators are used to combine conditional statements.


# In[20]:


x = 5
y = 10

print(x > 3 and y < 20)  # Output: True
print(x > 10 or y < 20)  # Output: True
print(not(x > 3))        # Output: False


# In[ ]:


4. Assignment Operators
Assignment operators are used to assign values to variables.


# In[21]:


x = 10

x += 5  # x = x + 5
print(x)  # Output: 15

x *= 2  # x = x * 2
print(x)  # Output: 30


# In[22]:


5. Bitwise Operators
Bitwise operators operate on bits and perform bit-by-bit operations.


# In[23]:


x = 5  # Binary: 0101
y = 3  # Binary: 0011

print(x & y)  # Output: 1 (Binary: 0001)
print(x | y)  # Output: 7 (Binary: 0111)
print(x ^ y)  # Output: 6 (Binary: 0110)
print(~x)     # Output: -6 (Binary: Inverted bits)
print(x << 2) # Output: 20 (Binary: 10100)
print(x >> 2) # Output: 1 (Binary: 0001)


# In[ ]:


Summary:
Python operators play a vital role in performing computations, making logical decisions, and manipulating data.
By understanding and utilizing these operators effectively, you can build more efficient and readable programs.


# In[ ]:


Ques no:5  Explain the concept of type casting in Python with examples
Type casting in Python refers to the process of converting one data type into another. 
It allows you to change the type of a variable to perform operations that require variables to be of 
the same type, or to ensure compatibility across different parts of the program.

There are two types of type casting in Python:

1.Implicit Type Casting
2.Explicit Type Casting


# In[ ]:


1. Implicit Type Casting
In implicit type casting, Python automatically converts one data type to another without any user intervention. 
This usually happens when two different types are involved in an operation, 
and Python automatically upcasts the smaller data type into the larger one (e.g., converting an int to a float).


# In[ ]:


# Implicit conversion from int to float
num_int = 10
num_float = 2.5

result = num_int + num_float
print(result)           # Output: 12.5
print(type(result))     # Output: <class 'float'>



# In[ ]:


2. Explicit Type Casting
In explicit type casting, also known as type conversion, the user manually converts the data type of a variable using Python's built-in functions.

Common type casting functions:

int() – Converts a value to an integer.
float() – Converts a value to a float.
str() – Converts a value to a string.
list() – Converts a value (like a tuple) to a list.
tuple() – Converts a value (like a list) to a tuple.
bool() – Converts a value to a boolean.


# In[ ]:


1. Integer to Float


# In[ ]:


num = 5
num_float = float(num)
print(num_float)         # Output: 5.0
print(type(num_float))   # Output: <class 'float'>


# In[ ]:


2. Float to Integer
When casting a float to an integer, the decimal part is truncated.


# In[ ]:


num = 7.9
num_int = int(num)
print(num_int)           # Output: 7
print(type(num_int))     # Output: <class 'int'>


# In[ ]:


3. String to Integer/Float
You can convert a string representation of a number to an integer or float. 
The string must represent a valid number, or it will raise an error.


# In[ ]:


str_num = "100"
int_num = int(str_num)
float_num = float(str_num)
print(int_num)           # Output: 100
print(float_num)         # Output: 100.0


# In[ ]:


4. Integer/Float to String
Converting an integer or float to a string is useful when concatenating numbers with text.


# In[ ]:


num = 42
str_num = str(num)
print(str_num)           # Output: '42'
print(type(str_num))     # Output: <class 'str'>


# In[ ]:


Ques no: 6 How do conditional statements work in Python? Illustrate with examples


# In[ ]:


Conditional statements in Python allow you to execute specific blocks of code
based on whether a certain condition or set of conditions is true or false. 
Python supports several conditional statements: if, elif, and else. 
    These statements control the flow of the program by branching it into different paths depending on the conditions specified.

Syntax:
if statement: Executes a block of code if the condition is true.
elif statement: Checks another condition if the previous if condition is false.
else statement: Executes a block of code if all the previous conditions are false


# In[ ]:


if condition:
    # block of code executed if the condition is True
elif another_condition:
    # block of code executed if the 'if' condition is False and this condition is True
else:
    # block of code executed if all previous conditions are False


# In[ ]:


1. if Statement
The if statement checks whether a condition is true, and if so, executes the indented block of code under it.

Example:


# In[6]:


age = 18

if age >= 18:
    print("You are eligible to vote.")


# In[ ]:


2. if-else Statement
An if-else statement adds a default block of code to execute if the if condition is false.

Example:


# In[7]:


age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# In[ ]:


3. if-elif-else Statement
The elif (short for "else if") statement allows for multiple conditions. 
If the if condition is False, Python checks the elif condition. You can have multiple elif statements. 
The else block executes if none of the conditions are true.

Example:


# In[8]:


marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")


# In[ ]:


4. Nested if Statements
You can nest if statements inside one another to check more complex conditions.

Example:


# In[9]:


age = 20
citizenship = "India"

if age >= 18:
    if citizenship == "India":
        print("You are eligible to vote in India.")
    else:
        print("You are not eligible to vote in India.")
else:
    print("You are not eligible to vote.")


# In[ ]:


5. Multiple Conditions Using Logical Operators (and, or, not)
You can combine multiple conditions using logical operators.

and: Both conditions must be true for the block to execute.
or: Either condition can be true for the block to execute.
not: Reverses the condition's truth value.
Example with and:


# In[10]:


age = 20
citizenship = "India"

if age >= 18 and citizenship == "India":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# In[ ]:


Ques no:7 Describe the different types of loops in Python and their use cases with examples.


# In[ ]:


In Python, loops are used to execute a block of code repeatedly, either for a specific number of iterations or while 
a condition is true. Python provides two primary types of loops: for loops and while loops. 
    Let’s explore both in detail along with their use cases.

1. for Loop
The for loop in Python is used to iterate over a sequence (like a list, tuple, string, or range). 
It is particularly useful when the number of iterations is known in advance.

Syntax:


# In[11]:


for item in sequence:
    # block of code
    Use Cases:
Iterating over lists, tuples, or strings.
Repeating a block of code for a known number of times using range().
Processing items in a collection or performing operations over a sequence.
Example 1: Iterating over a list


# In[12]:


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# In[ ]:


Example 2: Using range() in a for loop


# In[13]:


# Prints numbers from 0 to 4
for i in range(5):
    print(i)


# In[ ]:


Example 3: Iterating over a string


# In[ ]:


for char in "Python":
    print(char)


# In[ ]:


2. while Loop
The while loop executes a block of code as long as the specified condition is True. 
It is useful when the number of iterations is not known in advance and you want to keep looping based on a condition.

Syntax:


# In[ ]:


Example 1: Basic while loop


# In[14]:


counter = 0
while counter < 5:
    print(counter)
    counter += 1


# In[ ]:


3. break Statement
The break statement is used to exit a loop prematurely, regardless of the condition. 
It is commonly used to stop loops based on a certain condition.

Example: Using break in a while loop


# In[15]:


counter = 0
while counter < 10:
    if counter == 5:
        break  # Exit the loop when counter is 5
    print(counter)
    counter += 1


# In[ ]:


4. continue Statement
The continue statement skips the rest of the current iteration and moves to the next iteration of the loop.

Example: Skipping even numbers in a loop


# In[16]:


for i in range(6):
    if i % 2 == 0:
        continue  # Skip the rest of the loop when i is even
    print(i)


# In[ ]:


5. else with Loops
Python allows the use of an else clause with loops. 
The else block is executed when the loop completes normally (without being terminated by break).

Example: else with for loop


# In[17]:


for i in range(5):
    print(i)
else:
    print("Loop completed")


# In[ ]:


6. Nested Loops
A loop inside another loop is called a nested loop. 
Nested loops are useful when working with multidimensional data structures 
like lists of lists (matrices) or performing repetitive operations at multiple levels.

Example: Nested for loop


# In[18]:


for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i = {i}, j = {j}")


# In[ ]:


Use Cases for Loops:
for Loop:
1.Iterating over items in a list, string, tuple, or dictionary.
2.Repeating a block of code for a defined number of iterations.
3.Processing data in bulk (e.g., reading files line by line).
while Loop:
1.Repeatedly executing code until a specific condition is met.
2.Handling cases where the number of iterations is unknown.
3.Continuously waiting for user input or sensor data.

