def multiply_numbers(a, b):
    x = a
    y = b
    product = 0
    for i in range(y):
        product += x
    return product

result = multiply_numbers(3, 4)
print(f"Result: {result}")
