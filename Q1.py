def binary(n):
    return format(n & 255, '08b')

def value(n):
    return n if n < 128 else n - 256

def calculate(a, b):
    result = a - b
    r = result & 255

    print("\nExpression:", a, "-", b)
    print("First operand :", binary(a))
    print("Second operand:", binary(b))
    print("Result binary :", binary(r))
    print("Result decimal:", value(r))
    print("Overflow:", "Yes" if result < -128 or result > 127 else "No")

calculate(45, 19)
calculate(-35, -12)
