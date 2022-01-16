def aliquot_sum(n):
    sum_factors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_factors += i
    return sum_factors


def nics_cat(n):
    if n <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")
    if aliquot_sum(n) < n:
        return "Deficient"
    if aliquot_sum(n) == n:
        return "Perfect"
    if aliquot_sum(n) > n:
        return "Abundant"
