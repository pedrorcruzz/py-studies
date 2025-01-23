import timeit


def sum1(n):
    soma = 0  # step 1
    for i in range(n + 1):  # step 2: Loop  (n + 1) any number of times
        soma += 1  # step 3: execute (n+ 1) any number of times
    return soma  # step 4


print(timeit.timeit("sum1(10)", globals=globals(), number=1000))


def sum2(n):
    return (n * (n+1)) / 2  # step 1: 3 operations in one line


print(timeit.timeit("sum2(10)", globals=globals(), number=1000))
