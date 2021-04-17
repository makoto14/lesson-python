# 連立方程式
import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')

equation1 = 2*x + 3*y - 16
equation2 = x + 7*y - 19

print(sympy.solve([equation1, equation2]))


# 3/4x + 5/2y = -6 ...①
# y = 2x - 7 ...②

equation3 = 3/4*x + 5/2*y + 6
equation4 = - 2*x + y + 7
print(sympy.solve([equation3, equation4]))


# 5x-4y+6z=8 ...①
# 7x-6y+10z=14 ...②
# 4x+9y+7z=74 ...③
equation5 = 5*x - 4*y + 6*z - 8
equation6 = 7*x - 6*y + 10*z - 14
equation7 = 4*x + 9*y + 7*z - 74
print(sympy.solve([equation5, equation6, equation7]))
