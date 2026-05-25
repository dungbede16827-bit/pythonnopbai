# # input người dùng nhập phiếu đăng ký int 
# mỗi pheieus đk chuỗi gồm 4 phần
# Họ tên | Khóa học | Mã học viên | Email
# Output
# Sau khi chuẩn hóa:
# ===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====
# Học viên: Nguyen Van A
# Khóa học: Python Basic
# Mã học viên: RK-001
# Email: student01@gmail.com
# Mã xác nhận: RK-001_PYTHON-BASIC
# Sử dụng:
# Hàm	Công dụng
# `split("	")`
# strip()	xóa khoảng trắng
# title()	chuẩn hóa tên
# upper()	viết hoa
# lower()	viết thường
# Bước 1
# Nhập số lượng phiếu.
# Kiểm tra:
# if quantity <= 0
# kết thúc chương trình.
# Bước 2
# Nhập từng phiếu đăng ký.
# Dùng:
# split("|")
# để tách chuỗi.
# Bước 3
# Kiểm tra đủ 4 phần dữ liệu.
# Nếu không đủ:
# continue
# bỏ qua phiếu.
# Bưoc 4
# Chuẩn hóa dữ liệu.
# Họ tên:
# strip().title()
# Khóa học
# strip().title()
# Mã học viên:
# strip().upper()
# Email:
# strip().lower()
# Bước 5
# Kiểm tra dữ liệu hợp lệ.
# Email phải chứa:
# @
# Mã học viên:
# len(student_id) >= 5
# Bước 6
# Tạo mã xác nhận:
# RK-001_PYTHON-BASIC


quantity = int(input("Nhập số lượng phiếu đăng ký: "))

if quantity <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
    print("Chương trình kết thúc.")

else:

    for i in range(quantity):

        print(f"\nPhiếu đăng ký {i+1}")

        register = input("Nhập dữ liệu: ")

        data = register.split("|")

        if len(data) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        full_name = data[0].strip().title()
        course_name = data[1].strip().title()
        student_id = data[2].strip().upper()
        email = data[3].strip().lower()

     
        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        
        if len(student_id) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        confirm_code = student_id + "_" + course_name.upper().replace(" ", "-")

     
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")

        print(f"Học viên: {full_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_id}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirm_code}")