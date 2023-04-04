"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """return some of the elements in xs"""
    sum_total: float = 0.0
    for num in range(len(xs)):
        sum_total += xs[num]
    return sum_total
