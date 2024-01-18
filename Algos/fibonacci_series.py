def get_fibonacci_series(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def fibonacci_series_chunk(n):
    a = 0
    b = 1
    i = 0
    fibs =[]
    while i < n:
        fibs.append(a) 
        a, b = b, a + b
        i += 1
    return fibs

print(get_fibonacci_series(10))
print(fibonacci_series_chunk(10))