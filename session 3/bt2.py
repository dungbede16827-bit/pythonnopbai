# hệ thống vẫn tiếp tục chạy vì lệnh print này hiển thị cho mọi ngày nghỉ 
# mà không điều kiện gì cả 
# thêm lệnh continue bỏ qua if == 0 nên kh xét thưởng được chỉ nhận được cảnh báo


print(" --- HỆ THỐNG GỬI EMAIL THƯỜNG TẾT --- ")

# Vòng lặp chạy đúng 3 Lần cho 3 nhân viên
for employee_number in range(1, 4):
    print(" --- Đang xử lý nhan vien so", employee_number, " -- ")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input ("Nhập số ngày công trong thang: "))

    # Kiểm tra diều kiện
    if working_days == 0 :
        print ("CẢNH BÁO: Nhân viên nghi cả tháng. Không xet duyet thưởng.")
        continue # bỏ qua nếu == 0 

    bonus_amount = working_days * 200000
    print("> Đã gui Email: Chúc mung nhận dược", bonus_amount, "VNĐ tien thưởng!")
    
    print("-----------------------------------------------------\n")



print ("Đã hoan tat quá trình duyệt thưởng cho 3 nhân viên!")