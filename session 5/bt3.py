# số lượng phòng học int 
# hàng ghế int 
# số ghế trên mỗi hàng int 

# in sơ đồ ngồi bằng dấu *
# Hoặc hiển thị thông báo lỗi:
# Số lượng phòng học không hợp lệ
# Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này
# Phòng quá lớn. Dừng nhập dữ liệu

# Ý tưởng xử lý
# Dùng vòng lặp ngoài để duyệt từng phòng học.
# Với mỗi phòng:
# Nhập số hàng và số ghế.
# Kiểm tra dữ liệu hợp lệ.
# Nếu hợp lệ:
# Dùng vòng lặp lồng nhau để in dấu *.


room_count = int(input("Nhập số lượng phòng học: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")

else:


    for room in range(1, room_count + 1):

        print(f"\nPhòng học {room}")

        row_count = int(input("Nhập số hàng ghế: "))
        seat_count = int(input("Nhập số ghế mỗi hàng: "))

        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        for row in range(row_count):

            for seat in range(seat_count):
                print("*", end="")

            print()