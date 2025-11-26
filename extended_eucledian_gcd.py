def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


if __name__ == "__main__":
    a = int(input("enter a "))
    b = int(input("enter b "))

    g, x, y = extended_gcd(a, b)

    print(g)
    print(x)
    print(y)
