def perfect_numbers(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    aliquot_sum = sum(factors)
    return aliquot_sum


def nics_cat(n):
    if n < perfect_numbers(n):
        return "Deficient"


print(perfect_numbers(15))
print(nics_cat(15))
