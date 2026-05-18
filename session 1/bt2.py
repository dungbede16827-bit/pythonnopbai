# dữ liệu khi truyền vào của input mặc định là string nên khi nhập lúc nào cũng là string
# muốn kh là string nữa thì phải ép kiểu int vào trc input 
# input là hàm nhận dữ liệu đầu vào từ người dùng dữ liệu người dùng nhập vào dù là số hay kí tự bất kỳ thứ gì 
# từ input đều là string 

print (" --- HỆ THỐNG NHẬP CHI SỐ SINH TON --- ")
name_patient = input ("Nhập tên bệnh nhân : ")
weight = float(input ("Nhập cân nặng bệnh nhân : "))

print (" --- KIỂM TRA DỮ LIỆU LƯU TRỮ --- ")
print ("Bệnh nhân : ", name_patient)
print ("Cân nặng dã nhập : " , weight)

# Trường nhóm IT viết thêm dòng này dể kiểm tra dữ Liệu của cân nặng
print ("CẢNH BÁO - Kiểu dữ liệu dang lưu là : ", type(weight))