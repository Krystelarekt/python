import sympy as sym
from sympy.matrices import Matrix

x, y = sym.symbols('x y') 
expr1 = input("enter 1st function:")
sym.sympify(expr1)
expr2 = input("enter 2nd function:")
sym.sympify(expr2)
expr3 = input("enter 3rd function:")
sym.sympify(expr3)
print("1st Expression : {} ".format(expr1))
print("2nd Expression : {} ".format(expr2))
print("3rd Expression : {} ".format(expr3))

xexpr1_diff1 = sym.Derivative(expr1, x)
xexpr2_diff1 = sym.Derivative(expr2, x)
xexpr3_diff1 = sym.Derivative(expr3, x)

xexpr1_diff2 = sym.Derivative(xexpr1_diff1, x)
xexpr2_diff2 = sym.Derivative(xexpr2_diff1, x)
xexpr3_diff2 = sym.Derivative(xexpr3_diff1, x)

yexpr1_diff1 = sym.Derivative(expr1, y)
yexpr2_diff1 = sym.Derivative(expr2, y)
yexpr3_diff1 = sym.Derivative(expr3, y)

yexpr1_diff2 = sym.Derivative(yexpr1_diff1, y)
yexpr2_diff2 = sym.Derivative(yexpr2_diff1, y)
yexpr3_diff2 = sym.Derivative(yexpr3_diff1, y)

m = sym.Matrix([
    [expr1,expr2,expr3],
    [xexpr1_diff1,xexpr2_diff1,xexpr3_diff1],
    [xexpr1_diff2,xexpr2_diff2,xexpr3_diff2]
])

if(m.det()==0):
    print("it is linear dependent")

else:
    print("it is linear independent")

print(m.det())

print("1st derivative:->")
print("eq 1:")
print("Derivative of expression with respect to x : {}".format(xexpr1_diff1.doit()))
print("Derivative of expression with respect to y : {}".format(yexpr1_diff1.doit()))
print("eq 2:")
print("Derivative of expression with respect to x : {}".format(xexpr2_diff1.doit()))
print("Derivative of expression with respect to y : {}".format(yexpr2_diff1.doit()))
print("eq 3:")
print("Derivative of expression with respect to x : {}".format(xexpr3_diff1.doit()))
print("Derivative of expression with respect to y : {}".format(yexpr3_diff1.doit()))
print("2nd derivative:->")
print("eq 1:")
print("Derivative of expression with respect to x : {}".format(xexpr1_diff2.doit()))
print("Derivative of expression with respect to y : {}".format(yexpr1_diff2.doit()))
print("eq 2:")
print("Derivative of expression with respect to x : {}".format(xexpr2_diff2.doit()))
print("Derivative of expression with respect to y : {}".format(yexpr2_diff2.doit()))
print("eq 3:")
print("Derivative of expression with respect to x : {}".format(xexpr3_diff2.doit()))
print("Derivative of expression with respect to y : {}".format(yexpr3_diff2.doit()))