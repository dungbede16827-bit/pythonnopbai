import random

patient_name = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính: ")
birth_year = int(input("Nhập năm sinh: "))
phone_number = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng ban đầu: ")
medical_fee = float(input("Nhập chi phí khám: "))

random_number = random.randint(100, 999)
patient_id = f"BN{birth_year}{random_number}"
print(f"""
 THẺ BỆNH NHÂN 

Mã BN        : {patient_id}

Tên          : {patient_name} ({type(patient_name)})
Giới tính    : {gender} ({type(gender)})
Năm sinh     : {birth_year} ({type(birth_year)})
Điện thoại   : {phone_number} ({type(phone_number)})
Email        : {email} ({type(email)})
Triệu chứng  : {symptom} ({type(symptom)})
Chi phí      : {medical_fee} VND ({type(medical_fee)})

""")