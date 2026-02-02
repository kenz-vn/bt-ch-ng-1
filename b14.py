import math

n = float(input("Nhập một số: "))

if n < 0:
    print("Không thể tính căn bậc hai của số âm")
else:
    print("Căn bậc hai là:", math.sqrt(n))
input("Nhấn Enter để thoát...")
