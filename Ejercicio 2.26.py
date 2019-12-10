def oper(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=" ")
        a, b = b, 3*b + 2*a
oper(1000)