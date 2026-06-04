blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


def find_blood_bag(inventory, blood_id):
    blood_id = blood_id.strip().upper()

    for i in range(len(inventory)):
        if inventory[i].startswith(blood_id + "-"):
            return i

    return -1


def display_inventory(inventory):
    print("\n--- DANH SÁCH KHO MÁU ---")

    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    total_volume = 0

    print("Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("-" * 62)

    for blood in inventory:
        data = blood.rsplit("-", 4)

        blood_id = data[0]
        donor = data[1]
        blood_type = data[2]
        volume = data[3]
        expiry = data[4]

        total_volume += int(volume)

        print(
            f"{blood_id:<6} | "
            f"{donor:<15} | "
            f"{blood_type:<8} | "
            f"{volume} ml   | "
            f"{expiry}"
        )

    print("-" * 62)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    blood_id = input("Nhập mã túi máu mới: ").strip().upper()

    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    if find_blood_bag(inventory, blood_id) != -1:
        print(f"\nLỗi: Mã túi máu {blood_id} đã tồn tại! Vui lòng nhập mã khác.")
        return

    donor = input("Nhập tên người hiến: ").strip().title()

    if donor == "":
        print("\nLỗi: Tên người hiến không được để trống!")
        return

    blood_type = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()

    if not volume.isdigit():
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    if int(volume) <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_blood = "-".join([
        blood_id,
        donor,
        blood_type,
        volume,
        expiry
    ])

    inventory.append(new_blood)

    print(f"\nThành công: Đã nhập túi máu {blood_id} vào kho!")
    print("\nDữ liệu lưu:")
    print(new_blood)


def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    blood_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()

    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    new_expiry = input("Nhập ngày hết hạn mới: ").strip()

    data = inventory[index].rsplit("-", 4)

    data[4] = new_expiry

    inventory[index] = "-".join(data)

    print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {blood_id}!")


def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    blood_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()

    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    inventory.pop(index)

    print(f"\nThành công: Đã xuất túi máu {blood_id} khỏi kho!")


def main():
    while True:

        print("""
=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===
1. Xem danh sách túi máu trong kho
2. Nhập túi máu mới
3. Gia hạn / Sửa ngày hết hạn
4. Xuất / Hủy túi máu
5. Thoát chương trình
========================================
""")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_inventory(blood_inventory)

        elif choice == "2":
            add_blood_bag(blood_inventory)

        elif choice == "3":
            update_expiry(blood_inventory)

        elif choice == "4":
            remove_blood_bag(blood_inventory)

        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


main()