import sympy as sp

print("=== 余弦定理求对边 a（精确根式版）===")
print("支持输入：pi/3、sqrt(2)、1/2、5 等")

# 输入角度
A = sp.sympify(input("请输入角 A（弧度，如 pi/3）："))

# 输入边长（可以是无理数！）
b = sp.sympify(input("请输入边长 b（如 sqrt(3)）："))
c = sp.sympify(input("请输入边长 c（如 2/3）："))

# 余弦定理
a = sp.sqrt(b**2 + c**2 - 2 * b * c * sp.cos(A))
a_exact = sp.simplify(a)

print("\n精确结果：a =", a_exact)
print("小数近似：a =", round(float(a), 6))
input("\n按回车键退出……")
