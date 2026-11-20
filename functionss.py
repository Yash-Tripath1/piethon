'''
Sum of squares and absolute difference
Write a function:
def sum_squares_abs_diff_squares(a, b):



It takes two integers and returns a tuple containing:
1. The sum of their squares.
2. The absolute difference of their squares.
Example:
sum_squares_abs_diff_squares(3, 4)# Expected output:(25, 7)
'''

def sum_squares_abs_diff_squares(a,b):
    sum= (a*a)+(b*b)
    dif=abs((a*a)-(b*b))

    t=(sum,dif)
    return t

print(sum_squares_abs_diff_squares(3,4))
#___________________________________________________________________________________________________________


'''
Is odd-length palindrome?
Write a function:
def is_odd_length_palindrome(s):

It takes a string s and returns:
- True if the string is a palindrome AND has an odd length.
- False otherwise.
'''

def is_odd_length_palindrome(s):
    if s[::-1]==s:
        if len(s)%2!=0:
            return True
        else:
            return False
    else:
        return False

print(is_odd_length_palindrome("mom"))


def is_odd_length_palindrome(s):
    return s[::-1] == s and len(s) % 2 != 0     #even smaller approach


'''
Write a function:
def remove_elements_at_two_indices(l, i1, i2):



It takes:
- l: A list.
- i1: First index.
- i2: Second index.
The function should remove the elements at both indices from the original list.

Important conditions:
- Both indices are non-negative.
- The indices are unique (they are different).
- You must modify the original list (in-place).
- The function should not return anything.
Example
l = [1, 2, 3, 4, 5, 6, 7]i1 = 5i2 = 1remove_elements_at_two_indices(l, i1, i2)print(l)



Expected output:
[1, 3, 4, 5, 7]
'''
def remove_elements_at_two_indices(l,l1,l2):
    if l1>l2:
        l.pop(l1)
        l.pop(l2)
    else:
        l.pop(l2)
        l.pop(l1)

    return l
print(remove_elements_at_two_indices([1,2,3,4,5,6], 2, 5))