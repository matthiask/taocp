def fib_bottom_up(n):
    prev1 = 1
    prev2 = 1
    result = 1
    for i in range(1, n):
        result = prev1 + prev2
        prev1, prev2 = result, prev1
    return result


def fib_recurse(n):
    if n in (0, 1): return 1
    return fib_recurse(n - 1) + fib_recurse(n - 2)


if __name__ == '__main__':
    for n in range(30):
        print('{:>10d} {:>10d}'.format(
            n,
            fib_bottom_up(n),
            # fib_recurse(n),
        ))
