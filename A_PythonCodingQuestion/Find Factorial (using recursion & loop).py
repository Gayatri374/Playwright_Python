# Iterative
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Recursive
def factorial_rec(n):
    return 1 if n <= 1 else n * factorial_rec(n-1)

print(factorial(5))      # 120
print(factorial_rec(5))  # 120