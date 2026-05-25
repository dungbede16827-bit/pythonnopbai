raw_input = "   nGuyen vaN aN  ;  2004   "

while True:

    choice = int(input(""" 
                    ===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
                        1. Hiển thị chuỗi dữ liệu gốc
                        2. Chuẩn hóa Họ tên và tính Tuổi
                        3. Tạo Mã ID và Email tự động
                        4. Thoát chương trình
                        =====================================
                        Nhập lựa chọn của bạn (1-4):


    """))
    match choice:
        case 4:
            print("Bạn đã thoát chương tình !")
            break 
        case 1:
            print("Chuỗi dữ liệu gốc hiện tại: ")
            print(f" '  nGuyen vaN aN  ;  2004   ' ")
        case 2: 
            new_full_name = raw_input.strip().split(";")
            print(f"Họ Tên : {new_full_name[0].strip().title()}")
            print(f"Tuổi: {2026 - int(new_full_name[1].strip())}")
        case 3:
            data = raw_input.strip().split(";")

            name = data[0].strip().title()
            birth = data[1].strip()

            words = name.split()

            ho = words[0]
            ten_dem = words[1]
            ten = words[2]

            email = (ho[0] + ten_dem[0] + ten).lower() + "@company.com"

            member_id = ten.upper() + birth[-2:]

            print("\n===== THẺ THÀNH VIÊN =====")
            print(f"Họ tên : {name}")
            print(f"Mã ID  : {member_id}")
            print(f"Email  : {email}")
            
        case _:
            print("mời bạn nhập lựa chọn khác ")
