import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuot Khong Day-250000-4.8",
    "P03-Ban Phim Co-850000-4.5"
]


def display_labels():
    """
    Hiển thị tem nhãn sản phẩm.
    """

    print("\n--- DANH SÁCH TEM NHÃN ---")

    template = "Mã: {code} | Tên: {name} | Giá: {price} | Rating: {rating}*"

    for product in product_list:

        data = product.split("-")

        if len(data) != 4:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")
            continue

        code, name, price, rating = data

        info = {
            "code": f"{code:<10}",
            "name": f"{name:<20}",
            "price": f"{int(price):,} VND",
            "rating": rating
        }

        print(template.format_map(info))


def sort_products():
    """
    Sắp xếp theo rating giảm dần,
    nếu bằng nhau thì giá tăng dần.
    """

    valid_products = []

    for product in product_list:

        data = product.split("-")

        if len(data) != 4:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")
            continue

        code, name, price, rating = data

        if not price.isdigit():
            print(f"Sản phẩm {code} có giá không hợp lệ")
            continue

        valid_products.append(product)

    valid_products.sort(
        key=lambda x: (
            -float(x.split("-")[3]),
            int(x.split("-")[2])
        )
    )

    print("\n--- SẮP XẾP SẢN PHẨM ---")

    for index, product in enumerate(valid_products, start=1):
        print(f"{index}. {product}")


def calculate_total_value():
    """
    Tính tổng giá trị kho bằng reduce().
    """

    prices = []

    for product in product_list:

        data = product.split("-")

        if len(data) != 4:
            continue

        price = data[2]

        if price.isdigit():
            prices.append(int(price))

    total = functools.reduce(
        lambda acc, x: acc + x,
        prices,
        0
    )

    return total


def show_total_value():
    """
    Hiển thị tổng giá trị kho.
    """

    total = calculate_total_value()

    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND")


def main():

    while True:

        print("""
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm
2. Sắp xếp sản phẩm thông minh
3. Tính tổng giá trị kho hàng
4. Đóng hệ thống
================================================
""")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            display_labels()

        elif choice == "2":
            sort_products()

        elif choice == "3":
            show_total_value()

        elif choice == "4":
            print("Đóng hệ thống thành công!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()