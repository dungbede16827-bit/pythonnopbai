product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:

    print("""
===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm
2. Bán sản phẩm cho khách hàng
3. Xử lý đổi trả sản phẩm
4. Áp dụng giảm giá cho sản phẩm
5. Nhập thêm hàng vào kho cửa hàng
6. Thoát chương trình
""")

    choice = input(
        "Mời bạn nhập lựa chọn: "
    ).strip()

    if not choice.isdigit():

        print(
            "Lựa chọn không hợp lệ!"
        )

        continue

    choice = int(choice)

    match choice:

        # CASE 1
        case 1:

            if len(product_list) == 0:

                print(
                    "Danh sách sản phẩm trống"
                )

            else:

                for index, product in enumerate(
                        product_list,
                        start=1
                ):

                    if product["quantity"] == 0:

                        status = "Hết hàng"

                    elif product["quantity"] <= 5:

                        status = "Sắp hết hàng"

                    else:

                        status = "Còn hàng"

                    print(
                        f"{index}. "
                        f"Mã: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Tồn kho: {product['quantity']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Đổi trả: {product['returned']} | "
                        f"Giảm giá: {product['discount']}% | "
                        f"Trạng thái: {status}"
                    )

        # CASE 2
        case 2:

            product_id = input(
                "Nhập mã sản phẩm khách muốn mua: "
            ).strip().upper()

            found = False

            for product in product_list:

                if product["product_id"] == product_id:

                    found = True

                    quantity_buy = input(
                        "Nhập số lượng khách mua: "
                    )

                    if not quantity_buy.isdigit():

                        print(
                            "Số lượng mua không hợp lệ"
                        )

                    else:

                        quantity_buy = int(
                            quantity_buy
                        )

                        if quantity_buy <= 0:

                            print(
                                "Số lượng phải lớn hơn 0"
                            )

                        elif quantity_buy > product["quantity"]:

                            print(
                                "Số lượng trong kho không đủ để bán"
                            )

                        else:

                            final_price = (
                                product["price"]
                                * (100-product["discount"])
                                /100
                            )

                            total_money = (
                                final_price
                                * quantity_buy
                            )

                            product["quantity"] -= quantity_buy

                            product["sold"] += quantity_buy

                            print(
                                "Bán sản phẩm thành công"
                            )

                            print(
                                f"Tổng tiền: {total_money:.0f} VNĐ"
                            )

            if found == False:

                print(
                    "Không tìm thấy sản phẩm cần bán"
                )

        # CASE 3
        case 3:

            product_id = input(
                "Nhập mã sản phẩm khách muốn đổi/trả: "
            ).strip().upper()

            found = False

            for product in product_list:

                if product["product_id"] == product_id:

                    found = True

                    quantity_return = input(
                        "Nhập số lượng đổi/trả: "
                    )

                    if not quantity_return.isdigit():

                        print(
                            "Số lượng đổi/trả không hợp lệ"
                        )

                    else:

                        quantity_return = int(
                            quantity_return
                        )

                        if quantity_return <= 0:

                            print(
                                "Số lượng phải lớn hơn 0"
                            )

                        elif quantity_return > product["sold"]:

                            print(
                                "Số lượng đổi/trả không được vượt quá số lượng đã bán"
                            )

                        else:

                            product["sold"] -= quantity_return

                            product["quantity"] += quantity_return

                            product["returned"] += quantity_return

                            final_price = (
                                product["price"]
                                * (100-product["discount"])
                                /100
                            )

                            refund_money = (
                                final_price
                                * quantity_return
                            )

                            print(
                                "Đổi trả thành công"
                            )

                            print(
                                f"Tiền hoàn: {refund_money:.0f} VNĐ"
                            )

            if found == False:

                print(
                    "Không tìm thấy sản phẩm cần đổi trả"
                )

        # CASE 4
        case 4:

            product_id = input(
                "Nhập mã sản phẩm cần giảm giá: "
            ).strip().upper()

            found = False

            for product in product_list:

                if product["product_id"] == product_id:

                    found = True

                    discount = input(
                        "Nhập phần trăm giảm giá: "
                    )

                    if not discount.isdigit():

                        print(
                            "Phần trăm giảm giá không hợp lệ"
                        )

                    else:

                        discount = int(discount)

                        if discount < 0 or discount > 70:

                            print(
                                "Giảm giá chỉ từ 0-70%"
                            )

                        else:

                            product["discount"] = discount

                            print(
                                "Áp dụng giảm giá thành công"
                            )

            if found == False:

                print(
                    "Không tìm thấy sản phẩm"
                )

        # CASE 5
        case 5:

            product_id = input(
                "Nhập mã sản phẩm cần nhập thêm: "
            ).strip().upper()

            found = False

            for product in product_list:

                if product["product_id"] == product_id:

                    found = True

                    quantity_add = input(
                        "Nhập số lượng nhập thêm: "
                    )

                    if not quantity_add.isdigit():

                        print(
                            "Số lượng nhập không hợp lệ"
                        )

                    else:

                        quantity_add = int(
                            quantity_add
                        )

                        if quantity_add <= 0:

                            print(
                                "Số lượng phải lớn hơn 0"
                            )

                        else:

                            product["quantity"] += quantity_add

                            print(
                                "Nhập hàng thành công"
                            )

            if found == False:

                print(
                    "Không tìm thấy sản phẩm"
                )

        # CASE 6
        case 6:

            print(
                "Bạn đã thoát chương trình"
            )

            break

        case _:

            print(
                "Lựa chọn không hợp lệ!"
            )