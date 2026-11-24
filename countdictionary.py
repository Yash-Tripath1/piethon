'''
You are given a list of grocery items purchased by a customer.
items = [    "apple", "banana", "apple",    "orange", "banana", "apple",    "mango", "orange"]



Write a function:
def count_items(items):



Your task is to create and return a dictionary containing the frequency of every item.

Expected output:
{    "apple": 3,    "banana": 2,    "orange": 2,    "mango": 1}
'''

def count_items(items):
    d={}
    for i in items:
        d[i]=d.get(i, 0)+1
    return d

print(count_items([    "apple", "banana", "apple",    "orange", "banana", "apple",    "mango", "orange"]))