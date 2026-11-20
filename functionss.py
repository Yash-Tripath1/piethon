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