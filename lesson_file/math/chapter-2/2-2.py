# 集合の操作

a = set([2, 4, 5, 6])
b = set([3, 4, 6])

print(a)
print(b)

# 積集合
# 重複しているものを返す
print(a & b)

# 差集合
# 重なっていない部分を返す
print(a - b)

# 和集合
# どちらかに合致するものを返す
print(a | b)