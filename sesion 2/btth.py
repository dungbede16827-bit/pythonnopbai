from datetime import datetime

name = input("Nhập tên bệnh nhân: ")
if name == "" :
    print ("không được để trống")
    exit()

nam_sinh = int(input("Nhập năm sinh: "))
if nam_sinh < 1900 or nam_sinh > datetime.now().year :
    print ("năm sinh không hợp lệ")

so_ngay_bi_benh = int(input("số ngày bị bênh :"))
if so_ngay_bi_benh <= 0 :
    print(" số ngày bị bệnh không hợp lệ")
    exit()

nhiet_do = float(input("nhập nhiệt độ cơ thể (C)"))
if nhiet_do < 30 or nhiet_do > 45 :
    print("nhiệt độ không hợp lệ")
    exit()
chi_phi = int(input("nhập chi phí khám : "))
if chi_phi < 0 :
    print("chi phí không được nhỏ hơn 0")
    exit()

tuoi_benh_nhan = datetime.now().year - nam_sinh

phu_phi = chi_phi * 0.1 
tong_chi_phi = phu_phi + chi_phi

if nhiet_do > 38 and so_ngay_bi_benh > 3 : 
    result =  print("Nguy hiem")
elif nhiet_do > 38 :
    result = print("sốt cao")
elif nhiet_do > 37.5 :
    result = print("Sốt nhẹ")
else :
    result = print("Bình Thường")


if result == 'Nguy hiểm' :
    if tuoi_benh_nhan > 60 :
        rate = 'Cấp cứu'
    else :
        rate = 'ưu tiên cao'
else :
    rate = 'người bình thường'

tong_phi_danh_gia = "cao" if tong_chi_phi > 500_000 else "Thấp"



print (f"""
Nhập tên bệnh nhân: {name}
Nhập năm sinh: {nam_sinh}
Nhập số ngày bị bệnh: {so_ngay_bi_benh}
Nhập nhiệt độ cơ thể (C): {nhiet_do}
Nhập chi phí khám: {chi_phi}

KẾT QUẢ
Tên: {name}
Tuổi: {tuoi_benh_nhan}
Nhiệt độ: {nhiet_do}  C
Số ngày bệnh: {so_ngay_bi_benh}

Tình trạng: {result}
Mức độ ưu tiên: {rate}

Tổng chi phí: {tong_chi_phi} VND
Mức chi phí: {tong_phi_danh_gia}

 """)







