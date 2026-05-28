# Sau khi chạy lệnh:
# delivery_orders.insert(0, "GE000")
# Danh sách thay đổi như sau:
# Ban đầu:
# ["GE001", "GE002", "GE003-CANCEL", "GE004"]
# Sau khi chèn:
# ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"]
# Giải thích:
# insert(index, value) chèn phần tử vào vị trí chỉ định.
# "GE000" được chèn vào index = 0.
# Các phần tử phía sau bị dịch sang phải 1 vị trí.
# delivery_orders[1] = "GE002-UPDATED"

# Sau khi chèn "GE000" vào đầu danh sách:
# delivery_orders[1] là "GE001" chứ không phải "GE002".

# => Code đã sửa nhầm đơn hàng.
# Sau khi chèn "GE000", "GE002" nằm ở index 2
# delivery_orders.remove(3) lỗi 
# remove() xóa theo giá trị, không xóa theo vị trí.

# Code đang tìm phần tử có giá trị 3.

# Trong danh sách không tồn tại số 3.

# Nên Python báo lỗi.
# remove() xóa theo giá trị.
# Biến transferred_order chưa được tạo.

# pop() được gọi nhưng kết quả trả về không lưu vào biến.
# Muốn lưu đơn hàng lấy ra bằng pop() transferred_order = delivery_orders.pop()


delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
delivery_orders.append("GE004")

delivery_orders.insert(0, "GE000")

delivery_orders[2] = "GE002-UPDATED"

delivery_orders.remove("GE003-CANCEL")

transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)