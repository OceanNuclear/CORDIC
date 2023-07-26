from numpy import pi, cos, arctan, array as ary
import numpy as np
from math import fsum
max_iter = 80
verbose = True
powers = ary([0.5**n for n in range(0, max_iter)])
monotonically_decreasing_series = arctan(powers)
from functools import reduce
from operator import mul
cosine_values = reduce(mul, cos(monotonically_decreasing_series), 1.0)
mode = "degree" # {degree|radian}
if mode=="degree":
    monotonically_decreasing_series = np.rad2deg(monotonically_decreasing_series)

def approximator(target_num):
    """Procedure to find the best fit algorithm """
    comp, series = [], []
    for basis in monotonically_decreasing_series:
        if fsum(comp)>target_num:
            this_direction = -1
        elif fsum(comp)<target_num:
            this_direction = 1
        else: # equal
            this_direction = 0
        comp.append(basis*this_direction)
        series.append(this_direction)
    return comp, series

def approximation_summary(target_num)
    comp, series = approximator(target_num)
    print("Approximated angle sum = ", fsum(comp))
    print("Using the following series:")
    print(series)
    if verbose:
        print("The value of scale factor constant K =", cosine_values)

if __name__=='__main__':
    while True:
        
    target_num = float(input("Enter the target number to approximate:"))