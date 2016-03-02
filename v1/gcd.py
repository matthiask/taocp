import random


def euclid_greatest_common_divisor(m, n):
    while True:
        r = m % n  # remainder
        if r == 0:
            return n
        m, n = n, r


def euclid_gcd_without_exchange(m, n):
    while True:
        m = m % n
        if m == 0: return n
        n = n % m
        if n == 0: return m


def fmt(a, b):
    print('{:>10d} {:>10d} {:>10d}'.format(
        a,
        b,
        # euclid_greatest_common_divisor(a, b),
        euclid_gcd_without_exchange(a, b),
    ))


if __name__ == '__main__':
    for i in range(100):
        fmt(
            random.randint(1, 1000),
            random.randint(1, 1000),
        )

    fmt(6099, 2166)
