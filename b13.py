a = input("Nhập số thứ nhất: ")
b = input("Nhập số thứ hai: ")

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)

    if b == 0:
        print("Không thể chia cho 0")
    else:
        print("Kết quả:", a / b)
else:
    print("Vui lòng nhập số nguyên")
input("Nhấn Enter để thoát...")
