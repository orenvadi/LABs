def aprox(a: int, b: int, f):
    x1 = a
    x3 = b
    x2 = (x3 - x1) / 2
    fx1 = f(x1)
    fx2 = f(x2)
    fx3 = f(x3)
    a1 = (fx2 - fx1) / (x2 - x1)
    a2 = (1 / (x3 - x2)) * (((fx3 - fx1) / (x3 - x1)) - ((fx2 - fx1) / (x2 - x1)))
    return (x2 + x1) / 2 - (a1 / 2 * a2)


def fn(x):
    return x**5 - x + 0.2


print(aprox(-2, 20, fn))
print(fn(aprox(-2, 20, fn)))
