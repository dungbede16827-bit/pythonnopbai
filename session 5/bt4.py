# người dùng nhập chi nhánh int 
# số học viên đi học của từng lớp int 
# mỗi chi nhánh cố định 2 lớp
# Hệ thống hiển thị trạng thái của từng lớp:

# Lớp học ổn định
# Lớp cần được nhắc nhở theo dõi
# Hoặc các thông báo lỗi:
# Số học viên không hợp lệ. Vui lòng nhập lại.
# Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.
# Ý tưởng xử lý
# Dùng vòng lặp ngoài để duyệt từng chi nhánh.
# Dùng vòng lặp trong để duyệt 2 lớp của mỗi chi nhánh.
# Với mỗi lớp:
# Nhập số học viên.
# Nếu số âm  bắt nhập lại.
# Nếu bằng 0 bỏ qua đánh giá.
# Nếu >= 20 lớp ổn định.
# Nếu < 20  cần nhắc nhở.


branch_count = int(input("Nhập số lượng chi nhánh: "))

class_count = 2


for branch in range(1, branch_count + 1):

    print(f"\nChi nhánh {branch}:")

   
    for classroom in range(1, class_count + 1):

    
        while True:

            student_count = int(
                input(
                    f"Nhập số học viên đi học của lớp {classroom}: "
                )
            )

    
            if student_count < 0:
                print(
                    "Số học viên không hợp lệ. Vui lòng nhập lại."
                )

            else:
                break

    
        if student_count == 0:
            print(
                "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
            )
            continue

        if student_count >= 20:

            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                f"Lớp học ổn định"
            )

        else:

            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                f"Lớp cần được nhắc nhở theo dõi"
            )