# Thiết kế luồng chương trình
# Mô tả các bước chương trình hoạt động:
# Chào bệnh nhân
# Yêu cầu nhập thông tin
# Ép kiểu dữ liệu int, float
# Kiểm tra dữ liệu
# In phiếu khám
# In log hệ thống 

hospital_name = "Bệnh viện Đa khoa Sức Khỏe Vàng"

print("KIOSK KHAI BÁO Y TẾ TỰ PHỤC VỤ")

patient_name = input("Nhập họ và tên bệnh nhân : ")
patient_id = input("Nhập mã bệnh nhân : ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))
body_temperature = float(input("Nhập nhiệt độ cơ thể : "))
heart_rate = int(input("Nhập nhịp tim : "))
body_weight = float(input("Nhập cân nặng (Ví dụ: 65.5): "))

print(f"""
PHIẾU KHÁM BỆNH ĐIỆN TỬ 
Tên bệnh viện : {hospital_name}
Mã bệnh nhân  : {patient_id}
Họ và tên     : {patient_name}
Tuổi          : {patient_age}
Nhiệt độ      : {body_temperature} C
Nhịp tim      : {heart_rate} nhịp/phút
Cân nặng      : {body_weight} kg
Trạng thái    : Dữ liệu hợp lệ
""")

print(f"""
Kiểm tra kiểu dữ liệu sau khi chuẩn hóa 
patient_name    {type(patient_name)}
patient_id      {type(patient_id)}
patient_age      {type(patient_age)}
body_temperature  {type(body_temperature)}
heart_rate       {type(heart_rate)}
body_weight      {type(body_weight)}

""")