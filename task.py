# 1: Create a function that, given a list of integers, returns the highest product between three of those numbers.
# For example, given the list [1, 10, 2, 6, 5, 3] the highest product would be 10 * 6 * 5 = 300

def highest_product(ints: list):
    if len(ints) >= 3:
        ints.sort()
        return max(ints[0]*ints[1]*ints[-1], ints[-1]*ints[-2]*ints[-3])
    else:
        return None
