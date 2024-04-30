email = 'example_key'

def maxkd(meteor, k):
    """
    Given a number `meteor`, finds the largest number of length `k` or fewer,
    composed of digits from `meteor`, in order.

    >>> maxkd(1234, 1)
    4
    >>> maxkd(32749, 2)
    79
    >>> maxkd(1917, 2)
    97
    >>> maxkd(32749, 18)
    32749
    """
    if k == 0:
        return 0
    if meteor < 10 ** k:
        return meteor
    a = meteor // 10
    b = meteor % 10
    return max(maxkd(a, k), maxkd(a, k - 1) * 10 + b)

# ORIGINAL SKELETON FOLLOWS

# def maxkd(meteor, k):
#     """
#     Given a number `meteor`, finds the largest number of length `k` or fewer,
#     composed of digits from `meteor`, in order.

#     >>> maxkd(1234, 1)
#     4
#     >>> maxkd(32749, 2)
#     79
#     >>> maxkd(1917, 2)
#     97
#     >>> maxkd(32749, 18)
#     32749
#     """
#     if ______:
#         return ______
#     a = ______
#     b = ______
#     return ______
