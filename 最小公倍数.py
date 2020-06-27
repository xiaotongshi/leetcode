
def lcm(a, b):
    c = max(a, b)
    while True:
        if c%a == 0 and c%b == 0:
            print(c)
            break
        c += 1

lcm(4,6)

# 两数乘积除以最大公约数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def fun(a, b):
    c = gcd(a, b)
    print(a*b/c)

fun(4, 6)