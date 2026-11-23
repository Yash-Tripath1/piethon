'''
Question: De-duplicate the treasure
A goblin has collected coins, but some coins have the same number. Help him keep only the first occurrence of each number.

Write:
def clean_hoard(coins):

Example:
coins = [5, 2, 5, 3, 2, 8, 3, 1]

Expected output:
[5, 2, 3, 8, 1]
'''

#ok the hard way of doing this which i thought of, solution is written by AI after i explained it my approach
#the approach was much different than how i imagined so im not gonna consider this, so just asked AI's solution

def clean_hoard(l):
    result = []

    for i in range(len(l)):
        duplicate = False

        for j in range(i-1, -1, -1):
            if l[i] == l[j]:
                duplicate = True
                break

        if not duplicate:
            result.append(l[i])

    return result


#_______________________________________________________________
#here's some actual good solution which i found more efficient and without AI's help
def clean_hoard(l):
    s=set(l)
    m=list(s)
    return m

print(clean_hoard([5, 2, 5, 3, 2, 8]))
#but this gives  [8, 2, 3, 5] and not [5, 2, 3, 8]

#_________________________________________________________________

def clean_hoard(l):
    m=[]
    for i in l:
        if i in m:
            continue
        m.append(i)
    return m
print(clean_hoard([5, 2, 5, 3, 2, 8]))

#YAYYYYYYYYYYYY
#i might be showing signs of mental illness honestly, fs




    