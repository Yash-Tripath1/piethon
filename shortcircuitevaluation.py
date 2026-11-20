'''
Count positive integers, ignoring None
Write a function:
def count_positive_ignore_none(nums):



It receives a list containing integers and possibly None.

Your task is to count how many elements are strictly greater than zero, while ignoring:
- Negative numbers
- Zero
- None values
Examples
count_positive_ignore_none([1, -2, 3, 0, None])     2
count_positive_ignore_none([5, 8, 10, None, -4])    3
count_positive_ignore_none([0, -1, None, -5])       0
'''

def count_positive_ignore_none(nums):
    count=0
    i=0
    for i in range(len(nums)):
        if nums[i] is not None and nums[i]>0:
            count=count+1
    return count

print(count_positive_ignore_none([1, -2, 3, 0, None]))

'''
        Python evaluates conditions from left to right.

Suppose nums[i] = None:
1. nums[i] is not None → False
2. Python sees and and knows the entire condition cannot be True.
3. It skips the second comparison.
4. No error!
This behaviour is called short-circuit evaluation.
        '''