def _factorial(num):
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num -= 1
    return factorial

result = _factorial(5)
print(result)
