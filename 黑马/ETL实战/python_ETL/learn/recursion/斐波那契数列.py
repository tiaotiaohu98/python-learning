'''
    1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711

    # 求解斐波那契数列的函数
    fib(1) = 1
    fib(2) = 1
    fib(3) = fib(1) + fib(2)
    fib(4) = fib(2) + fib(3)
    fib(5) = fib(3) + fib(4)
    ...
    fib(n) = fib(n-2) + fib(n-1)
'''

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-2) + fib(n-1)

print(fib(15))

