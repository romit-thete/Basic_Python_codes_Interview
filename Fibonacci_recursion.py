"""
Using Recursion:
In mathematics, the Fibonacci series and Golden ratio are closely connected.
In a Fibonacci series, every term is the sum of the preceding two terms, starting from 0 and 1 as first and second terms.
The Fibonacci series is given as, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987.
"""


def Fib_recursion(num):
    # If nth  term is less than or equal to 1, the Fibonacci representation will be the number itself (only for 0 and 1)
    if num <= 1:
        return num
    # Recursion starts here F(n) = F(n-1) + F(n-2)
    return Fib_recursion(num - 1) + Fib_recursion(num - 2)


n = int(input("Enter the nth term up to which a sequence is to be created: "))

# Fibonacci is only for whole numbers!
if n <= 0:
    print("Please enter a positive integer")
else:
    ### Uncomment the below line to get the Fibonacci representation of the nth term
    # print(Fib_recursion(n - 1))
    for i in range(n):
        print(Fib_recursion(i), end=', ')
