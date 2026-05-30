# Input
# Lựa chọn menu của người dùng (string).
# Mã sản phẩm (string).
# Số lượng mua / nhập kho (int).
# Dữ liệu sản phẩm trong product_list (list + dictionary).
# Output
# Danh sách sản phẩm và trạng thái tồn kho.
# Thông báo bán hàng / nhập kho thành công hoặc lỗi dữ liệu.
# Báo cáo doanh thu, tổng doanh thu, sản phẩm bán chạy nhất.
# Thông báo thoát chương trình.
#  Đề xuất giải pháp
# Dùng List lưu danh sách sản phẩm.
# Dùng Dictionary lưu thông tin từng sản phẩm.
# Dùng .strip().upper() để chuẩn hóa mã sản phẩm.
# Dùng try-except, if, for, append(), cập nhật dữ liệu để kiểm tra hợp lệ và xử lý chương trình.

product_list = [

    {"product_id":"SP001","product_name":"Áo polo nam","price":299000,"quantity":20,"sold":5},

    {"product_id":"SP002","product_name":"Quần kaki nam","price":399000,"quantity":8,"sold":3},

    {"product_id":"SP003","product_name":"Váy công sở nữ","price":459000,"quantity":3,"sold":7}

]

while True:

    print("""
===== HỆ THỐNG VẬN HÀNH YODY =====

1. Hiển thị sản phẩm
2. Bán sản phẩm
3. Nhập thêm hàng
4. Xem doanh thu
5. Thoát
""")

    choice = input("Nhập lựa chọn: ")

    # HIỂN THỊ
    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách trống")

        else:

            for product in product_list:

                if product["quantity"] == 0:
                    status = "Hết hàng"

                elif product["quantity"] <= 5:
                    status = "Sắp hết"

                else:
                    status = "Còn hàng"

                print(
                    product["product_id"],
                    product["product_name"],
                    product["price"],
                    product["quantity"],
                    product["sold"],
                    status
                )

    # BÁN HÀNG
    elif choice == "2":

        code = input("Nhập mã sản phẩm: ")
        code = code.strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == code:

                found = True

                try:

                    amount = int(
                        input("Nhập số lượng mua: ")
                    )

                    if amount <=0:

                        print(
                            "Số lượng không hợp lệ"
                        )

                    elif amount > product["quantity"]:

                        print(
                            "Không đủ hàng"
                        )

                    else:

                        product["quantity"] = product["quantity"] - amount

                        product["sold"] = product["sold"] + amount

                        money = amount * product["price"]

                        print(
                            "Tiền phải trả:",
                            money
                        )

                except:

                    print(
                        "Số lượng không hợp lệ"
                    )

        if found == False:

            print(
                "Không tìm thấy sản phẩm"
            )

    # NHẬP HÀNG
    elif choice == "3":

        code = input("Nhập mã sản phẩm: ")
        code = code.strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == code:

                found = True

                try:

                    amount = int(
                        input("Nhập số lượng thêm: ")
                    )

                    if amount <=0:

                        print(
                            "Số lượng không hợp lệ"
                        )

                    else:

                        product["quantity"] = product["quantity"] + amount

                        print(
                            "Nhập kho thành công"
                        )

                except:

                    print(
                        "Số lượng không hợp lệ"
                    )

        if found == False:

            print(
                "Không tìm thấy sản phẩm"
            )

    # DOANH THU
    elif choice == "4":

        total = 0
        max_sold = 0
        best_name = ""

        for product in product_list:

            revenue = product["price"] * product["sold"]

            total = total + revenue

            print(
                product["product_name"],
                "Đã bán:",
                product["sold"],
                "Doanh thu:",
                revenue
            )

            if product["sold"] > max_sold:

                max_sold = product["sold"]

                best_name = product["product_name"]

        print(
            "Tổng doanh thu:",
            total
        )

        print(
            "Bán chạy nhất:",
            best_name
        )

    # THOÁT
    elif choice == "5":

        print("Thoát chương trình")

        break

    else:

        print(
            "Lựa chọn không hợp lệ"
        )