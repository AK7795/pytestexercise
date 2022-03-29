def prime(a):
    for i in range(2, int(a / 2) + 1):
        if (a % i) == 0:

            return "not prime"
    else:
        return "prime"


def palin(a):
    t = a
    r = 0
    while (a > 0):
        d = a % 10
        r = r * 10 + d
        a = a // 10
    if t == r:
        return "palindrome"
    else:
        return "not palindrome"


if __name__ == "__main__":
        n1 = int(input("enter no 1 : "))
        print(prime(n1))
        print(palin(n1))