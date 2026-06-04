# Các phương thức như:

# strip()
# title()
# upper()
# lower()

# không sửa chuỗi gốc mà trả về một chuỗi mới sau khi xử lý.
# Phải gán lại giá trị trả về cho biến:

# raw_diagnosis = raw_diagnosis.strip()
# raw_diagnosis = raw_diagnosis.title()

# Hoặc viết gọn:

# raw_diagnosis = raw_diagnosis.strip().title()
# extend() thêm từng phần tử của một iterable vào list.

# Chuỗi (String) cũng là một iterable, nên:

# lst = ["Sốt Xuất Huyết"]

# lst.extend("Viem Phe Quan")

# print(lst)
# Cần thay extend() bằng phương thức nào?

# Để thêm nguyên vẹn một chuỗi vào cuối danh sách, phải dùng:

# append()

# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    
    raw_diagnosis = raw_diagnosis.strip().title()

    
    current_list.append(raw_diagnosis)

    return current_list


new_diagnosis = "  viEm phE QUan  "


updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)