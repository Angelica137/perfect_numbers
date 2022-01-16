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
    sum = aliquot_sum(n)
    if sum < n:
        return "Deficient"
    if sum == n:
        return "Perfect"
    if sum > n:
        return "Abundant"
