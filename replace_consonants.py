''' 
Write a program that accepts a string and replaces every consonant with the hash character (#).

The following must remain unchanged:
- Vowels: a, e, i, o, u
- Numbers
- Symbols
- Spaces
Important: The vowel check must be case-insensitive, but preserve the original case of characters that remain.
Examples
Example 1
Input:
Python 3.10

Output:
#y##o# 3.10
'''

def replace_consonant(s):
    c="bcdfghjklmnpqrstvwxyz"
    result=""
    for char in s:
        if char.lower() in c:
            result+="#"
        else:
            result+=char
    return result


print(replace_consonant("Python 3.10"))
print(replace_consonant("Hello World!"))

#_________________________________________________________________________________________________________________

def replace_consonant(s):
    vowels = "aeiouAEIOU"
    result = []

    for char in s:
        if char.isalpha() and char not in vowels:
            result.append("#")
        else:
            result.append(char)

    return "".join(result)