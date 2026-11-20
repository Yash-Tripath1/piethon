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

