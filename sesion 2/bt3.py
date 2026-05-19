# # # phân tích input 
# # # nhập vào họ và tên bệnh nhân kiểu string
# # # tuổi bênh nhân kiểu int 
# # out put 
# # Hệ thống in Phiếu khám bệnh điện tử gồm:
# # Tên bệnh nhân
# # Tuổi
# # Kết quả phân luồng
# # Trường hợp lỗi
# # Nếu:
# # tên rỗng
# # chỉ nhập khoảng trắng
# # tuổi âm
# # tuổi > 150
# # => hệ thống báo lỗi và kết thúc chương trình.
# # Sử dụng:
# # if-elif-else
# # toán tử logic or
# # hàm .strip()
# # ý tưởng Bước 1 — Kiểm tra dữ liệu lỗi
# # Bước 2 — Phân luồng bệnh nhân
# # < 6 tuổi
# #  Bệnh nhi
# # >= 80 tuổi
# #  Người cao tuổi
# # còn lại
# #  Khám thường

# Nhập tên bệnh nhân
# Nhập tuổi bệnh nhân
# Nếu tên rỗng hoặc chỉ chứa khoảng trắng
#     In thông báo lỗi
#     Kết thúc chương trình
# Nếu tuổi < 0 hoặc tuổi > 150
#     In thông báo lỗi
#     Kết thúc chương trình
# Nếu tuổi < 6
#     Phân luồng = "ƯU TIÊN: Bệnh nhi"
# Ngược lại nếu tuổi >= 80
#     Phân luồng = "ƯU TIÊN: Người cao tuổi"
# Ngược lại
#     Phân luồng = "KHÁM THƯỜNG"
# In phiếu khám bệnh
# KẾT THÚC

print("===== HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN =====")
patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))

if patient_name.strip() == "":
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
elif patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else:

    if patient_age < 6:
        result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."

    elif patient_age >= 80:
        result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print(f"""
===== PHIẾU KHÁM BỆNH =====

Tên bệnh nhân: {patient_name}
Tuổi: {patient_age}

Kết quả phân luồng:
{result}
""")