from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()

    for i in range(len(records)):
        if records[i].startswith(patient_id + "-"):
            return i

    return -1


def display_records(records):
    print("\n--- DANH SÁCH BỆNH NHÂN ---")

    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    for i in range(len(records)):
        data = records[i].split("-")

        print(
            f"{i+1}. [{data[0]}] {data[1]} | "
            f"Năm sinh: {data[2]} | "
            f"Chẩn đoán: {data[3]}"
        )

    print("-" * 70)


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ")
    patient_name = patient_name.replace("-", " ")
    patient_name = patient_name.strip().title()

    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if not birth_year.isdigit():
            print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        birth_year = int(birth_year)

        if birth_year < 1900 or birth_year > current_year:
            print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        break

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.replace("-", " ")
    diagnosis = diagnosis.strip().capitalize()

    record = (
        patient_id
        + "-"
        + patient_name
        + "-"
        + str(birth_year)
        + "-"
        + diagnosis
    )

    records.append(record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print(record)


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    )

    new_diagnosis = new_diagnosis.replace("-", " ")
    new_diagnosis = new_diagnosis.strip().capitalize()

    data[3] = new_diagnosis

    records[index] = "-".join(data)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[index])


def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    current_year = datetime.now().year

    tre_em = 0
    truong_thanh = 0
    nguoi_gia = 0

    for record in records:
        data = record.split("-")

        age = current_year - int(data[2])

        if age < 16:
            tre_em += 1
        elif age <= 60:
            truong_thanh += 1
        else:
            nguoi_gia += 1

    print(f"Trẻ em: {tre_em} bệnh nhân")
    print(f"Trưởng thành: {truong_thanh} bệnh nhân")
    print(f"Người cao tuổi: {nguoi_gia} bệnh nhân")
    print("-" * 40)


while True:

    print("""
===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====
1. Xem danh sách hồ sơ bệnh án
2. Thêm hồ sơ bệnh nhân mới
3. Cập nhật chẩn đoán theo Mã BN
4. Báo cáo phân loại theo độ tuổi
5. Thoát chương trình
==================================================
""")

    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        display_records(patient_records)

    elif choice == "2":
        add_patient(patient_records)

    elif choice == "3":
        update_diagnosis(patient_records)

    elif choice == "4":
        generate_age_report(patient_records)

    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")