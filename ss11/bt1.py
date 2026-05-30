# Tuple có 4 phần tử.

# Index	Giá trị
# 0	SP001
# 1	Áo polo nam
# 2	Size L
# 3	299000
# SP001 nằm ở:

# index 0
# product_code = product_info[1] không phải mã sản phẩm.
# product_code = product_info[0]
# "Áo polo nam" nằm ở 

# index 1

# product_info[2]

# là:

# "Size L"

# không phải tên sản phẩm  index 1
# product_length = product_info.length()

# Tuple không có hàm:

# length()

# nên gây lỗi
# Dùng:

# len()

# Đúng:

# product_length = len(product_info)
# product_info[3] = 279000

# Vì tuple là immutable.

# Không cho phép sửa trực tiếp phần tử.


product_info = (
    "SP001",
    "Áo polo nam",
    "Size L",
    299000
)

product_code = product_info[0]


product_name = product_info[1]


product_length = len(product_info)


product_info = (
    product_info[0],
    product_info[1],
    product_info[2],
    279000
)

print("Mã sản phẩm:", product_code)

print("Tên sản phẩm:", product_name)

print(
    "Số lượng thông tin sản phẩm:",
    product_length
)

print(
    "Thông tin sản phẩm sau cập nhật:",
    product_info
)