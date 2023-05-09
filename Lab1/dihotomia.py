from math import fabs  # just float abs


def fn(x):
    return x**2


def dihotomia(f, a, b, eps):
    """
    Find the minimum of a unimodal function using the dichotomous search method.

    Parameters:
    f (function): A unimodal function to minimize.
    a (float): The left endpoint of the interval to search over.
    b (float): The right endpoint of the interval to search over.
    eps (float): The desired accuracy of the minimizer.

    Returns:
    The value of x that minimizes the function f.
    """
    while abs(b - a) > eps:
        c = (a + b) / 2
        d = c + eps / 2

        if f(c) < f(d):
            b = d
        else:
            a = c

    return (a + b) / 2


a = 1
b = 10

eps = 0.01

print(f"{dihotomia(fn, a, b, eps):.16f}")
for _ in range(10):
    # print(f"eps = {eps:.10f} dihotomia = {dihotomia(fn, a, b, eps):.16f}")
    eps *= 10
