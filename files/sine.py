import sympy as sp

# 定义符号
pi = sp.pi
sin = sp.sin

print("=== 正弦定理计算器（SymPy 精确无理数版）===\n输入弧度请输入 1\n输入 π 的倍数请输入 2")

choice = int(input("请选择："))

if choice == 1:
    A = sp.sympify(input("请输入角 A（弧度，可输 pi/2, sqrt(2) 等）："))
    B = sp.sympify(input("请输入角 B（弧度，可输 pi/2, sqrt(3) 等）："))

elif choice == 2:
    kA = sp.sympify(input("请输入 A = k*pi 中的 k："))
    kB = sp.sympify(input("请输入 B = k*pi 中的 k："))
    A = kA * pi
    B = kB * pi

else:
    print("输入错误")
    exit()

sin_A = sin(A)
sin_B = sin(B)

print("\n已知边选择：\n输入 a 边请按 3\n输入 b 边请按 4")

choice2 = int(input("请选择："))

if choice2 == 3:
    a = sp.sympify(input("请输入边长 a："))
    b = a * sin_B / sin_A
    print("\nb =", b)
    print("b 小数近似：", float(b.evalf()))

elif choice2 == 4:
    b = sp.sympify(input("请输入边长 b："))
    a = b * sin_A / sin_B
    print("\na =", a)
    print("a 小数近似：", float(a.evalf()))

else:
    print("输入错误")
    exit()
