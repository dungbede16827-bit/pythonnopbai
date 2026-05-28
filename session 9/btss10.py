# Input
# Dữ liệu	Kiểu dữ liệu	Mô tả
# choice	int	Người dùng chọn menu từ 1–5
# product_id	string	Mã sản phẩm
# product_name	string	Tên sản phẩm
# quantity	int	Số lượng sản phẩm
# price	int	Đơn giá sản phẩm
# Output
# Hiển thị danh sách sản phẩm trong giỏ hàng.
# Hiển thị tổng số lượng sản phẩm.
# Hiển thị tổng tiền của giỏ hàng.
# Thông báo thêm sản phẩm thành công.
# Thông báo cập nhật thành công.
# Thông báo xóa thành công.
# Thông báo lỗi nếu dữ liệu không hợp lệ.

cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True :

    print("""
===== HỆ THỐNG QUẢN LÝ GIỎ HÀNG SHOPEE =====
1. Xem chi tiết giỏ hàng và Tổng tiền
2. Thêm sản phẩm mới hoặc Tăng số lượng
3. Cập nhật số lượng sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
""")

    try :

        choice = int(input("Nhập lựa chọn: "))

        match choice :

            case 1 :

                total_quantity = 0
                total_money = 0

                print("===== GIỎ HÀNG =====")

                for product in cart_items :

                    product_id = product[0]
                    product_name = product[1]
                    quantity = product[2]
                    price = product[3]

                    print("Mã:", product_id)
                    print("Tên:", product_name)
                    print("Số lượng:", quantity)
                    print("Đơn giá:", price)
                    print("-------------------")

                    total_quantity = total_quantity + quantity
                    total_money = total_money + quantity * price

                print("Tổng số lượng:", total_quantity)
                print("Tổng tiền:", total_money)

            case 2 :

                product_id = input("Nhập mã sản phẩm: ").upper()
                product_name = input("Nhập tên sản phẩm: ")

                quantity = int(input("Nhập số lượng: "))
                price = int(input("Nhập đơn giá: "))

                if quantity <= 0 or price < 0 :

                    print("Dữ liệu không hợp lệ!")

                else :

                    found = False

                    for product in cart_items :

                        old_id = product[0]

                        if old_id == product_id :

                            product[2] = product[2] + quantity

                            found = True

                            print("Đã tăng số lượng.")

                    if found == False :

                        new_product = []

                        new_product.append(product_id)
                        new_product.append(product_name)
                        new_product.append(quantity)
                        new_product.append(price)

                        cart_items.append(new_product)

                        print("Đã thêm sản phẩm mới.")

            case 3 :

                product_id = input("Nhập mã cần cập nhật: ").upper()

                new_quantity = int(
                    input("Nhập số lượng mới: ")
                )

                if new_quantity <= 0 :

                    print("Số lượng không hợp lệ!")

                else :

                    found = False

                    for product in cart_items :

                        if product[0] == product_id :

                            product[2] = new_quantity

                            found = True

                            print("Cập nhật thành công.")

                    if found == False :

                        print(
                            "Mã sản phẩm không tồn tại trong giỏ hàng."
                        )

            case 4 :

                product_id = input(
                    "Nhập mã sản phẩm cần xóa: "
                ).upper()

                found = False

                for product in cart_items :

                    if product[0] == product_id :

                        cart_items.remove(product)

                        found = True

                        print("Xóa thành công.")

                        break

                if found == False :

                    print(
                        "Mã sản phẩm không tồn tại trong giỏ hàng."
                    )

            case 5 :

                print("Thoát chương trình.")
                break

            case _ :

                print("Lựa chọn không hợp lệ!")

    except :

        print("Lựa chọn không hợp lệ!")