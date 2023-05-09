def pauell(x1: int, dx: int, f) -> int:
    x2 = x1 + dx
    fx1 = f(x1)
    fx2 = f(x2)

    x3 = 0

    if fx1 > fx2:
        x3 = x1 + 2 * dx
    elif fx1 < fx2:
        x3 = x1 - dx

    fx3 = f(x3)

    Fmin = min(fx1, fx2, fx3)
    Xmin: int = -666

    counter = -2
    while counter <= 20:
        print(f(counter))
        if round(f(counter)) == round(Fmin):
            Xmin = counter
        counter += 0.1
    print(Fmin)
    return Xmin


def fn(x):
    return x**5 - x + 0.2


print(pauell(-2, 0.01, fn))
print(fn(-0.33))
