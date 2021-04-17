# 連立方程式

from numpy.linalg import solve

# y - 3x = 4
# 7x - 6y = - 35
# xとyの位置が逆になっているので揃える-> -3x + y = 4
left = [[-3, 1], [7, -6]]
right = [4, -35]
print(solve(left, right))


# 8x - 2y = 0
# 2x - 8y = - 60
left2 = [[8, -2], [2, -8]]
right2 = [0, -60]
print(solve(left2, right2))


# 3/4x + 5/2y = -6 ...い
# y = 2x - 7 ...ろ
# そろえる-> -2x + y =  - 7 ...ろ
left3 = [[3/4, 5/2], [-2, 1]]
right3 = [-6, -7] 
print(solve(left3, right3))


# 2(x + 3y) = -6 ...①
# 2y - 7 = -(3x - y) ...②
# ->
# 2x + 6y = -6 ...①
# 3x - y = 7 ...②

left4 = [[2, 6], [3, 1]]
right4 = [-6, 7]
print(solve(left4, right4))

# 5x-4y+6z=8 ...①
# 7x-6y+10z=14 ...②
# 4x+9y+7z=74 ...③
left5 = [[5, -4, 6], [7, -6, 10], [4, 9, 7]]
right5 = [8, 14, 74]
print(solve(left5, right5))
