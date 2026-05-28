order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print(""" \n 
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình

""")
    choice = int(input("Mời bạn chọn chức năng : _"))

    match choice:
        case 1: 
            if len(order_list) == 0 :
                print("danh sách không có dữ liệu ")
            else :
                for index,value in enumerate(order_list,start=0) :
                    print(f" {index}:{value} ")
        case 2:
            while True :
                print("""
                ----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
                1. Thêm đơn hàng mới
                2. Sửa đơn hàng theo vị trí
                3. Xóa đơn hàng theo vị trí
                4. Quay lại menu chính
""")
                choose = int(input("chọn chức năng để cập nhật"))

                if choose == 1 :
                     order_code = input(  "Nhập mã đơn hàng: " ).strip().upper()
                     status = input("nhập trạng thái : ").strip().upper()
                     new_order = f"{order_code}  - {status}"
                     order_list.append(new_order)
                     print("đã thêm đơn hàng thành công")
                elif choose == 2 :
                    input_index = input("Nhập vị trí cần sửa: ").strip()
                    if not input_index.isdigit():
                        print("Vị trí không hợp lệ!")
                        continue
                    input_index = int(input_index)
                    if  input_index < 1 or input_index > len(order_list) :
                        print("Không tồn tại đơn hàng ở vị trí này !")
                        continue
                    order_code = input("nhập mã đơn hàng mới :").strip().upper()
                    status = input("Nhập trạng thái mới :").strip().upper()

                    update_order = f"{order_code} - {status}"
                    order_list[input_index - 1 ] = update_order
                    print("cập nhật thành công !")
                elif choose ==  3:
                    input_index = input("Nhập vị trí cần sửa: ").strip()
                    if not input_index.isdigit():
                        print("Không được nhập chữ !")
                        continue
                    input_index = int(input_index)
                    if  input_index < 1 or input_index > len(order_list) :
                        print("Không tồn tại đơn hàng ở vị trí này !")
                        continue
                    delete_order = order_list.pop(input_index - 1)

                    print(f"đã xóa {delete_order} ")
                elif choose == 4:
                    break
                else :
                    print("lựa chọn không hợp lệ , vui lòng nhập lại !")
                
            
        case 3:
            pending = 0 
            delivering = 0
            completed = 0
            cancelled = 0

            for order in order_list:
                parts = order.split("-")
                status = parts[1].strip()

                if status == "PENDING":
                    pending += 1
                elif status == "DELIVERING":
                     delivering += 1

                elif status == "COMPLETED":
                  completed += 1
                elif status == "CANCELLED":
                    cancelled += 1
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")

            print(f"PENDING: {pending}")
            print(f"DELIVERING: {delivering}")
            print(f"COMPLETED: {completed}")
            print(f"CANCELLED: {cancelled}")
            print(f"Tổng số đơn hàng: {len(order_list)}")        
        case 4:
            print("Bạn đã thoát chương trình ! ")
            break
        case _:
            print("nhập chức năng không đúng vui lòng nhập lại")