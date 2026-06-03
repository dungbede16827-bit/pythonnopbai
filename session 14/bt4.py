student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def calculate_average(student):
    return (
        student["math"]
        + student["physics"]
        + student["chemistry"]
    ) / 3


def display_grades(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        avg = calculate_average(student)

        if avg >= 8:
            rank = "Giỏi"

        elif avg >= 6.5:
            rank = "Khá"

        elif avg >= 5:
            rank = "Trung bình"

        else:
            rank = "Yếu"

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {avg:.2f} - {rank}"
        )

    print("---------------------------")


def update_student_score(records):

    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    found_student = None

    for student in records:

        if student["student_id"] == student_id:
            found_student = student
            break

    if found_student is None:

        print(
            f"Không tìm thấy sinh viên mang mã "
            f"{student_id} trong hệ thống!"
        )
        return

    subject_choice = input(
        "Chọn môn học (1-Toán, 2-Lý, 3-Hóa): "
    ).strip()

    subjects = {
        "1":"math",
        "2":"physics",
        "3":"chemistry"
    }

    subject_names = {
        "1":"Toán",
        "2":"Lý",
        "3":"Hóa"
    }

    if subject_choice not in subjects:

        print("Lựa chọn môn không hợp lệ!")
        return

    while True:

        new_score = input(
            "Nhập điểm mới: "
        ).strip()

        check_score = new_score.replace(".","",1)

        if not check_score.isdigit():

            print(
                "Điểm số phải là số!"
            )
            continue

        new_score = float(new_score)

        if new_score < 0 or new_score > 10:

            print(
                "Điểm số không hợp lệ. "
                "Vui lòng nhập từ 0 đến 10!"
            )
            continue

        break

    subject_key = subjects[subject_choice]

    found_student[subject_key] = new_score

    print(
        f">> Đã cập nhật điểm "
        f"{subject_names[subject_choice]} "
        f"của sinh viên "
        f"'{found_student['name']}' "
        f"thành {new_score}."
    )

    


def generate_report(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)

    pass_count = 0
    fail_count = 0

    for student in records:

        avg = calculate_average(student)

        if avg >= 5:
            pass_count += 1
        else:
            fail_count += 1

    pass_percent = (pass_count / total) * 100
    fail_percent = (fail_count / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")

    print(f"Tổng số sinh viên: {total}")

    print(
        f"Số lượng qua môn "
        f"(ĐTB >= 5.0): "
        f"{pass_count} sinh viên "
        f"(Chiếm {pass_percent:.2f}%)"
    )

    print(
        f"Số lượng trượt "
        f"(ĐTB < 5.0): "
        f"{fail_count} sinh viên "
        f"(Chiếm {fail_percent:.2f}%)"
    )

    print("----------------------")


def find_valedictorian(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]

    max_avg = calculate_average(
        top_student
    )

    for student in records:

        avg = calculate_average(student)

        if avg > max_avg:

            max_avg = avg
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")

    print(
        f"Sinh viên: "
        f"{top_student['name']} "
        f"(Mã: {top_student['student_id']})"
    )

    print(
        f"Điểm Trung Bình: "
        f"{max_avg:.2f}"
    )

    print(
        "Chúc mừng sinh viên đã đạt "
        "thành tích xuất sắc nhất khóa!"
    )

    print("--------------------------")


def main():

    while True:

        print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====
1. Xem bảng điểm và học lực
2. Cập nhật điểm thi sinh viên
3. Báo cáo thống kê (Đỗ/Trượt)
4. Tìm sinh viên Thủ khoa
5. Thoát chương trình
======================================================
""")

        choice = input(
            "Chọn chức năng (1-5): "
        ).strip()

        if choice == "1":

            display_grades(student_records)

        elif choice == "2":

            update_student_score(student_records)

        elif choice == "3":

            generate_report(student_records)

        elif choice == "4":

            find_valedictorian(student_records)

        elif choice == "5":

            print(
                "Cảm ơn bạn đã sử dụng hệ thống!"
            )
            break

        else:

            print(
                "Lựa chọn không hợp lệ!"
            )


main()