# lỗi sai là dùng or chỉ cần 1 trong 2 điều kiện đúng là sẽ thực thi được nên chỉ cần lớn hơn 50kg hoặc 16 tuổi là đủ điều kiện
# ở đây ta phải sử dụng and để cả 2 đồng thời đúng
# sự khác nhau giữa or và and là or chỉ cần 1 trong 2 đúng là đúng còn and phải đồng thời cả 2
# sửa lại 

print(" -- BLOOD DONOR SCREENING SYSTEM --- ")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra diều kiện hiến máu
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
 if donor_age < 18 :
    print("Result: NOT ELIGIBLE. Because you are under 18 years old. Thank you for your interest.")
 else :
    print('Result: NOT ELIGIBLE. Because you do not weigh 50kg. Thank you for your interest.')