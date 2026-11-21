'''
Remove duplicate elements while preserving order
Write a function:
def remove_duplicates(nums):

It should return a new list containing each element only once, keeping the order of its first appearance.
'''

def remove_duplicates(nums):
    newl=[]
    setl=set(nums)
    newl=newl+ list(setl)
    return newl

print(remove_duplicates([3, 1, 2, 3, 1]))

#BUT THIS DOES NOT PRESERVE ORDER, so go through this instead
#_______________________________________________________________________________________________________________

def remove_duplicate(nums):
    newl=[]
    for i in nums:
        if i not in newl:
            newl.append(i)

    return newl

print(remove_duplicate([3, 1, 2, 3, 1]))