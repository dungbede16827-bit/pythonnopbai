def clock_in(attendance_book):
    """
    Chấm công vào
    """

    employee_id = input("Nhập mã nhân viên: ").strip().upper()

    for employee in attendance_book:
        if employee["id"] == employee_id:
            print("Mã nhân viên đã tồn tại!")
            return

    employee_name = input("Nhập tên nhân viên: ").strip()
    clock_in_time = input("Nhập giờ vào : ").strip()

    new_employee = {
        "id": employee_id,
        "name": employee_name,
        "times": (clock_in_time, None)
    }

    attendance_book.append(new_employee)

    print(
        f"Thành công: Đã ghi nhận {employee_id} chấm công vào lúc {clock_in_time}!"
    )


def clock_out(attendance_book):
    """
    Chấm công ra
    """

    employee_id = input("Nhập mã nhân viên: ").strip().upper()

    for employee in attendance_book:

        if employee["id"] == employee_id:

            out_time = input("Nhập giờ ra: ").strip()

            old_clock_in = employee["times"][0]

           
            employee["times"] = (old_clock_in,out_time)

            print("Chấm công ra thành công!")
            return

    print("Không tìm thấy nhân viên!")