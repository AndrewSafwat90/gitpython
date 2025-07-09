import timeit
import random

# print(dir(timeit))


# print(timeit.timeit("'Andrew' * 1000"))


# print(random.randint(1, 1000))
# print(timeit.timeit(stmt="random.randint(1, 1000)", setup="import random"))
print(timeit.repeat(stmt="random.randint(1, 1000)",
      setup="import random", repeat=3, number=4))
