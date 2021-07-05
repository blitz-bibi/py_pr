"""
Exercise 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

Given:

number_of_terms = 5

So series will become 2 + 22 + 222 + 2222 + 22222

Expected output:

24690
"""

import math

def sum_of_series(x):
    return 0.0246 * (math.pow(10, x) - 1 - (9*x))

nlimit = 3
print(sum_of_series(nlimit))

