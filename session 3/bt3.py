# mã nhân viên string 
# họ và tên nhân viên string 
# phòng công tác string 
# dùng vòng lặp 3 lần

for i in range(1,4, 1) :
        print(f"Nhân viên thứ {i}")
        id = input("Mã nhân viên :")
        name = input("Họ và tên nhân viên :  ")
        work_room = input("Phòng ban công tác : ")

        if(id == "" or name == "" ) :
            print("[CẢNH BÁO] Dữ Liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        else :
            print(f"""THÔNG TIN NHÂN VIÊN :
        id : {id}
        Tên : {name}
        Phòng ben công tác : {work_room}
        """)
    

        