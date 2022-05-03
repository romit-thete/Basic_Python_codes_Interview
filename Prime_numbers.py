"""
A prime number is a whole number greater than 1 whose only factors are 1 and itself.
A factor is a whole number that can be divided evenly into another number.
The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
Numbers that have more than two factors are called composite numbers.
"""

rng = int(input("Enter range: "))
list1 = []
print("Prime numbers:", end=' ')

# 1 is neither prime nor composite, hence we start with 2
for num in range(2, rng+1):
    for i in range(2, num):
        if num % i == 0:
            break           # breaks iteration and moves back to the for loop and increment num
    # This else will run when from 2 until num, all the values of i are exhausted, and we still get num % i != 0...
    else:
        print(num, end=', ')
