# 連立方程式
# 2x + 3y = 16
# x + 7y = 19

from numpy.linalg import solve

left = [[2, 3], [1, 7]]
right = [16, 19]

print(solve(left, right))


# 2x + 3y = 16
# 2x + 14y = 38
# minus
# -11y = 22
# y =2


# x + 14 = 19
# x = 5
