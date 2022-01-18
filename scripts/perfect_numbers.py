import operator


def nics_cat(n: int) -> str:
    if n <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")
    factors = sum(i for i in range(1, n) if n % i == 0)
    operators = [("perfect", operator.eq), ("deficient",
                                            operator.lt), ("abundant", operator.gt)]
    for label, op in operators:
        if op(factors, n):
            return label
    if factors < n:
        return "Deficient"
    if factors == n:
        return "Perfect"
    return "Abundant"


operators = [operator.eq, operator.lt, operator.gt]
labels = ["=", "<", ">"]


def get_comparison_operator(a, b):
    """
    A function that returns an operator string based on the relation between
    the supplied two numbers.
    """
    for op, label in zip(operators, labels):
        if op(b, a):
            return label
    return '?'


print("hello")
print(get_comparison_operator(2, 6))  # returns '<'

'''
ops = [("perfect", operator.eq), ("deficient", operator.lt), ("abundant", operator.gt)]
for label, op in ops: ...
# or
ops = {"perfect": operator.eq, "deficient": operator.lt, "abundant": operator.gt}
for label, op in ops.items(): ...
'''
