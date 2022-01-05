def perfect_numbers(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors
