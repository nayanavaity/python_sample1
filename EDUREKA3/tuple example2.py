# Creating tuples
empty_tuple = ()  # Empty tuple
single_element_tuple = (5,)  # Single element requires a comma
multiple_elements_tuple = (1, "Hello", 3.14)

# Accessing elements in a tuple
print(multiple_elements_tuple[0])  # Output: 1
print(multiple_elements_tuple[1])  # Output: "Hello"

# Nested tuple
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])  # Output: (2, 3)
print(nested_tuple[1][0])  # Output: 2

# Slicing a tuple
print(multiple_elements_tuple[1:])  # Output: ("Hello", 3.14)

# Length of a tuple
print(len(multiple_elements_tuple))  # Output: 3

# Tuple unpacking
a, b, c = multiple_elements_tuple
print(a)  # Output: 1
print(b)  # Output: "Hello"
print(c)  # Output: 3.14

# Iterating through a tuple
for item in multiple_elements_tuple:
    print(item)

# Tuples are immutable
# The following would raise an error:
# multiple_elements_tuple[0] = 10