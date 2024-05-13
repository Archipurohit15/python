def fibonacci(n):
    """Return a list of Fibonacci numbers up to the nth Fibonacci number."""
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list
