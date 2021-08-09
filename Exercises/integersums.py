"""
Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.
"""


def add_it_up(number: int):
    sum = 0
    for num in range(number + 1):
        sum += num
    return sum


def add_it_up_2(number: int):
    return sum(range(number + 1))


print(add_it_up(5))
print(add_it_up_2(5))