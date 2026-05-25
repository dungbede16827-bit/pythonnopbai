

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


while True :
    choice = int(input("""

    ===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
    1. Hiển thị chuỗi dữ liệu gốc
    2. Chuẩn hóa dữ liệu và in báo cáo
    3. Tìm kiếm nhân viên theo mã ID
    4. Thoát chương trình

    """))
    match choice :
        case 4: 
            print("bạn đã thoát chương trình !")
            break
        case 1:
            print("raw_data")
        case 2:
            parts = raw_data.split("|")
            person_1 = parts[0]
            person_2 = parts[1]
            person_3 = parts[2]
            person_1_parts = person_1.split(";")
            person_2_parts = person_2.split(";")
            person_3_parts = person_3.split(";")
            person_1_id = person_1_parts[0].strip().upper()
            person_1_name = person_1_parts[1].strip().title()
            person_1_phone = person_1_parts[2].strip().replace("-","")
            person_1_department = person_1_parts[3].strip().title()
            person_2_id = person_2_parts[0].strip().upper()
            person_2_name = person_2_parts[1].strip().title()
            person_2_phone = person_2_parts[2].strip().replace("-","")
            person_2_department = person_2_parts[3].strip().title()
            person_3_id = person_3_parts[0].strip().upper()
            person_3_name = person_3_parts[1].strip().title()
            person_3_phone = person_3_parts[2].strip().replace("-","")
            person_3_department = person_3_parts[3].strip().title()
        case 3:
            search_id = input("Nhập mã ID nhân viên cần tìm kiếm: ").strip().upper()
            if search_id == person_1_id:
                print(f"ID: {person_1_id}, Họ tên: {person_1_name}, Số điện thoại: {person_1_phone}, Phòng ban: {person_1_department}")
            elif search_id == person_2_id:
                print(f"ID: {person_2_id}, Họ tên: {person_2_name}, Số điện thoại: {person_2_phone}, Phòng ban: {person_2_department}")
            elif search_id == person_3_id:
                print(f"ID: {person_3_id}, Họ tên: {person_3_name}, Số điện thoại: {person_3_phone}, Phòng ban: {person_3_department}")
            else:
                print("Không tìm thấy nhân viên với mã ID đã nhập.")
        case _:
            print("Mời bạn nhập lựa chọn khác !")






            