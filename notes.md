def find_factors:
    instantiate empty list -> O(n)
    for each int in range 1 to n: -> O(n)
    check n's remainder is 0 -> O(1)
    if it is append it to the empty list -> O(1)
    return the list -> O(1)
TOTAL: O(n) + O(n) + O(1) + O(1) + O(1)
TOTAL: O(n)

