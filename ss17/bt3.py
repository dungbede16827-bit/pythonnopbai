teams_list = []
match_schedule = []

def input_teams():

    print("\n--- NHẬP DANH SÁCH ---")

    teams = input(
        "Nhập các đội (cách nhau bởi dấu phẩy): "
    )

    teams = teams.split(",")

    teams_list = []

    for team in teams:

        team = team.strip().upper()

        if team != "" and team not in teams_list:
            teams_list.append(team)

    print(
        f"Đã ghi nhận {len(teams_list)} đội: {teams_list}"
    )

    return teams_list

def create_schedule(teams_list):

    if len(teams_list) < 2:
        print(
            "Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu."
        )
        return []

    match_schedule = []

    matches = itertools.combinations(
        teams_list,
        2
    )

    for match in matches:

        team_a = match[0]
        team_b = match[1]

        match_schedule.append(
            f"{team_a} vs {team_b}"
        )

    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    for index, match in enumerate(
        match_schedule,
        start=1
    ):
        print(f"{index}. {match}")

    print(
        f"Tổng số trận đấu: {len(match_schedule)} trận."
    )

    return match_schedule

def generate_match_ids(match_schedule):

    if len(match_schedule) == 0:
        print(
            "Vui lòng tạo lịch thi đấu trước khi sinh mã ID."
        )
        return

    print("\n--- MÃ TRẬN ĐẤU ---")

    for index, match in enumerate(
        match_schedule,
        start=1
    ):

        team_a, team_b = match.split(" vs ")

        code_a = team_a[:3]

        while len(code_a) < 3:
            code_a += "X"

        code_b = team_b[:3]

        while len(code_b) < 3:
            code_b += "X"

        match_id = (
            f"M{index:02d}-{code_a}-{code_b}"
        )

        print(
            f"Trận {index} ({match}) -> ID: {match_id}"
        )


while True:

    print("""
============= ESPORTS MATCHMAKER =============
1. Nhập danh sách Đội tuyển
2. Tạo lịch thi đấu (Combinations)
3. Tạo mã trận đấu tự động
4. Đóng hệ thống
==============================================
""")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        teams_list = input_teams()

    elif choice == "2":
        match_schedule = create_schedule(
            teams_list
        )

    elif choice == "3":
        generate_match_ids(
            match_schedule
        )

    elif choice == "4":
        print("Đóng hệ thống thành công!")
        break

    else:
        print("Lựa chọn không hợp lệ!")