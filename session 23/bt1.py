# # Khi dùng:

# # from math import *

# # Toàn bộ hàm, hằng số trong thư viện math được đưa vào phạm vi hiện tại.
# Dễ gây xung đột tên

# Khó đọc và bảo trì

# Khi thấy:

# distance = sqrt(x)

# Ta không biết sqrt() đến từ đâu.

# Trong khi:

# import math

# distance = math.sqrt(x)
# thì nguồn gốc hàm rất rõ ràng.
# PEP8 khuyến nghị tránh:

# from module import *

# trừ một số trường hợp đặc biệt.

# Cách import an toàn

# Cách 1 (Khuyến nghị nhất)

# import math

# distance = math.sqrt(25)
# Cách 2
# from math import sqrt, radians, sin, cos
# Chỉ import đúng những gì cần dùng.

from datetime import datetime

from geo_calculator import calculate_distance
from time_estimator import predict_eta
from file_helper import create_log_dir


shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00",
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00",
    },
]


def main():
    print(
        "====== HỆ THỐNG ĐIỀU PHỐI "
        "RIKKEI LOGISTICS ======="
    )

    create_log_dir("logs")

    print(
        "[INFO] Khởi tạo hệ thống lưu trữ "
        "log hành trình... Thành công."
    )

    print("-" * 75)

    for shipment in shipments:

        distance = calculate_distance(
            shipment["from_lat"],
            shipment["from_lon"],
            shipment["to_lat"],
            shipment["to_lon"],
        )

        eta = predict_eta(
            shipment["depart"],
            distance
        )

        deadline = datetime.strptime(
            shipment["deadline"],
            "%Y-%m-%d %H:%M:%S"
        )

        print(
            f"\n[CHUYẾN XE {shipment['id']}]"
        )

        print(
            f" + Khoảng cách vận chuyển: "
            f"{distance:.2f} km"
        )

        print(
            f" + Thời gian khởi hành: "
            f"{shipment['depart']}"
        )

        print(
            f" + Dự kiến cập bến (ETA): "
            f"{eta.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        if eta <= deadline:
            print(
                " + Trạng thái: "
                " AN TOÀN "
                "(Kịp tiến độ trước deadline)"
            )
        else:
            print(
                f" + Trạng thái: "
                f" CẢNH BÁO "
                f"(Trễ hạn! Deadline yêu cầu lúc "
                f"{deadline.strftime('%H:%M:%S')})"
            )

    print("=" * 56)


if __name__ == "__main__":
    main()