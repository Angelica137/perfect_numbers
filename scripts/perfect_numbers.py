def aliquot_number(n):
    factors = [i for i in range(1, n) if n % i == 0]
    return sum(factors)


def nics_cat(n):
    if n <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")
    aliquot = aliquot_number(n)
    if aliquot < n:
        return "Deficient"
    if aliquot == n:
        return "Perfect"
    if aliquot > n:
        return "Abundant"
