# Dữ liệu đầu vào (Input)
# Điều dưỡng nhập dữ liệu từ bàn phím nên ban đầu tất cả dữ liệu đều có kiểu:
# String
# Dữ liệu đầu ra mong muốn (Output)
# Sau khi xử lý, hệ thống phải chuẩn hóa dữ liệu thành đúng kiểu:
# Thông tin	Kiểu dữ liệu mong muốn
# Mã bệnh nhân	String
# Nhiệt độ	Float
# Nhịp tim	Integer
# Giải pháp 1: Ép kiểu trực tiếp khi nhập
# Ý tưởng

# Sử dụng hàm float() và int() ngay trong lệnh input().
# Giải pháp 2: Nhập chuỗi trước rồi ép kiểu sau
# Ý tưởng

# Lưu dữ liệu nhập vào dưới dạng chuỗi, sau đó mới chuyển kiểu dữ liệu.

ma_benh_nhan = input("Nhập mã bệnh nhân: ")
nhiet_do = float(input("Nhập nhiệt độ: "))
nhip_tim = int(input("Nhập nhịp tim: "))
print(f"""--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU \n
Mã bệnh nhân: {ma_benh_nhan} \n
Nhiệt dộ cơ thể: {nhiet_do} độ c
Kiểu dữ liệu hệ thống ghi nhận: {type(nhiet_do)}
Nhịp tim: {nhip_tim} nhịp/phút
Kiểu dữ liệu hệ thống ghi nhận: {type(nhip_tim)}

Thông báo: Dữ Liệu hợp Lệ. Màn hình Monitor dã sẵn sang ket noi!""") 