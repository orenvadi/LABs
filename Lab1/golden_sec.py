def golden_section_short(f, left, right, tolerance=1e-6):
    """
    Find the minimum of a unimodal function using the golden section method.

    Parameters:
    f (function): A unimodal function to minimize.
    a (float): The left endpoint of the interval to search over.
    b (float): The right endpoint of the interval to search over.
    tolerance (float): The tolerance for the minimum value of the function.

    Returns:
    The value of x that minimizes the function f.
    """
    phi = (5**0.5 - 1) / 2  # golden ratio
    c, d = right - phi * (right - left), left + phi * (
        right - left
    )  # initialize interval

    while right - left > tolerance:
        if f(c) < f(d):
            right, d = d, c
            c = right - phi * (right - left)
        else:
            left, c = c, d
            d = left + phi * (right - left)

    return (left + right) / 2


def golden_section_long(f, a, b, tol=1e-6):
    """
    Find the minimum of a unimodal function using the golden section method.

    Parameters:
    f (function): A unimodal function to minimize.
    a (float): The left endpoint of the interval to search over.
    b (float): The right endpoint of the interval to search over.
    tol (float): The tolerance for the minimum value of the function.

    Returns:
    The value of x that minimizes the function f.
    """
    # Define the golden ratio
    golden_ratio = (5**0.5 - 1) / 2

    # Initialize the interval endpoints
    c = b - golden_ratio * (b - a)
    d = a + golden_ratio * (b - a)

    # Evaluate the function at the interval endpoints
    fc = f(c)
    fd = f(d)

    # Loop until the interval is smaller than the tolerance
    while b - a > tol:
        # Determine which subinterval to search in
        if fc < fd:
            b = d
            d = c
            c = b - golden_ratio * (b - a)
            fd = fc
            fc = f(c)
        else:
            a = c
            c = d
            d = a + golden_ratio * (b - a)
            fc = fd
            fd = f(d)

    # Return the midpoint of the final interval
    return (a + b) / 2


def fn(x: int) -> int:
    return x**2


a, b = 1, 10
print(golden_section_short(fn, a, b))
