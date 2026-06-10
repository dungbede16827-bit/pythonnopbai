# Tên cũ:

# ds
# p
# l

# Tên mới:

# roster_list
# player
# salary
# player_id
# player_status

# Giúp code dễ đọc và tự mô tả ý nghĩa (Self-documenting Code).

# Mỗi hàm chỉ thực hiện một nhiệm vụ:

# display_roster()
# sign_player()
# update_player_status()
# generate_payroll_report()
# calculate_actual_pay()
# find_player_by_id()

# Không viết một hàm xử lý toàn bộ hệ thống.
# Sử dụng:

# try:
# except ValueError:
# except KeyError:

# để chương trình không bị crash.
# Tách logic tính lương:

# calculate_actual_pay()

# để tránh viết lại nhiều lần.
import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]


def find_player_by_id(roster_list, player_id):
    """
    Find player by ID.
    """
    for player in roster_list:
        if player["player_id"] == player_id:
            return player
    return None


def calculate_actual_pay(player):
    """
    Calculate actual monthly salary.
    """

    if player["status"] == "Benched":
        return player["salary"] * 0.5

    return player["salary"]


def display_roster(roster_list):
    """
    Display roster.
    """

    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")

    print(
        f"{'ID':<8} | "
        f"{'Tên tuyển thủ':<20} | "
        f"{'Vị trí':<15} | "
        f"{'Lương':<12} | "
        f"Trạng thái"
    )

    print("-" * 80)

    for player in roster_list:

        try:
            status = player["status"]

        except KeyError:
            status = "Unknown"

        name = player["name"]

        if status == "Benched":
            name += " [DỰ BỊ]"

        print(
            f"{player['player_id']:<8} | "
            f"{name:<20} | "
            f"{player['role']:<15} | "
            f"{player['salary']:<12,.1f} | "
            f"{status}"
        )

    logging.info(
        "Coach viewed the team roster."
    )


def sign_player(roster_list):
    """
    Sign new player.
    """

    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    if find_player_by_id(
        roster_list,
        player_id
    ):
        print(
            f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại."
        )

        logging.warning(
            f"Failed to sign player - Duplicate player ID {player_id}"
        )

        return

    name = input(
        "Nhập tên tuyển thủ: "
    ).strip().title()

    role = input(
        "Nhập vị trí thi đấu: "
    ).strip().title()

    while True:

        try:
            salary = float(
                input(
                    "Nhập mức lương hàng tháng: "
                )
            )

            if salary <= 0:
                print(
                    "Lương phải là số dương. Vui lòng nhập lại."
                )
                continue

            break

        except ValueError:

            print(
                "Lương phải là số. Vui lòng nhập lại."
            )

            logging.warning(
                "Failed to sign player - Invalid salary input"
            )

    roster_list.append(
        {
            "player_id": player_id,
            "name": name,
            "role": role,
            "salary": salary,
            "status": "Active"
        }
    )

    print(
        f"Thành công: Đã chiêu mộ tuyển thủ {name}."
    )

    logging.info(
        f"Signed new player {name} with salary {salary}"
    )


def update_player_status(roster_list):
    """
    Update player salary or status.
    """

    player_id = input(
        "Nhập mã tuyển thủ cần cập nhật: "
    ).strip().upper()

    player = find_player_by_id(
        roster_list,
        player_id
    )

    if not player:

        print(
            f"Không tìm thấy tuyển thủ mang mã {player_id}."
        )

        logging.warning(
            f"Failed to update player - Player ID {player_id} not found"
        )

        return

    print("\n1. Cập nhật lương")
    print("2. Cập nhật trạng thái")

    choice = input(
        "Chọn chức năng cập nhật: "
    )

    if choice == "1":

        while True:

            try:
                new_salary = float(
                    input(
                        "Nhập mức lương mới: "
                    )
                )

                if new_salary <= 0:
                    print(
                        "Lương phải là số dương."
                    )
                    continue

                old_salary = player["salary"]

                player["salary"] = new_salary

                logging.info(
                    f"Updated player {player_id} salary from "
                    f"{old_salary} to {new_salary}"
                )

                print(
                    f"Thành công: Đã cập nhật lương cho tuyển thủ {player_id}."
                )

                break

            except ValueError:

                print(
                    "Lương phải là số."
                )

    elif choice == "2":

        print("1. Active")
        print("2. Benched")

        status_choice = input(
            "Nhập lựa chọn: "
        )

        player["status"] = (
            "Active"
            if status_choice == "1"
            else "Benched"
        )

        logging.info(
            f"Updated player {player_id} status to {player['status']}"
        )

        print(
            f"Thành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}."
        )


def generate_payroll_report(roster_list):
    """
    Generate payroll report.
    """

    print(
        "\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---"
    )

    if not roster_list:
        print(
            "Đội hình hiện đang trống. Tổng quỹ lương: 0.0"
        )
        return

    total = 0

    try:

        for player in roster_list:

            actual_salary = calculate_actual_pay(
                player
            )

            total += actual_salary

        print(
            f"Tổng quỹ lương hàng tháng: {total}"
        )

        logging.info(
            f"Generated monthly payroll report. Total: {total}"
        )

    except KeyError as error:

        print(
            "Lỗi: Một tuyển thủ đang bị thiếu dữ liệu."
        )

        logging.error(
            f"Missing key while generating payroll report: {error}"
        )