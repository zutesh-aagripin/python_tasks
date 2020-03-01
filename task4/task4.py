import sys
import re

args = sys.argv
if len (args) < 3:
    print ("Usage: Python task4.py [string1] [string2]")
    exit(0)
elif len (args) > 3:
    print("Usage: Python task4.py [string1] [string2]")
    exit(0)
s1 = args[1]
s2 = args[2]

def detailedcheck(s1, s2):
	i = 0
	j = 0;
	star = -1;
	while (s2[j] == "*" and len(s2) > j + 1 and s2[j + 1] == "*"):
		j += 1
	if (s2[0] == "*" and len(s2) > j + 1 and len(s1) > 0 and s2[j + 1] == s1[0]):
		j += 1
	while (i < len(s1) and j < len(s2)):
		if s1[i] == s2[j]:
			i += 1
			j += 1
			star = -1;
		elif s2[j] == '*' and star == 1:
			j += 1
		elif s2[j] == '*':
			i += 1
			j += 1
			star = 1;
		elif s2[j] in s1[i:] and star == 1:
			i += 1
		else:
			return "KO"
	if (i < len(s1) and star == -1):
		return "KO"
	if (j < len(s2) and s2[j] != "*"):
		return "KO"
	return "OK"

#if s1 == s2:
#	print("OK")
#elif s1 != s2 and "*" not in s2:
#	print("KO")
#elif "*" in s2 and s1 != s2:
print(detailedcheck(s1, s2))