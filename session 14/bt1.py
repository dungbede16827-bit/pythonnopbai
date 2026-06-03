# Thứ tự tham số là:

# price
# discount
# shipping_fee

# Nhưng chương trình gọi:
# calculate_final_price(100000, 15000, 0.1)
# Python sẽ gán theo đúng vị trí truyền vào:

# price = 100000
# discount = 15000
# shipping_fee = 0.1
# Công thức trong hàm:

# total = price - (price * discount) + shipping_fee

# Sau khi gán sai tham số:

# total = 100000 - (100000 * 15000) + 0.1

# Ta có:

# 100000 * 15000 = 1500000000

# Nên:

# total = 100000 - 1500000000 + 0.1
#        = -1499900000 + 0.1
#        = -1499899999.9

# Hàm hiện tại chỉ dùng:

# print(...)

# mà không có return.

# Trong Python, hàm không có return sẽ tự động trả về:

# None

# Do đó:

# order_total = None

# Khi chạy:

# None + 5000

# Python không thể cộng kiểu NoneType với int.

# => sinh lỗi:
# TypeError
# Giá trị của order_total:

# None

# Vì:

# calculate_final_price()

# không trả về dữ liệu nào.

# Python mặc định:

# return None
# print(total)	return total
# Chỉ hiển thị ra màn hình	Trả kết quả về nơi gọi hàm
# Không lưu để tính tiếp	Có thể gán biến, dùng tiếp
# Không thay đổi giá trị trả về của hàm	Quyết định giá trị trả về
# Cần sửa 2 điểm:

# 1. Truyền đúng thứ tự tham số

# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total

# Gọi hàm đúng thứ tự tham số
order_total = calculate_final_price(100000, 0.1, 15000)

# Cộng thêm phí đóng gói
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)
