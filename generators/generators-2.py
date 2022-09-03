# Generators are iterable but iterable is not generator
# Generators store latest value in memory

# yield pause generator and waiting for next to resume it.


def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(1000)
next(g)
next(g)
print(next(g))
