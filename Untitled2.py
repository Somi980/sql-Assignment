#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question no: 1 Write a code to reverse a  string.


# In[1]:


def reverse_string(s):
    return s[::-1]

# Example usage
input_string = "Hello"
reversed_string = reverse_string(input_string)
print("Reversed String:", reversed_string)


# In[ ]:


Question no:2 Write a code to count the number of vowels in a string.


# In[3]:


def count_vowels(s):
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
input_string = "Hello World"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)


# In[ ]:


Question no 3: Write a code to check if a given string in a palindrome or not.


# In[4]:


def is_palindrome(s):
    # Convert the string to lowercase and remove spaces for accurate comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
input_string = "madam"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome")
else:
    print(f"'{input_string}' is not a palindrome")


# In[ ]:


Question no: 4  Write a code to check if two given strings are anagrams of each other.


# In[5]:


def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams")
else:
    print(f"'{string1}' and '{string2}' are not anagrams")


# In[ ]:


Question no: 5 Write a code to find all occurrences of a given substring within another string.


# In[6]:


def find_substring_occurrences(main_string, substring):
    occurrences = []
    start = 0
    
    # Use a loop to find the substring and record its positions
    while True:
        start = main_string.find(substring, start)
        if start == -1:  # If no more occurrences are found, exit the loop
            break
        occurrences.append(start)
        start += len(substring)  # Move start index to avoid overlapping matches
    
    return occurrences

# Example usage
main_string = "abracadabra"
substring = "abra"
positions = find_substring_occurrences(main_string, substring)

if positions:
    print(f"The substring '{substring}' is found at positions: {positions}")
else:
    print(f"The substring '{substring}' was not found.")


# In[ ]:


Question no:6  Write a code to perform basic string compression using the counts of repeated characters.


# In[7]:


def compress_string(s):
    compressed = []
    count = 1
    
    # Iterate through the string to count consecutive characters
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))  # Append the character and its count
            count = 1  # Reset count
    
    # Don't forget to add the last character and its count
    compressed.append(s[-1] + str(count))
    
    # Join the list into a compressed string
    compressed_string = ''.join(compressed)
    
    # Return the original string if compression doesn't make it shorter
    return compressed_string if len(compressed_string) < len(s) else s

# Example usage
input_string = "aabcccccaaa"
compressed_output = compress_string(input_string)
print("Compressed String:", compressed_output)


# In[ ]:


Question no:7 Write a code to determine if a string has all unique characters.


# In[8]:


def has_unique_characters(s):
    # Use a set to track unique characters
    char_set = set()
    
    # Iterate through the string and check for duplicates
    for char in s:
        if char in char_set:
            return False  # Duplicate found
        char_set.add(char)
    
    return True  # No duplicates found

# Example usage
input_string = "abcdefg"
if has_unique_characters(input_string):
    print(f"'{input_string}' has all unique characters.")
else:
    print(f"'{input_string}' does not have all unique characters.")


# In[ ]:


Question no:8  Write a code to convert a given string to uppercase or lowercase.


# In[9]:


def convert_case(s, to_upper=True):
    if to_upper:
        return s.upper()  # Convert to uppercase
    else:
        return s.lower()  # Convert to lowercase

# Example usage
input_string = "Hello World"

# Convert to uppercase
uppercase_string = convert_case(input_string, to_upper=True)
print("Uppercase:", uppercase_string)

# Convert to lowercase
lowercase_string = convert_case(input_string, to_upper=False)
print("Lowercase:", lowercase_string)


# In[ ]:


Question no:9  Write a code to count the number of words in a strings.


# In[10]:


def count_words(s):
    # Split the string by spaces to get a list of words
    words = s.split()
    return len(words)

# Example usage
input_string = "Hello, how are you doing today?"
word_count = count_words(input_string)
print("Number of words:", word_count)


# In[ ]:


Question no:10  Write a code to concatenate two strings without using the + operators


# In[11]:


def concatenate_strings(str1, str2):
    return "{}{}".format(str1, str2)

# Example usage
string1 = "Hello"
string2 = "World"
concatenated_string = concatenate_strings(string1, string2)
print("Concatenated String:", concatenated_string)


# In[ ]:


Question no:11  Write a code to remove all occurrences of a specific element from a list.


# In[12]:


def remove_element(lst, element):
    # Create a new list with all elements except the specified one
    return [item for item in lst if item != element]

# Example usage
my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_remove = 2
updated_list = remove_element(my_list, element_to_remove)

print("Updated List:", updated_list)


# In[ ]:


Question no: 12 Implement a code to find the second largest number in a given list of integers.


# In[13]:


def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for second largest
    
    # Remove duplicates by converting to a set
    unique_numbers = set(numbers)
    
    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None

    # Sort the unique numbers in descending order and get the second largest
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]

# Example usage
my_list = [3, 1, 4, 4, 5, 2]
second_largest = find_second_largest(my_list)

if second_largest is not None:
    print("Second Largest Number:", second_largest)
else:
    print("Not enough unique numbers to determine the second largest.")


# In[ ]:


Question no:13  Create a code to count the occurrences of each element in a list and return a dictionary
 with elements as key and their counts as values.


# In[14]:


def count_occurrences(lst):
    counts = {}  # Initialize an empty dictionary

    for item in lst:
        if item in counts:
            counts[item] += 1  # Increment count if item is already in dictionary
        else:
            counts[item] = 1  # Initialize count for new item

    return counts

# Example usage
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
occurrences = count_occurrences(my_list)

print("Occurrences:", occurrences)


# In[ ]:


Question no:14 Write a code to revere ' list in-place without using any
 built-in reverse functions.


# In[15]:


def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # Swap the elements at the left and right indices
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

# Example usage
my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)

print("Reversed List:", my_list)


# In[ ]:


Question no:15 Implement a code to find and remove duplicates from a list while preserving the original order of 
elements.


# In[16]:


def remove_duplicates(lst):
    seen = set()  # Set to keep track of seen elements
    unique_list = []  # List to store the unique elements

    for item in lst:
        if item not in seen:
            seen.add(item)  # Add to the set if it's not seen
            unique_list.append(item)  # Append to the unique list

    return unique_list

# Example usage
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
result = remove_duplicates(my_list)

print("List after removing duplicates:", result)


# In[ ]:


Question no:16  Create a code to check if a given list is sorted (either in ascending or descending order) or not.


# In[17]:


def is_sorted(lst):
    if len(lst) < 2:  # A list with less than 2 elements is considered sorted
        return True

    # Check for ascending order
    ascending = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
    # Check for descending order
    descending = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    
    return ascending or descending

# Example usage
my_list_asc = [1, 2, 3, 4, 5]
my_list_desc = [5, 4, 3, 2, 1]
my_list_unsorted = [1, 3, 2, 4]

print(f"Is the list {my_list_asc} sorted? {is_sorted(my_list_asc)}")  # True
print(f"Is the list {my_list_desc} sorted? {is_sorted(my_list_desc)}")  # True
print(f"Is the list {my_list_unsorted} sorted? {is_sorted(my_list_unsorted)}")  # False


# In[ ]:


Question no:17 Write a code to merge two sorted lists into a single sorted lists.


# In[18]:


def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    # Merge the two lists while there are elements in both
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # If there are remaining elements in list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If there are remaining elements in list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = merge_sorted_lists(list1, list2)

print("Merged Sorted List:", merged)


# In[ ]:


Question no:18 Implement a code to find the intersection of two given lists.


# In[19]:


def find_intersection(list1, list2):
    # Use a set for efficient look-up
    set2 = set(list2)
    intersection = [item for item in list1 if item in set2]
    return intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)

print("Intersection of the two lists:", intersection)


# In[ ]:


Question no:19 Create a code to find the union of two lists without duplicates.


# In[20]:


def find_union(list1, list2):
    # Use a set to automatically handle duplicates
    union_set = set(list1) | set(list2)
    return list(union_set)

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union = find_union(list1, list2)

print("Union of the two lists:", union)


# In[21]:


Question no:20 Write a code to shuffle a given list randomly  without using any
 built-in shuffle functions.


# In[22]:


import random

def shuffle_list(lst):
    # Create a copy of the original list to avoid modifying it
    shuffled = lst[:]
    
    # Implementing Fisher-Yates shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)  # Generate a random index
        # Swap the current element with the random element
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled

# Example usage
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)

print("Original List:", my_list)
print("Shuffled List:", shuffled_list)


# In[ ]:


Question no:21 Write a code that takes two tuples as input and returns a new tuple containing elements that are 
common to both input tuples.


# In[23]:


def common_elements(tuple1, tuple2):
    # Use set intersection to find common elements and convert it back to a tuple
    common = tuple(set(tuple1) & set(tuple2))
    return common

# Example usage
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
result = common_elements(tuple1, tuple2)

print("Common elements:", result)


# In[ ]:


Question no:22 Create a code that prompts the user to enter two sets of integers separated by  commas. Then, print the 
intersection of these two sets.


# In[ ]:


def get_set_from_input(prompt):
    # Get user input and convert it to a set of integers
    user_input = input(prompt)
    return set(map(int, user_input.split(',')))

def main():
    # Prompt the user for two sets of integers
    set1 = get_set_from_input("Enter the first set of integers (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of integers (separated by commas): ")
    
    # Find the intersection of the two sets
    intersection = set1 & set2
    
    # Print the result
    print("Intersection of the two sets:", intersection)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:


Question no:23  Write a code to concatenate two tuples. The function should take two tuples as input and return a new 
tuple containing elements from both input tuples.


# In[ ]:


def concatenate_tuples(tuple1, tuple2):
    # Concatenate the two tuples
    return tuple1 + tuple2

# Example usage
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = concatenate_tuples(tuple1, tuple2)

print("Concatenated Tuple:", result)


# In[ ]:


Question no:24  Develop a code that prompts the user to input two sets of strings. Then print the elements that are
present in the first set but not in the second set.


# In[ ]:


def get_set_from_input(prompt):
    # Get user input and convert it to a set of strings
    user_input = input(prompt)
    return set(user_input.split(','))

def main():
    # Prompt the user for two sets of strings
    set1 = get_set_from_input("Enter the first set of strings (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of strings (separated by commas): ")
    
    # Find the difference of the two sets (elements in set1 but not in set2)
    difference = set1 - set2
    
    # Print the result
    print("Elements in the first set but not in the second set:", difference)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:


Question no:25 Create a code that takes a tuple and two integers as input. The function should return a new tuple 
containing elements from the original tuple within the specified range of indices. 


# In[ ]:


def get_tuple_slice(original_tuple, start_index, end_index):
    # Return a new tuple containing elements from the specified index range
    return original_tuple[start_index:end_index]

# Example usage
input_tuple = (10, 20, 30, 40, 50, 60, 70)
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

result = get_tuple_slice(input_tuple, start, end)

print("New Tuple:", result)


# In[ ]:


Question no:26 def get_set_from_input(prompt):
    # Get user input and convert it to a set of characters
    user_input = input(prompt)
    return set(user_input)

def main():
    # Prompt the user for two sets of characters
    set1 = get_set_from_input("Enter the first set of characters: ")
    set2 = get_set_from_input("Enter the second set of characters: ")
    
    # Find the union of the two sets
    union = set1 | set2
    
    # Print the result
    print("Union of the two sets:", union)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:


Question no:27 Develop a code that takes a tuple of integers as input. The function should return the maximum and 
minimum values from the tuple using tuple unpacking.


# In[ ]:


def get_max_min(values):
    # Use built-in max and min functions to get the maximum and minimum values
    max_value = max(values)
    min_value = min(values)
    return max_value, min_value  # Return as a tuple

# Example usage
input_tuple = tuple(map(int, input("Enter a tuple of integers (separated by spaces): ").split()))
max_value, min_value = get_max_min(input_tuple)  # Unpacking the returned tuple

print("Maximum Value:", max_value)
print("Minimum Value:", min_value)


# In[ ]:


Question no:28 Create a code that defines two sets of integers. Then print the union intersection and difference of these 
two sets.


# In[ ]:


def main():
    # Define two sets of integers
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # Calculate union, intersection, and difference
    union = set1 | set2  # Union
    intersection = set1 & set2  # Intersection
    difference = set1 - set2  # Difference (elements in set1 but not in set2)

    # Print the results
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Union of the two sets:", union)
    print("Intersection of the two sets:", intersection)
    print("Difference (Set 1 - Set 2):", difference)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:


Question no:29  Write a code that takes a tuple and an element as input. The function should return the count of 
occurrences of the given element in the tuples.


# In[ ]:


def count_occurrences(input_tuple, element):
    # Count occurrences of the element in the tuple
    return input_tuple.count(element)

# Example usage
input_tuple = tuple(input("Enter a tuple of elements (separated by spaces): ").split())
element = input("Enter the element to count: ")

# If the input tuple contains integers, convert the element to int
if input_tuple and input_tuple[0].isdigit():
    input_tuple = tuple(map(int, input_tuple))
    element = int(element)

count = count_occurrences(input_tuple, element)

print(f"The element '{element}' occurs {count} times in the tuple.")


# In[ ]:


Question no:30  Develop a code that prompts the user to input two sets of strings. Then print the symmetric difference of 
these two sets.


# In[ ]:


def get_set_from_input(prompt):
    # Get user input and convert it to a set of strings
    user_input = input(prompt)
    return set(user_input.split(','))

def main():
    # Prompt the user for two sets of strings
    set1 = get_set_from_input("Enter the first set of strings (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of strings (separated by commas): ")
    
    # Calculate the symmetric difference of the two sets
    symmetric_difference = set1.symmetric_difference(set2)
    
    # Print the result
    print("Symmetric difference of the two sets:", symmetric_difference)

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:


Question no:31 Write a code that takes a list of words as input and returns a dictionary where the keys are unique words 
and the values are the frequencies of those words in the input lists.


# In[ ]:


def word_frequencies(words):
    # Create a dictionary to store word frequencies
    frequency_dict = {}
    
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1  # Increment count if the word is already in the dictionary
        else:
            frequency_dict[word] = 1  # Initialize count if it's a new word
    
    return frequency_dict

# Example usage
input_words = input("Enter a list of words (separated by spaces): ").split()
frequency_dict = word_frequencies(input_words)

print("Word Frequencies:", frequency_dict)


# In[ ]:


Question no:32 Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are 
common keys the values should be added togethers.


# In[ ]:


def merge_dictionaries(dict1, dict2):
    # Create a new dictionary to store the merged result
    merged_dict = dict1.copy()  # Start with the first dictionary
    
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add the values if the key exists
        else:
            merged_dict[key] = value  # Otherwise, add the new key-value pair
    
    return merged_dict

# Example usage
dict1 = eval(input("Enter the first dictionary (e.g., {'a': 1, 'b': 2}): "))
dict2 = eval(input("Enter the second dictionary (e.g., {'b': 3, 'c': 4}): "))

result = merge_dictionaries(dict1, dict2)

print("Merged Dictionary:", result)


# In[ ]:


Question no:33  Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of 
keys as input and return the corresponding value. If any of the keys do not exist in the dictionary the 
function should return None.


# In[ ]:


def access_nested_value(nested_dict, keys):
    # Initialize the current dictionary to the input nested dictionary
    current_dict = nested_dict
    
    for key in keys:
        # Check if the current key exists in the current dictionary
        if key in current_dict:
            current_dict = current_dict[key]  # Move to the next level
        else:
            return None  # Return None if the key does not exist
    
    return current_dict  # Return the final value if all keys are found

# Example usage
nested_dict = {
    'a': {
        'b': {
            'c': 42
        },
        'd': 10
    },
    'e': 5
}

keys = ['a', 'b', 'c']
value = access_nested_value(nested_dict, keys)

print("Value:", value)  # Output: Value: 42

# Test with a non-existing key
keys_non_existing = ['a', 'b', 'x']
value_non_existing = access_nested_value(nested_dict, keys_non_existing)

print("Value for non-existing keys:", value_non_existing)  # Output: Value for non-existing keys: None


# In[ ]:


Question no:34 Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You 
can choose whether to sort in ascending or descending orders.


# In[ ]:


def sort_dictionary_by_values(input_dict, descending=False):
    # Sort the dictionary by values
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=descending))
    return sorted_dict

# Example usage
input_dict = {
    'a': 3,
    'b': 1,
    'c': 2,
    'd': 4
}

# Choose sorting order
order = input("Sort in ascending or descending order? (a/d): ").strip().lower()
descending = True if order == 'd' else False

sorted_dict = sort_dictionary_by_values(input_dict, descending)

print("Sorted Dictionary:", sorted_dict)


# In[ ]:


Question no:35  Write a code that inverts a dictionary swapping keys and values. Ensure that the inverted dictionary 
correctly handles cases where multiple keys have the same value by storing the keys as a list in the 
inverted dictionary.


# In[ ]:


def invert_dictionary(original_dict):
    inverted_dict = {}
    
    for key, value in original_dict.items():
        # Check if the value is already a key in the inverted dictionary
        if value in inverted_dict:
            # If it exists, append the key to the list
            inverted_dict[value].append(key)
        else:
            # If it does not exist, create a new entry with the key as a list
            inverted_dict[value] = [key]
    
    return inverted_dict

# Example usage
input_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}

inverted_dict = invert_dictionary(input_dict)

print("Original Dictionary:", input_dict)
print("Inverted Dictionary:", inverted_dict)

