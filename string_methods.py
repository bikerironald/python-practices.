name = 'bikeri'
print(name[3])
# Indexing and Slicing Strings:
"""Understanding how to access individual characters within a string
(indexing) and extracting portions of a string (slicing) is crucial. Python
uses zero-based indexing, meaning the first character is at index 0."""

message = "Python is Fun!"
print(message[::9])

# Indexing and slicing strings
message = "Python is Fun!"
print(message[0])         # Output: P (first character)
print(message[-1])        # Output: ! (last character)
print(message[7:9])       # Output: is (slicing from index 7 to 9)
print(message[:6])        # Output: Python (slicing from the beginning)