
while True : 
    quantity_staff = int(input("Nhập số lượng nhân viên : "))
    for i in range(1,quantity_staff+ 1, 1) :
        print(f"Nhân viên thứ {i}")
        name = input("Tên nhân viên :")
        number_woking = int(input("Số ngày đi làm  "))

        if(number_woking < 20 ) :
            display = "Cần cải thiện chuyên cần "
        else :
            display = "Nhân viên chuyên cần tốt "

        print(f"""THÔNG TIN NHÂN VIÊN :
        Tên : {name}
        Số ngày đi làm : {number_woking}
        {display}  
        """)
    choice = input("tiếp tục chương trình(y/n) :")
    if(choice == 'n') :
        print("CHƯƠNG TRÌNH KẾT THÚC")
        break







    

    