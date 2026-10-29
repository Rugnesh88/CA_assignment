def binary(n):
    return format(n, '08b')

def rol(n, count):
    for i in range(count):
        n = ((n << 1) | (n >> 7)) & 255
        print("Step", i + 1, ":", binary(n))
    print("Final result:", binary(n))

def rcl(n, carry, count):
    for i in range(count):
        new_carry = (n >> 7) & 1
        n = ((n << 1) | carry) & 255
        carry = new_carry
        print("Step", i + 1, ":", binary(n), "Carry:", carry)
    print("Final result:", binary(n))
    print("Final carry:", carry)

print("a) Rotate Left without Carry")
rol(int("10110110", 2), 2)

print("\nb) Rotate Left with Carry (initial carry = 0)")
rcl(int("10110110", 2), 0, 2)
