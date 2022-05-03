"""
Using Recursion:
In mathematics, the factorial of a non-negative integer n, denoted by n!,
is the product of all positive integers less than or equal to n.
The factorial of n also equals the product of n with the next smaller factorial:
    n! = n * (n-1) * (n-2) * (n-3) * ... * 2 * 1
"""


def Factorial(num):
    # If the number is less than or equal to 1, the factorial is always going to be 1. i.e., fact(0) = 1 and fact(1) = 1
    if num <= 1:
        return num
    # Recursion starts here n! = n * (n-1)!
    return num * Factorial(num-1)


n = int(input("Enter the number to know the factorial: "))
print(Factorial(n))

### Uncomment the below three lines To get the factorial series up to and including 'n'
# n = int(input("Enter the number up to which the factorial series is to be displayed: "))
# for i in range(n + 1):
#     print(Factorial(i), end=', ')
