# Input
# Lựa chọn menu của người dùng (string).
# Mã sản phẩm, tên sản phẩm (string).
# Giá sản phẩm (int).
# Số lượng sản phẩm (int).
# Output
# Danh sách sản phẩm hiện tại.
# Thông báo thêm / cập nhật / xóa thành công.
# Thông báo lỗi dữ liệu không hợp lệ.
# Thông báo thoát chương trình.
# Giải pháp

# Dùng:

# List lưu toàn bộ sản phẩm.
# Dictionary  lưu thông tin 1 sản phẩm.

# Các phương thức sử dụng:

# .strip()  xóa khoảng trắng.
# .upper()  chuyển mã sang in hoa.
# append()  thêm sản phẩm.
# remove()  xóa sản phẩm.
# vòng lặp for.
# try-except kiểm tra nhập số.

product_list = [

    {
        "product_id":"SP001",
        "product_name":"Áo polo nam",
        "price":299000,
        "quantity":20
    },

    {
        "product_id":"SP002",
        "product_name":"Quần kaki nam",
        "price":399000,
        "quantity":15
    },

    {
        "product_id":"SP003",
        "product_name":"Váy công sở nữ",
        "price":459000,
        "quantity":10
    }

]

while True:

    print("""
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====

1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
""")

    choice = input("Nhập lựa chọn: ")

  
    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")

        else:

            print("Danh sách sản phẩm hiện tại:")

            for i, product in enumerate(product_list,1):

                print(
                    f"{i}. "
                    f"Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Số lượng: {product['quantity']}"
                )

  
    elif choice == "2":

        product_id = input(
            "Nhập mã sản phẩm: "
        ).strip().upper()

        duplicate = False

        for product in product_list:

            if product["product_id"] == product_id:
                duplicate = True
                break

        if duplicate:
            print("Mã sản phẩm bị trùng")

        else:

            product_name = input(
                "Nhập tên sản phẩm: "
            )

            try:

                price = int(
                    input("Nhập giá sản phẩm: ")
                )

                quantity = int(
                    input("Nhập số lượng sản phẩm: ")
                )

                if price <=0 or quantity <=0:
                    print(
                        "Giá/Số lượng không hợp lệ"
                    )

                else:

                    new_product = {

                        "product_id":product_id,
                        "product_name":product_name,
                        "price":price,
                        "quantity":quantity
                    }

                    product_list.append(new_product)

                    print(
                        "Thêm sản phẩm thành công"
                    )

            except:
                print(
                    "Giá/Số lượng không hợp lệ"
                )

    
    elif choice == "3":

        product_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                product["product_name"] = input(
                    "Tên mới: "
                )

                try:

                    price = int(
                        input("Giá mới: ")
                    )

                    quantity = int(
                        input("Số lượng mới: ")
                    )

                    if price<=0 or quantity<=0:

                        print(
                            "Giá/Số lượng không hợp lệ"
                        )

                    else:

                        product["price"] = price
                        product["quantity"] = quantity

                        print(
                            "Cập nhật thành công"
                        )

                except:
                    print(
                        "Giá/Số lượng không hợp lệ"
                    )

                break

        if found == False:

            print(
                "Không tìm thấy mã sản phẩm cần cập nhật!"
            )

   
    elif choice == "4":

        product_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                product_list.remove(product)

                found = True

                print(
                    "Xóa sản phẩm thành công"
                )

                break

        if found == False:

            print(
                "Không tìm thấy mã sản phẩm cần xoá!"
            )

  
    elif choice == "5":

        print("Thoát chương trình.")

        break

    
    else:

        print(
            "Lựa chọn không hợp lệ, vui lòng nhập lại!"
        )