def find_factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors


def aliquot_sum(n):
    aliquot_sum = sum(find_factors(n))
    return aliquot_sum


def nics_cat(n):
    if aliquot_sum(n) == n:
        return "Perfect"
