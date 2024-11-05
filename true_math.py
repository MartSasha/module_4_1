from math import inf
def divide(first, second):
    if second != 0:
        true_divide = first/second
        return true_divide
    else:
        return inf
divide(5, 0)