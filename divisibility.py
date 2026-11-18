'''
Describe Number Based on Divisibility
Write a function describe_number that takes an integer as input and returns:

"Fizz" if the number is divisible by 3.
"Buzz" if divisible by 5.
"FizzBuzz" if divisible by both 3 and 5.
"Normal" if it is divisible by neither.
NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

'''

def divisibility(n):
    if(n%3==0):
        if(n%5==0):
            return "FizzBuzz"
        else:
            return "Fizz"
    else:
        if(n%5==0):
            return "Buzz"
        else:
            return "Normal"


        #OR THIS ONE
def describe_number(m):
    if m % 3 == 0 and m % 5 == 0:
        return "FizzBuzz"
    elif m % 3 == 0:
        return "Fizz"
    elif m % 5 == 0:
        return "Buzz"
    else:
        return "Normal"

m = int(input("Enter a number: "))
result = describe_number(m)

print(result)
    

