'''
Reverse the vowels in a text
Problem statement

Write a program that reverses ONLY the vowels in a given text, leaving every other character exactly where it is.

Vowels include:
"aeiouAEIOU"


Both uppercase and lowercase must be preserved.
Input format
- First line: An integer n, representing the number of lines.
- Next n lines: The actual text.
Example
Input
1
HEllo

Output
HollE

Why?

The consonants remain untouched.
___________________________________________________________________________________________________________________________________
'''

'''
Game plan : pehle vowels ko extract kre and unke indices store krle, fir vowels ko reverse kre, fir unhi same indices jispe 
vowels the uspe reversed vowels laga de
'''
'''
BUGGY SOLUTION LOL  

n=int(input("enter an integer representing the number of lines of text"))
s=input("Enter the sting")

v="aeiouAEIOU"
vow=""
index_ch=[]
for ch in s:
    if ch in v:
        index_ch.append(ch)
        vow=vow+ch

rev_vow=vow[::-1]
s[index_ch]= rev_vow

print(n)
print(s)
'''


def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    vow = []
    index_ch = []

    for i, ch in enumerate(s):   #to get both the index and the character
        if ch in vowels:
            index_ch.append(i)
            vow.append(ch)

    rev_vow = vow[::-1]

    s = list(s)

    for i in range(len(index_ch)):
        s[index_ch[i]] = rev_vow[i]

    return "".join(s)


# Calling part
n = int(input())

for _ in range(n):  #dummy variable
    s = input()
    print(reverse_vowels(s))





