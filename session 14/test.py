# # khai báo hàm : Từ khóa def
# # Tham số 
# def hello_hieu(name) :
#     print(f"xin chào {name} bé bỏng ")

# hello_hieu("Dương")
# hello_hieu("Phong")
# hello_hieu("Hiếu")
# hello_hieu("Dũng")

# # tạo một hàm tính tổng 2 số bất kỳ mà người dùng nhập

# def sum_member(a,b=1) :
#     sum = a + b 
#     print(f" TỔng của a và b là {sum}")

# sum_member(5,6)
# sum_member(1)
# sum_member(1,12)

# def info_user(name,address) :
#     print(f"Tôn tên là {name} , Quê tôi : {address}")

# info_user(address="Hà Lội" , name="Tuấn")

# def calc_point(a,b,c,d,*danh_sach_diem) :
#     sum = a + b + c + d
#     print
# calc_point(10,1,0,1)

# list_number = [1,2,3,4,5]

# def filter_number(list) :
#     new_list = []
#     for value in list :
#         if value % 2 == 1 :
#             new_list.append(value)
#     return new_list        
    

# print(filter_number(list_number))

# number_01 = "Tuấn"
# # khi gọi chương trình thì biến number_01 sẽ tự tăng 1 giá trị

# def handle_increment() :
#     global number_01
#     number_01 = "An"
    

# handle_increment()
# print(number_01)


# Bài 1 - Hàm tính BMI 

def tinh_bmi(can_nang,chieu_cao) :
    bmi = (can_nang / chieu_cao** 2)
    print(f"Cân nặng {can_nang} , chieu cao {chieu_cao}")
    print(f"BMI : {bmi}") 
    return bmi 
    
tinh_bmi(57,170)

def phan_loai_hoc_luc(*diem_so) :
    diem_tong = 0
    for point in diem_so :
        diem_tong += point
    xeploai = diem_tong / len(diem_so)

    if xeploai >= 9 :
        print("Xuất sắc")
    elif xeploai >= 8 :
        print("giỏi")
    elif xeploai >= 6.5 :
        print("Khá")
    elif xeploai > 5 :
        print("trung bình")
    else :
        print("yếu")

phan_loai_hoc_luc(7,5,8,9,7,8)









