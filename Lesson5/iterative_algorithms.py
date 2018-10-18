def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
