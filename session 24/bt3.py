# point_value_vnd là quy định chung của toàn hệ thống.

# Mọi thẻ thành viên đều sử dụng cùng một tỷ giá quy đổi điểm.

# Khi chương trình khuyến mãi thay đổi giá trị điểm, chỉ cần cập nhật một lần bằng Class Method thì tất cả các thẻ sẽ tự động áp dụng tỷ giá mới.

# Nếu khai báo trong init bằng self.point_value_vnd thì mỗi thẻ sẽ có một bản sao riêng và phải cập nhật từng thẻ một.
# @staticmethod?

# Hàm này chỉ kiểm tra định dạng mã thẻ.

# Hàm không sử dụng dữ liệu của đối tượng (self) và cũng không sử dụng dữ liệu của lớp (cls).

# Vì vậy có thể gọi trực tiếp:

# MemberCard.is_valid_card_id("RC01")

# mà không cần tạo đối tượng
# Điểm tích lũy là dữ liệu quan trọng.

# Nếu để public thì người dùng có thể tự ý sửa:

# card.points = 1000

# hoặc

# card.points = -50

# Dùng __points giúp che giấu dữ liệu và chỉ cho phép thay đổi thông qua các hàm nghiệp vụ earn_points() và redeem_points().

class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    def earn_points(self, bill_amount):
        diem_them = bill_amount // 10000

        self.__points += diem_them

        if self.__points >= 100:
            self.__tier = "VIP"

        return diem_them

    def redeem_points(self, points_to_use):
        if points_to_use <= 0:
            return None

        if points_to_use > self.__points:
            return False

        self.__points -= points_to_use

        giam_gia = (points_to_use *MemberCard.point_value_vnd)

        return giam_gia

    @classmethod
    def update_point_value(cls, new_value):
        if new_value > 0:
            cls.point_value_vnd = new_value

    @staticmethod
    def is_valid_card_id(card_id):
        if len(card_id) != 4:
            return False

        if not card_id.startswith("RC"):
            return False

        if not card_id[2:].isdigit():
            return False

        return True


cards_database = []


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card

    return None


card1 = MemberCard("RC01", "Nguyen Van A")
card1.earn_points(1500000)

card2 = MemberCard("RC02", "Tran Thi B")
card2.earn_points(200000)

cards_database.append(card1)
cards_database.append(card2)


while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")

        if len(cards_database) == 0:
            print("Chưa có dữ liệu.")
            continue

        for index, card in enumerate(cards_database, start=1):
            print(
                f"{index}. Mã: {card.card_id} | "
                f"Tên: {card.name} | "
                f"Điểm: {card.points} | "
                f"Hạng: {card.tier}"
            )

    elif choice == "2":
        print("\n--- ĐĂNG KÝ THẺ MỚI ---")

        card_id = input("Nhập mã thẻ: ")

        if find_card(card_id):
            print("\nMã thẻ đã tồn tại trong hệ thống!")
            continue

        if not MemberCard.is_valid_card_id(card_id):
            print("\nMã thẻ không hợp lệ!")
            continue

        name = input("Nhập tên khách hàng: ")

        new_card = MemberCard(card_id, name)

        cards_database.append(new_card)

        print("\nĐăng ký thẻ thành viên thành công!")
        print("Mã thẻ:", new_card.card_id)
        print("Tên khách hàng:", new_card.name)
        print("Điểm ban đầu:", new_card.points)
        print("Hạng thẻ:", new_card.tier)

    elif choice == "3":
        print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")

        card_id = input("Nhập mã thẻ: ")

        card = find_card(card_id)

        if card is None:
            print("Không tìm thấy thẻ!")
            continue

        try:
            bill_amount = int(
                input("Nhập tổng tiền hóa đơn: ")
            )

            if bill_amount <= 0:
                print("Hóa đơn không hợp lệ!")
                continue

            diem_them = card.earn_points(
                bill_amount
            )

            print(f"\nKhách hàng: {card.name}")
            print(f"Hóa đơn: {bill_amount:,} VNĐ")
            print(f"Số điểm được tích: {diem_them}")
            print(f"Tổng điểm hiện tại: {card.points}")

            if card.tier == "VIP":
                print(
                    "\nChúc mừng! Khách hàng đã được nâng hạng lên VIP."
                )

            print(
                f"Hạng thẻ hiện tại: {card.tier}"
            )

        except ValueError:
            print("Dữ liệu không hợp lệ!")

    elif choice == "4":
        print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")

        card_id = input("Nhập mã thẻ: ")

        card = find_card(card_id)

        if card is None:
            print("Không tìm thấy thẻ!")
            continue

        try:
            points_to_use = int(
                input("Nhập số điểm muốn sử dụng: ")
            )

            result = card.redeem_points(
                points_to_use
            )

            if result is False:
                print("\nKhông thể đổi điểm!")
                print(
                    "Số điểm muốn sử dụng vượt quá số điểm hiện có."
                )
                print(
                    f"Điểm hiện tại của khách: {card.points}"
                )
                print(
                    f"Số điểm sau giao dịch: {card.points}"
                )

            elif result is None:
                print("Số điểm không hợp lệ!")

            else:
                print(
                    f"\nĐã trừ {points_to_use} điểm."
                )
                print(
                    f"Khách hàng được giảm giá {result:,} VNĐ vào hóa đơn!"
                )
                print(
                    f"Số điểm còn lại: {card.points}"
                )
                print(
                    f"Hạng thẻ hiện tại: {card.tier}"
                )

        except ValueError:
            print("Dữ liệu không hợp lệ!")

    elif choice == "5":
        print(
            "\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---"
        )

        print(
            f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

        try:
            new_value = int(
                input(
                    "Nhập tỷ giá mới cho 1 điểm: "
                )
            )

            MemberCard.update_point_value(
                new_value
            )

            print(
                "\nCập nhật tỷ giá thành công!"
            )
            print(
                f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
            )

        except ValueError:
            print("Dữ liệu không hợp lệ!")

    elif choice == "6":
        print(
            "\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!"
        )
        break

    else:
        print("Vui lòng chọn từ 1 đến 6.")