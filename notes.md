def find_factors:
    instantiate empty list -> O(n)
    for each int in range 1 to n: -> O(n)
    check n's remainder is 0 -> O(1)
    if it is append it to the empty list -> O(1)
    return the list -> O(1)
TOTAL: O(n) + O(n) + O(1) + O(1) + O(1)
TOTAL: O(n)

def aliquot_sum:
    sum the elements in a list -> O(n)
    return the sum -> O(1)
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