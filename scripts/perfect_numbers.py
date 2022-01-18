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
