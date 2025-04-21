import math

digit_1 = int(input())
new = pow(digit_1, int(input('Степень')))
rooted = pow(new, 1/3)
print(rooted)
print(round(rooted, 1))
print(math.floor(rooted))
print(math.ceil(rooted))