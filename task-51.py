list1 = [24, 36, 48, 60]
list2 = [12, 18, 24, 36, 72]

merged_list = list1 + list2
result = merged_list[0]

from math import gcd

for elem in merged_list:
    result = gcd(result, elem)

print(result)