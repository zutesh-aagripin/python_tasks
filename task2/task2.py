import sys
import re

args = sys.argv
if len (args) < 2:
    print ("Usage: Python task2.py [filename]")
    exit(0)
elif len (args) > 2:
    print("Usage: Python task2.py [filename]")
    exit(0)
fd = open(args[1], 'r')
contains = fd.read()
fd.close

points = re.findall(r"(\D):", contains)
coordinates = re.findall(r"\d{0,},\d{0,},\d{0,}", contains)
numbers = []
for string in coordinates:
    numbers.append([int(num) for num in string.split(',')])
t1 = {points[0]:numbers[0], points[1]:numbers[1], points[2]:numbers[2]}
t2 = {points[3]:numbers[3], points[4]:numbers[4], points[5]:numbers[5]}
import math
def findside(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2 + (c2[2] - c1[2]) ** 2)
AB1 = (findside(t1.get("A"), t1.get("B")))
BC1 = (findside(t1.get("B"), t1.get("C")))
AC1 = (findside(t1.get("A"), t1.get("C")))
AB2 = (findside(t2.get("A"), t2.get("B")))
BC2 = (findside(t2.get("B"), t2.get("C")))
AC2 = (findside(t2.get("A"), t2.get("C")))

result = AB1 / AB2 == BC1 / BC2 == AC1 / AC2 or AB1 / AB2 == BC1 / AC2 == AC1 / BC2 or AB1 / BC2 == BC1 / AC2 == AC1 / AB2 or AB1 / BC2 == BC1 / AB2 == AC1 / AC2 or AB1 / AC2 == BC1 / AB2 == AC1 / BC2 or AB1 / AC2 == BC1 / BC2 == AC1 / AB2
print(result)