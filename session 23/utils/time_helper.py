from datetime import (datetime,timedelta)


def calculate_eta(flights):

    print(
        "\n----- TÍNH ETA -----"
    )

    flight_id = input("Nhập mã chuyến bay: ").strip().upper()

    for flight in flights:

        if flight["flight_id"] == flight_id:

            depart_time = (
                datetime.strptime(
                    flight["depart_time"],
                    "%Y-%m-%d %H:%M:%S"
                )
            )

            eta = (
                depart_time
                + timedelta(
                    minutes=flight[
                        "duration_min"
                    ]
                )
            )

            print(
                f"Giờ cất cánh: "
                f"{flight['depart_time']}"
            )

            print(f"ETA: {eta}")

            return

    print("Không tìm thấy chuyến bay!")