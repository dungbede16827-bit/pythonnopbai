tong_tien = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

if tong_tien >= 500000:
    giam_gia = tong_tien * 10 // 100
else:
    giam_gia = 0

thanh_toan = tong_tien - giam_gia

print("HÓA ĐƠN THANH TOÁN RIKKEI STORE")
print("Số tiền được giảm giá:", giam_gia, "VND")
print("Tổng tiền khách phải trả:", thanh_toan, "VND")