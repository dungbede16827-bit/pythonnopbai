# Sau khi chạy lệnh
# express_orders.insert(0, "GE100-FAST")

# Danh sách thay đổi như sau.

# Ban đầu:

# ['GE101', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']

# Sau khi chèn:

# ['GE100-FAST', 'GE101', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']

# Giải thích:

# insert(0, value) chèn phần tử vào vị trí đầu danh sách.
# Các phần tử cũ bị đẩy sang phải 1 vị trí.

# express_orders[1] = "GE102-UPDATED"

# Sau khi chèn "GE100-FAST":

# Index	Giá trị
# 0	GE100-FAST
# 1	GE101
# 2	GE102-WRONG
# 3	GE103-CANCEL
# 4	GE104

# index 1 lúc này là "GE101".

# Do đó code đã sửa "GE101" thay vì "GE102-WRONG".

# index = 2
# express_orders.pop(3)

# Sau khi insert và sửa dữ liệu, danh sách trở thành:

# ['GE100-FAST', 'GE102-UPDATED', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']

# pop(3) xóa phần tử ở vị trí số 3.

# Nhưng do trước đó sửa sai index nên dữ liệu đã bị lệch.

# Cách làm đúng nên dùng:

# remove("GE103-CANCEL")

# vì đề bài yêu cầu xóa theo giá trị đơn hàng.
# express_orders.remove("GE103-CANCEL")

# remove() xóa theo giá trị, không xóa theo vị trí.
# pop() mặc định lấy phần tử cuối cùng của danh sách.
# current_order = express_orders.pop()

# pop() không có tham số  lấy phần tử cuối.
# Trong khi yêu cầu nghiệp vụ cần lấy đơn hàng đầu tiên:
# current_order = express_orders.pop(0)

express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]


express_orders.append("GE104")

express_orders.insert(0, "GE100-FAST")

express_orders[2] = "GE102-UPDATED"

express_orders.remove("GE103-CANCEL")

current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)