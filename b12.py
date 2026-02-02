weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height * height)

print("BMI của bạn là:", round(bmi, 2))
input("Nhấn Enter để thoát...")
