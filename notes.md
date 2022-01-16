def find_factors:
    instantiate empty int -> O(1)
    for each int in range 1 to n: -> O(n)
    check n's remainder is 0 -> O(1)
    if it is add it to the list -> O(1)
    return the sum of the elements in the list -> O(n)
TOTAL: O(1) + O(n) + O(1) + O(1) + O(n)
TOTAL: O(n)


def nics_cat:
    if n is less or equal to 0 -> O(1)
    raise error -> O(1)
    if aliquot_sum(n) is less then n -> O(n) + O(1)
    return result -> O(1)
    if aliquot_sum(n) is equal then n -> O(n) + O(1)
    return result -> O(1)
    if aliquot_sum(n) is greater then n -> O(n) + O(1)
    return result -> O(1)
TOTAL O(n)