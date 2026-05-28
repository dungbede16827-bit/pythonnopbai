branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False] 
total = 0
while True :
    print("""
===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
""")
    choice = int(input("Nhập lựa chọn của bạn (1-4): _"))

    match choice :
        case 4:
            print("Bạn đã chọn thoát chương trình !")
            break
        case 1:
            print("----BÁO CÁO DOANH THU TỔNG HỢP----")
            print(f"{"Tên Cơ sở":<30} | {"Doanh Thu" :<30} | {"Trạng Thái " :<30}")
            print("-" * 120)
            for i in range(len(branch_names)) :
                if target_achieved[i] == True :
                    status = "Đạt"
                else :
                    status = "Không Đạt"
                print(f"{branch_names[i]:<30} | {daily_revenues[i] :<30} | {status :<30}")
                total = sum(daily_revenues)
            print("-"* 120)
            print(f"====> TONG DOANH THU TOAN VUNG: {total} VND")
        case 2 :

            max_revenue = daily_revenues[0]
            min_revenue = daily_revenues[0]

            max_branch = branch_names[0]
            min_branch = branch_names[0]

            for i in range(len(daily_revenues)) :

                if daily_revenues[i] > max_revenue :

                    max_revenue = daily_revenues[i]
                    max_branch = branch_names[i]

                if daily_revenues[i] < min_revenue :

                    min_revenue = daily_revenues[i]
                    min_branch = branch_names[i]

            print("Chi nhánh doanh thu cao nhất:")
            print(max_branch , "-" , max_revenue)

            print("Chi nhánh doanh thu thấp nhất:")
            print(min_branch , "-" , min_revenue)
        case 3 :

                failed_branches = []

                for i in range(len(branch_names)) :

                    if target_achieved[i] == False :

                        failed_branches.append(branch_names[i])

                print("Danh sách cơ sở không đạt chỉ tiêu:")
                print(failed_branches)
        case _:
            print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại!")
        