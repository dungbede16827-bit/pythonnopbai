# Phân tích Input / Output
# Input
# Dữ liệu	Kiểu dữ liệu	Mô tả
# menu_choice	string	Người dùng chọn chức năng từ menu
# order_code	string	Mã đơn hàng nhập vào khi thêm hoặc xóa
# Output
# Hiển thị danh sách đơn hàng.
# Thông báo thêm đơn hàng thành công.
# Thông báo xóa thành công / không tìm thấy mã.
# Thông báo lỗi nhập menu.
# Thông báo thoát chương trình.
# Sử dụng List

# Danh sách đơn hàng:

# Sử dụng các phương thức phù hợp
# Chức năng	Phương thức
# Thêm đơn	append()
# Xóa đơn	remove()
# Kiểm tra tồn tại	in
# Chuẩn hóa dữ liệu	strip(), upper()

# Kiểm tra dữ liệu hợp lệ
# Kiểm tra menu

# Cho phép:

# 1,2,3,4

# Nếu nhập khác:

# chữ cái
# số ngoài phạm vi
# báo lỗi.
# Chuẩn hóa mã đơn hàng

# Dùng:

# strip()
# upper()
# Dùng vòng lặp:

# while True


order_list = ["GE001", "GE002", "GE003"]

while True:

    print("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Xóa đơn hàng theo mã
4. Thoát chương trình
""")

    menu_choice = input("Nhập lựa chọn: ").strip()

    if menu_choice == "1":

        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")

        else:
            print("Danh sách đơn hàng hiện tại:")

            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")

    elif menu_choice == "2":

        new_order = input(
            "Nhập mã đơn hàng mới: "
        ).strip().upper()

        order_list.append(new_order)

        print("Thêm đơn hàng thành công!")

    elif menu_choice == "3":

        delete_order = input(
            "Nhập mã đơn hàng cần xóa: "
        ).strip().upper()

        if delete_order in order_list:

            order_list.remove(delete_order)

            print("Xóa đơn hàng thành công!")

        else:

            print(
                "Không tìm thấy mã đơn hàng cần xóa!"
            )


    elif menu_choice == "4":

        print("Thoát chương trình.")
        break

  
    else:

        print(
            "Lựa chọn không hợp lệ, vui lòng nhập lại!"
        )