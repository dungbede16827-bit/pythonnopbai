students = []

def tinh_tb(toan, ly, hoa):
    return round((toan + ly + hoa) / 3,2)

def xep_loai(tb):
    if tb < 5:
        return "Yeu"
    elif tb < 7:
        return "Trung Binh"
    elif tb < 8:
        return "Kha"
    else:
        return "Gioi"

while True:

    print("""
===== QUAN LY SINH VIEN =====

1. Hien thi danh sach
2. Them sinh vien
3. Cap nhat sinh vien
4. Xoa sinh vien
5. Tim kiem sinh vien
6. Sap xep danh sach
7. Thong ke hoc luc
8. Diem cao nhat / thap nhat
9. Thoat
""")

    choice = input("Nhap lua chon: ")

    # 1
    if choice == "1":

        for sv in students:
            print(sv)

    # 2
    elif choice == "2":

        id = input("Nhap ma SV: ")
        ten = input("Nhap ten: ")

        toan = float(input("Nhap diem Toan: "))
        ly = float(input("Nhap diem Ly: "))
        hoa = float(input("Nhap diem Hoa: "))

        tb = tinh_tb(toan,ly,hoa)
        loai = xep_loai(tb)

        sv = {
            "id":id,
            "ten":ten,
            "diem_toan":toan,
            "diem_ly":ly,
            "diem_hoa":hoa,
            "diem_tb":tb,
            "xep_loai":loai
        }

        students.append(sv)

        print("Them thanh cong!")

    # 3
    elif choice == "3":

        ma = input("Nhap ma can sua: ")

        for sv in students:

            if sv["id"] == ma:

                sv["diem_toan"] = float(input("Toan moi: "))
                sv["diem_ly"] = float(input("Ly moi: "))
                sv["diem_hoa"] = float(input("Hoa moi: "))

                sv["diem_tb"] = tinh_tb(
                    sv["diem_toan"],
                    sv["diem_ly"],
                    sv["diem_hoa"]
                )

                sv["xep_loai"] = xep_loai(sv["diem_tb"])

                print("Cap nhat thanh cong!")

    # 4
    elif choice == "4":

        ma = input("Nhap ma can xoa: ")

        for sv in students:

            if sv["id"] == ma:
                students.remove(sv)
                print("Da xoa!")

    # 5
    elif choice == "5":

        key = input("Nhap ten hoac ma: ").lower()

        for sv in students:

            if key in sv["ten"].lower() or key in sv["id"].lower():
                print(sv)

    # 6
    elif choice == "6":

        students.sort(
            key=lambda x:x["diem_tb"],
            reverse=True
        )

        print("Da sap xep!")

    # 7
    elif choice == "7":

        gioi = 0
        kha = 0
        tb = 0
        yeu = 0

        for sv in students:

            if sv["xep_loai"] == "Gioi":
                gioi +=1

            elif sv["xep_loai"] == "Kha":
                kha +=1

            elif sv["xep_loai"] == "Trung Binh":
                tb +=1

            else:
                yeu +=1

        print("Gioi:",gioi)
        print("Kha:",kha)
        print("TB:",tb)
        print("Yeu:",yeu)

    # 8
    elif choice == "8":

        if len(students)>0:

            max_sv = max(students,key=lambda x:x["diem_tb"])
            min_sv = min(students,key=lambda x:x["diem_tb"])

            print("Cao nhat:",max_sv)
            print("Thap nhat:",min_sv)

    # 9
    elif choice == "9":
        print("Thoat chuong trinh")
        break

    else:
        print("Lua chon khong hop le!")