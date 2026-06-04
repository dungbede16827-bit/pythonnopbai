# Do dòng lệnh:

# new_prescription = old_prescription

# không tạo ra một List mới.

# Python chỉ tạo thêm một biến mới (new_prescription) cùng trỏ đến vùng nhớ chứa danh sách mà old_prescription đang sử dụng.

# ũng thay đổi theo vì cả a và b đang tham chiếu đến cùng một List.

# Do đó:

# new_prescription.append("Oresol")

# thực chất đang thêm phần tử trực tiếp vào danh sách của:

# yesterday_prescription

# làm hỏng dữ liệu lịch sử.
# Cách 1: Dùng copy()
# new_prescription = old_prescription.copy()
# Cách 2: Dùng slicing
# new_prescription = old_prescription[:]
# Cách 3: Dùng hàm list()
# new_prescription = list(old_prescription)

# Cả ba cách trên đều tạo ra một List mới độc lập với List gốc.
# new_prescription[0].replace("Panadol", "Paracetamol")

# không làm thay đổi dữ liệu trong List vì:

# String trong Python là Immutable (bất biến).
# replace() không sửa chuỗi cũ.
# replace() trả về một chuỗi mới.
# Phải gán lại giá trị mới vào vị trí index tương ứng:

# new_prescription[0] = new_prescription[0].replace(
#     "Panadol",
#     "Paracetamol"
# )

# Hoặc đơn giản hơn:

# new_prescription[0] = "Paracetamol"

# Sau khi gán lại, phần tử đầu tiên của List mới thực sự được cập nhật.

# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = [
    "Panadol",
    "Vitamin C",
    "Amoxicillin"
]

def update_prescription(old_prescription):


    new_prescription = old_prescription.copy()


    new_prescription[0] = new_prescription[0].replace("Panadol","Paracetamol")


    new_prescription.append("Oresol")

    return new_prescription


today_prescription = update_prescription(
    yesterday_prescription
)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)