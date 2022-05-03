"""
Without Recursion:
In mathematics, the Fibonacci series and Golden ratio are closely connected.
In a Fibonacci series, every term is the sum of the preceding two terms, starting from 0 and 1 as first and second terms.
The Fibonacci series is given as, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987.
"""

n = int(input("Enter the number of terms to create a sequence: "))
n1, n2 = 0, 1       # Set the first and second terms
count = 0

# Fibonacci series always consists of whole numbers.
if n <= 0:
    print("Please enter a positive integer")

# Start a loop from 0 to number of terms
while count < n:
    # Print the first term
    print(n1, end=', ')
    # The next term will be the sum of the previous two terms (n1 and n2 in the first iteration)
    nth = n1 + n2
    # Swap n1 with n2
    n1 = n2
    # Swap n2 with the sum we received above
    n2 = nth
    # Increment the count to start the next iteration.
    count += 1
