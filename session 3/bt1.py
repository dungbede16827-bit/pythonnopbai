# total_budget không cộng dồn mà chỉ dữ lại lần nhập cuối cùng vì 
# khởi tạo bên trong vòng lặp mỗi lần lặp mới biến tổng lại khởi tạo lại 
# = 0 một lần nữa nên chỉ in lại một lần cuối

total_budget = 0
print(" --- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG --- ")

# Vòng lặp chạy 3 lần dể nhập Lương cho 3 nhân viên
for employee_number in range(1, 4):

    # Khởi tạo chiếc hộp dựng tổng tiên

    print ("Đang xử lý nhân viên số", employee_number)
    # Nhập mức Lương
    salary = int(input(" Nhập mức Lương (VNĐ): "))

    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print ("= KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẤN BỊ LÀ:", total_budget, "VNĐ")