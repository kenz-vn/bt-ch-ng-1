i = 1
while i <= 3:
    print("Sinh viên", i)

    name = input("Tên: ")
    toan = float(input("Toán: "))
    ly = float(input("Lý: "))
    hoa = float(input("Hóa: "))

    avg = (toan + ly + hoa) / 3

    print("Tên:", name)
    print("Điểm trung bình:", avg)
    print("----------------")

    i += 1
input("Nhấn Enter để thoát...")

