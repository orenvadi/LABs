def fibonacci_search(f, a, b, N):
    k = 0
    eps = 1e-6

    x0, x3 = a, b
    x1 = x0 + (x3 - x0) / (1 + (5**0.5) / 2)
    x2 = x3 - (x1 - x0)

    f1, f2 = f(x1), f(x2)
    k += 2

    while k < N:
        if f1 > f2:
            if x2 > x1:
                x3, x2 = x2, x1
            else:
                x0, x1 = x1, x2
            x1 = x0 + (x3 - x0) / (1 + (5**0.5) / 2)
            f1 = f2
            f2 = f(x1)
            k += 1
        else:
            if x1 > x2:
                x0, x1 = x2, x1
            else:
                x3, x2 = x2, x1
            x1 = x0 + (x3 - x0) / (1 + (5**0.5) / 2)
            f2 = f1
            f1 = f(x1)
            k += 1

        if abs(x3 - x0) < eps:
            break

    return (x0 + x3) / 2


fn = lambda x: x**2

a, b = -2, 10
print(fibonacci_search(fn, a, b, 130))
