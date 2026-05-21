# bởi vì total_students đang cộng dồn tất cả chi nhánh.
# Ví dụ:
# Chi nhánh 1 = 50 học viên
# Chi nhánh 2 = 40 học viên
# thì chi nhánh 2 sẽ in thành 90
# Muốn đúng thì phải reset về 0 cho mỗi chi nhánh:

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):

    total_students = 0

    print(f"\nChi nhánh {branch}")

    for classroom in range(1, class_count + 1):

        student_count = int(
            input(f"Nhập số học viên lớp {classroom}: ")
        )

        total_students += student_count

    print(f"Chi nhánh {branch}: {total_students} học viên")