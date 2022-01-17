def nics_cat(n):
    if n <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")
    factors = sum(i for i in range(1, n) if n % i == 0)
    if factors < n:
        return "Deficient"
    if factors == n:
        return "Perfect"
    return "Abundant"
