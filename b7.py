a = int(input("Nhập số 1: "))
b = int(input("Nhập số 2: "))
c = int(input("Nhập số 3: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
input("Nhấn Enter để thoát...")
