quantity = int(input("Nhập số lượng sinh viên : "))

for i in range(quantity):

    name = input("Nhập tên nhân viên : ")
    days = int(input("Nhập số ngày làm : "))

    if days < 0 or days > 22:
        print("Dữ liệu không hợp lệ")
        continue


    insao = ""

    for j in range(days):
        insao += "* "

  
    if days == 0:
        status = "Nhân viên nghỉ toàn bộ tháng"
    elif days >= 18:
        status = "Làm việc chăm chỉ"
    elif days < 10:
        status = "Làm việc ít"
    else:
        status = "Làm việc bình thường"

    print(f"""
Nhập số lượng nhân viên: {quantity}

Nhập tên nhân viên: {name}
Nhập số ngày làm: {days}

{name}: {insao}

{status}
""")