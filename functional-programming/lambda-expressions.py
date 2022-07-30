# Lambda
# -> Lambda is actually a computer science term that really is compatible with this idea of functional programming.

# Lambda Expressions
# -> Lambda expressions is python are one time anonymouse function that you don't need more than once.

# Syntext
# -> lambda param: action(param)

from functools import reduce


my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list, 0))
