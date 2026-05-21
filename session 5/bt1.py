# Vòng lặp ngoài duyệt theo tháng trước, sau đó mới duyệt theo chi nhánh.

# Điều này khiến dữ liệu được xử lý theo thứ tự:
# tháng 1 tất cả chi nhánh
# tháng 2 tất cả chi nhánh
# tháng 3 tất cả chi nhánh
# Kết quả báo cáo sẽ là:

# Chi nhánh 1 tháng 1
# Chi nhánh 2 tháng 1
# Chi nhánh 3 tháng 1

# Trong khi yêu cầu nghiệp vụ cần:

# Chi nhánh 1 tháng 1
# Chi nhánh 1 tháng 2
# Chi nhánh 1 tháng 3
# Tức là phải gom toàn bộ doanh thu của từng chi nhánh lại với nhau để dễ theo dõi và đối chiếu.

# Vòng lặp ngoài phải duyệt theo chi nhánh
# Vòng lặp trong phải duyệt theo tháng

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

for branch in range(1, branch_count + 1):

    for month in range(1, month_count + 1):

        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: ")
        )

        print(
            f"Chi nhánh {branch}, tháng {month}: "
            f"{revenue} triệu đồng"
        )


