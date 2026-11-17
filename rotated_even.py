'''
        list: A list with even indices rotated.
        [0,1,2,3,4,5,6] and k=1
        even indice= [0,2,4,6]
        we need to convert this to [6,0,2,4]
        then put this in the original list
        [6,1,0,3,2,5,4]
    '''

def rotate_even(l, k):
    even_indices= l[::2]
    #normalise k by taking its remainder
    k=k%len(even_indices)
    rotated = even_indices[-k:] + even_indices[:-k]
    l[::2]=rotated

    return l

l=list(map(int, input("Enter list separated by space").split()))
#split separates the string wherever there is space
#map(int, ...) converts each string into an integer
k=int(input("Enter rotation value (k): "))

result=rotate_even(l,k)
print(result)

'''
Extract elements at even indices.



Calculate the effective rotation using modulo.



Rotate those extracted elements.



Put them back into the original even-indexed positions.



Return the original list with its updated values.
'''

