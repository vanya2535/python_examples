from functools import reduce
a = [1, 2, 3, 4]
print(list(map(lambda x: x - 1, a)))
print(list(filter(lambda x: x > 1, a)))

def func(prev, now):
    print(prev, now)
    return prev - now

print(reduce(func, a))
b = 'asdasds'
print(list(zip(a, b)))