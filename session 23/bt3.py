from core.logistics import (show_flights)

from core.manager import (add_flight)

from utils.time_helper import (calculate_eta)

from utils.file_helper import (create_folder)

flights = [
    {
        "flight_id": "RA001",
        "passengers": 154,
        "depart_time":
        "2026-06-15 08:00:00",
        "duration_min": 120
    },
    {
        "flight_id": "RA002",
        "passengers": 85,
        "depart_time":
        "2026-06-15 13:30:00",
        "duration_min": 45
    }
]

while True:

    print("""
===== HỆ THỐNG ĐIỀU HÀNH BAY =====

1. Hiển thị chuyến bay
2. Thêm chuyến bay
3. Tính ETA
4. Tạo thư mục log
5. Thoát

=============================
""")

    try:

        choice = int(
            input(
                "Nhập lựa chọn: "
            )
        )

    except ValueError:

        print(
            "Vui lòng nhập từ 1-5"
        )
        continue

    match choice:

        case 1:
            show_flights(flights)

        case 2:
            add_flight(flights)

        case 3:
            calculate_eta(flights)

        case 4:
            create_folder()

        case 5:
            print(
                "Cảm ơn kỹ sư đã sử dụng hệ thống!"
            )
            break

        case _:
            print(
                "Lựa chọn không hợp lệ!"
            )