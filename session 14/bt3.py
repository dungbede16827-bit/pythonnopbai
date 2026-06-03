from xxlimited import new


students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def display_students(student_list) :
    for i in student_list :
        print(f" Mã : {i["student_id"]} | Tên : {i["name"]} | Toán : {i["math_score"]} | Anh : {i["english_score"]}")

def validate(score) :
    if not score.isdigit():
        return False 
    if float(score) < 0 or float(score) > 10 :
        return False
    return True 
def find_student_by_id(id,list_student) :
    for i in list_student:
        if id == i["student_id"] :
            return True 
    return False

def update_score(student_list): 
    while True:
        ma=input("nhap ma hoc vien: ")
        flag=find_student_by_id(ma, student_list)
        if flag is None:
            print("ma hoc sinh ko ton tai yeu cau nhap lai:")
            continue

        else:

            while True:

                new_math=input("nhap diem toan: ")
                if validate(new_math) == False:
                    print("yeu cau nhap lai")
                    continue
                new_eng=input("nhap diem tieng anh: ")
                if validate(new_eng) == False:
                    print("yeu cau nhap lai")
                    continue

                flag["math_score"] = float(new_math)
                flag["english_score"] = float(new_eng)
                print(f"cap nhat diem thanh cong cho hoc sinh {flag['name']} (Ma: {flag['student_id']})")
                break
        break




def add_student(student_list) :
    ma = input("Nhập mã hs : ").strip().upper()
    flag = 1
    for i in students :
        if find_student_by_id(ma,student_list) == True:
            flag = 1
            break
    if flag == 0 :
        name_new = input("NHAP TEN NV MOI :")
        while True :
            match_new = input("Nhap diem toan : ")
            if validate(match_new) == False :
                continue
            new_eng = input("nhap diem tieng anh : ")
            if validate(new_eng) == False :
                continue

            student_list.append( {
                "student_id": ma,
                "name": name_new,
                "math_score": float(match_new),
                "english_score": float(new_eng)
            })
            print(f"Thêm học sinh {name_new} thành công !")
            break
    else :
        print(f"Ma {ma} da ton tai ! Vui long nhap ma khac !")

def evaluate_students(student_list) :
        for i in student_list :
            average_score = (i["math_score"] + i["english_score"]) / 2
            if average_score >= 9 :
                print(f"Học sinh {i['name']} có học lực Xuất Sắc")
            elif average_score >= 8 :
                print(f"Học sinh {i['name']} có học lực Giỏi")
            elif average_score >= 6.5 :
                print(f"Học sinh {i['name']} có học lực Khá")
            elif average_score >= 5 :
                print(f"Học sinh {i['name']} có học lực Trung Bình")
            else :
                print(f"Học sinh {i['name']} có học lực Yếu")


while True :
    choice = int(input("""
                       
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
1. Hiển thị danh sách học viên
2. Thêm học viên mới
3. Cập nhật điểm thi theo mã học viên
4. Đánh giá học lực của toàn bộ học viên
5. Thoát chương trình
                       
MỜI BẠN NHẬP LỰA CHỌN TỪ 1-5

"""))
    match choice :
        case 5:
            print("Thoát Chương Trình ! ")
            break
        case 1:
            display_students(students)
        case 2:
            add_student(students)
        case 3:
            print("CẬP NHẬT ĐIỂM THI THEO MÃ HỌC VIÊN")
            update_score(students)
        case 4:
            print("ĐÁNH GIÁ HỌC LỰC CỦA TOÀN BỘ HỌC VIÊN")
            evaluate_students(students)



