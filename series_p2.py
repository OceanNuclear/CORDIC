from numpy import array as ary
from math import fsum
max_iter = 80
verbose = True
monotonically_decreasing_series = ary([0.5**n for n in range(1, max_iter)])

if __name__=='__main__':
    comp, series = [], []
    target_num = float(input("Enter the target number to approximate:"))
    for basis in monotonically_decreasing_series:
        if fsum(comp)>target_num:
            this_direction = -1
        elif fsum(comp)<target_num:
            this_direction = 1
        else: # equal
            this_direction = 0
        comp.append(basis*this_direction)
        series.append(this_direction)
    print("Approximated sum = ", fsum(comp))
    if verbose:
        print("using the following series:")
        print(series)