"""
sting methods are like functions which are used for manipulation of stings 
such as, convering cases, removinf=g white spaces, replacing characters, splitting, joining, and more.
#upper() - Converts all characters in a string to uppercase.
#lower() - Converts all characters in a string to lowercase.
#strip() - Removes leading and trailing whitespace from a string.
#replace() - Replaces a specified substring with another substring.
#split() - Splits a string into a list of substrings based on a specified delimiter.
#join() - Joins a list of strings into a single string with a specified delimiter.
#find() - Returns the index of the first occurrence of a specified substring in a string.
#count() - Returns the number of occurrences of a specified substring in a string.
#startswith() - Checks if a string starts with a specified substring.
#endswith() - Checks if a string ends with a specified substring.
#capitalize() - Capitalizes the first character of a string.
#title() - Converts the first character of each word in a string to uppercase.
#swapcase() - Swaps the case of all characters in a string (uppercase to lowercase and vice versa).
#zfill() - Pads a numeric string with zeros on the left to fill a specified width.

"""
s = "helllo world"
print(s.upper)
print(s.lower())
print(s.strip())
print(s.replace("l","d"))
print(s.split("l"))
print(s.join("kaladhar"))
print(s.find("h"))
print(s.count("l"))
print(s.startswith("h"))
print(s.endswith("d"))
print(s.isdigit())
print(s.isdecimal())
print(s.isupper())
print(s.islower())
print(s.isspace())
print(s.isnumeric())
print(s.isalpha)
print(s.zfill(10))
print(s.swapcase())