from datetime import datetime


def evaluate_flex_time(attendance_book):
    """
    Đánh giá vi phạm flex-time
    """

    print("\n--- ĐÁNH GIÁ CHẤM CÔNG ---")

    max_time = datetime.strptime("10:00","%H:%M")

    for employee in attendance_book:

        clock_in = employee["times"][0]
        clock_out = employee["times"][1]

        if clock_out is None:
            print(f"{employee['id']} - Chưa hoàn tất chấm công.")
            continue

        in_time = datetime.strptime(clock_in,"%H:%M" )

        out_time = datetime.strptime(clock_out,"%H:%M")

        if in_time > max_time:
            print(
                f"{employee['id']} - Vi phạm: Đến muộn quá 90 phút."
            )
            continue

        work_hours = (out_time - in_time).seconds / 3600

        if work_hours < 9:
            print(
                f"{employee['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ."
            )
        else:
            print(
                f"{employee['id']} - Hợp lệ: Hoàn thành ca làm việc."
            )