# transaction.strip() không trực tiếp thay đổi chuỗi ban đầu vì khi dùng kí tự ngăn cách là "-" 
# mà trong transation khí tự ngăn cách là | nên nay - thành | là hoàn thành 

transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "

transaction.strip()

parts = transaction.split("|")

student_name = parts[0].title()
course_code = parts [1]
amount = parts [2]
status = parts[3].upper()

print( "Học viên:", student_name)
print( "Khóa học:", course_code)
print("So tiên:", amount, "VND")
print("Trạng thái:", status)