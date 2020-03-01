import sys
import re

args = sys.argv
if len (args) < 2:
    print ("Usage: Python task1.py [filename]")
    exit(0)
elif len (args) > 2:
    print("Usage: Python task1.py [filename]")
    exit(0)
fd = open(args[1], 'r')
contains = fd.read()
fd.close
regulars = re.findall(r"\d{0,}\n", contains)
if len(regulars) == 0:
    print("Error: no numbers")
    exit(0)
numbers = [int(num) for num in regulars]

#нормальное человеческое решение
#import numpy as np
#fifty = np.mean(numbers)
#ninety = np.percentile(numbers, 90)
#print (sum([nbr for nbr in numbers if ninety > nbr > fifty]))

# решение с сортировкой и поиском перцентиля вручную
def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array

import math
def percentile(array, percent):
    return quicksort(array)[int(math.ceil((len(array) * percent) / 100)) - 1]

def average(array):
    return (sum(array) / len(array))

mean = average(numbers)
ninety = percentile(numbers, 90)
print (sum([nbr for nbr in numbers if ninety > nbr > mean]))