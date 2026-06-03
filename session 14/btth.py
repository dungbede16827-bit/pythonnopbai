from unicodedata import name


grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades(book) :
    print("BẢNG ĐIỂM HỌC SINH")
    print("Mã SV | Tên SV | Toán | Anh | Trung Bình")
    for i in book :
        print(f' id : {i["id"]} | TEN HOC SINH : {i["name"]} | DIEM TOAN {i["info"][0]} | DIEM TIENG ANH {i["info"][1]} |')
        print(f'DIEM TRUNG BINH {(i["info"][0] + i["info"][1])/2}')
def add_student(book) :
    new_grade_book_new = {}
    while True :
        new_grade_book_new["id"] = input("NHẬP MÃ HỌC SINH : ")
        duplicate = False
        for i in book :
            if i["id"] == new_grade_book_new["id"] :
                print(f"Lỗi: Mã học sinh {new_grade_book_new['id']} đã tồn tại! Vui lòng nhập mã khác. ")
                
                duplicate = True 
                break
            if duplicate :
                continue
            
        
        new_grade_book_new["name"] = input("NHẬP TÊN HỌC SINH : ")
        new_grade_book_new["info"] = (
            float(input("NHẬP ĐIỂM TOÁN : ")),
            float(input("NHẬP ĐIỂM ANH : "))
        )
        book.append(new_grade_book_new)
        print(f"Thành công: Đã thêm học sinh {new_grade_book_new['id']} vào hệ thống!")
        break
def update_scores(book) :
    id_input = input("Nhập mã học sinh cần cập nhật: ").strip().upper()
    for i in book :
        if i["id"] == id_input :
            print(f"Đang cập nhật điểm cho học sinh {i['name']} (Mã: {i['id']})")
            i["info"] = (
                float(input("Nhập điểm Toán mới: ")),
                float(input("Nhập điểm Anh mới: "))
            )
            print(f"Cập nhật thành công cho học sinh {i['name']} (Mã: {i['id']})")
            return
        
    print(f"Lỗi: Không tìm thấy học sinh với mã {id_input}. Vui lòng kiểm tra lại mã và thử lại.")        

def delete_student(book) :
    id_input = input("Nhập mã học sinh cần xóa: ").strip().upper()
    flag = 1
    for i in book :
        if i["id"] == id_input:
            flag = 0 
            book.remove(i)
            print("thong bao thanh cong")
            break
        if flag == 1:
            print("mã không tồn tại")


     

while True :
        print("""

=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
Chọn chức năng (1-5):

""")
        choose = input("NHẬP LỰA CHỌN TỪ 1 -> 5:  ")
        match choose :
            case "5" :
                  print("thoát chương trình !")
                  break
            case "1" :
                display_grades(grade_book)
            case "2" :
                add_student(grade_book)
            case "3" :
                print("CẬP NHẬT ĐIỂM SỐ HỌC SINH")
                update_scores(grade_book)
            case "4" :
                delete_student(grade_book)
            
