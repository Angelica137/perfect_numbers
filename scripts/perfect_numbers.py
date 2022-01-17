def nics_cat(n):
    factors = sum(i for i in range(1, n) if n % i == 0)
    if n <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")
    if factors < n:
        return "Deficient"
    if factors == n:
        return "Perfect"
    if factors > n:
        return "Abundant"
