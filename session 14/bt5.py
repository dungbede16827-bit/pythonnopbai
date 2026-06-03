student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]


def find_student(records, student_id):

    student_id = student_id.strip().upper()

    for index, student in enumerate(records):

        if student["student_id"] == student_id:
            return index

    return -1


def display_statements(records):

    print("\n------ SAO KÊ ĐIỂM SỐ ------")

    for index, student in enumerate(records, start=1):

        current = student["current_points"]

        if current < 500:
            status = "Cần tích lũy thêm"

        elif current <= 1500:
            status = "Thành viên tiềm năng"

        else:
            status = "Thành viên ưu tú"

        print(
            f"{index}. "
            f"Mã:{student['student_id']} | "
            f"Tên:{student['name']} | "
            f"Hiện có:{student['current_points']} | "
            f"Đã tiêu:{student['spent_points']} | "
            f"Hoàn trả:{student['refunded_points']} | "
            f"Hệ số:x{student['multiplier']} | "
            f"Trạng thái:{status}"
        )

    print("-----------------------------")


def redeem_rewards(records):

    student_id = input(
        "Nhập mã học viên đổi quà: "
    )

    index = find_student(records, student_id)

    if index == -1:

        print(
            "Không tìm thấy hồ sơ học viên!"
        )
        return

    spend = input(
        "Nhập số điểm cần tiêu: "
    ).strip()

    if not spend.isdigit():

        print(
            "Vui lòng nhập số nguyên dương!"
        )
        return

    spend = int(spend)

    if spend <= 0:

        print(
            "Vui lòng nhập số nguyên dương!"
        )
        return

    if spend > records[index]["current_points"]:

        print(
            "Số dư điểm không đủ để thực hiện giao dịch!"
        )
        return

    records[index]["current_points"] -= spend
    records[index]["spent_points"] += spend

    print(
        f">> Giao dịch thành công! "
        f"'{records[index]['name']}' "
        f"đã tiêu {spend} điểm. "
        f"Số dư còn lại: "
        f"{records[index]['current_points']} điểm."
    )


def appeal_score(records):

    student_id = input(
        "Nhập mã học viên cần phúc khảo: "
    )

    index = find_student(records, student_id)

    if index == -1:

        print(
            "Không tìm thấy hồ sơ học viên!"
        )
        return

    refund = input(
        "Nhập số điểm hoàn lại: "
    ).strip()

    if not refund.isdigit():

        print(
            "Vui lòng nhập số nguyên dương!"
        )
        return

    refund = int(refund)

    if refund <= 0:

        print(
            "Vui lòng nhập số nguyên dương!"
        )
        return

    if refund > records[index]["spent_points"]:

        print(
            "Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!"
        )
        return

    records[index]["spent_points"] -= refund
    records[index]["current_points"] += refund
    records[index]["refunded_points"] += refund

    print(
        f">> Hoàn điểm thành công! "
        f"'{records[index]['name']}' "
        f"được cộng lại {refund} điểm."
    )


def activate_multiplier(records):

    student_id = input(
        "Nhập mã học viên nhận hệ số: "
    )

    index = find_student(records, student_id)

    if index == -1:

        print(
            "Không tìm thấy hồ sơ học viên!"
        )
        return

    multiplier = input(
        "Nhập hệ số nhân mới (1.0 - 3.0): "
    ).strip()

    check = multiplier.replace(".", "", 1)

    if not check.isdigit():

        print(
            "Hệ số nhân không hợp lệ. "
            "Chỉ chấp nhận số từ 1.0 đến 3.0"
        )
        return

    multiplier = float(multiplier)

    if multiplier < 1.0 or multiplier > 3.0:

        print(
            "Hệ số nhân không hợp lệ. "
            "Chỉ chấp nhận số từ 1.0 đến 3.0"
        )
        return

    records[index]["multiplier"] = multiplier

    print(
        f">> Đã kích hoạt hệ số "
        f"x{multiplier} "
        f"cho học viên "
        f"'{records[index]['name']}'."
    )


def grade_assignment(records):

    student_id = input(
        "Nhập mã học viên vừa nộp bài: "
    )

    index = find_student(records, student_id)

    if index == -1:

        print(
            "Không tìm thấy hồ sơ học viên!"
        )
        return

    score = input(
        "Nhập số điểm gốc đạt được: "
    ).strip()

    check = score.replace(".", "", 1)

    if not check.isdigit():

        print(
            "Vui lòng nhập số hợp lệ!"
        )
        return

    score = float(score)

    if score <= 0:

        print(
            "Vui lòng nhập số nguyên dương!"
        )
        return

    multiplier = records[index]["multiplier"]

    real_score = score * multiplier

    records[index]["current_points"] += real_score

    print(
        f">> Hệ số hiện tại của "
        f"'{records[index]['name']}' "
        f"là x{multiplier}."
    )

    print(
        f">> Điểm thực nhận: "
        f"{real_score}"
    )

    print(
        f">> Đã cộng "
        f"{real_score} điểm "
        f"vào tài khoản!"
    )


def main():

    while True:

        print("""
===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====
1. Hiển thị sao kê điểm số
2. Đổi điểm lấy phần thưởng
3. Phúc khảo bài thi
4. Kích hoạt hệ số nhân điểm
5. Chấm bài
6. Thoát chương trình
=====================================================
""")

        choice = input(
            "Chọn chức năng (1-6): "
        ).strip()

        if choice == "1":

            display_statements(
                student_records
            )

        elif choice == "2":

            redeem_rewards(
                student_records
            )

        elif choice == "3":

            appeal_score(
                student_records
            )

        elif choice == "4":

            activate_multiplier(
                student_records
            )

        elif choice == "5":

            grade_assignment(
                student_records
            )

        elif choice == "6":

            print(
                "Cảm ơn bạn đã sử dụng hệ thống!"
            )
            break

        else:

            print(
                "Lựa chọn không hợp lệ!"
            )


main()