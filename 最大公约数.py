def fun1(a, b):
    while a % b:
        a, b = b, a % b
    return b

print(fun1(15, 6))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(15, 6))