# Class Attributes (Thuộc tính lớp)

# Dùng chung cho tất cả tài khoản:

# bank_name = "Vietcombank"
# transaction_fee = 2000
# Instance Attributes (Thuộc tính đối tượng)

# Mỗi tài khoản sẽ có:

# self.account_number
# self._account_name
# self.__balance

# Trong đó:

# Thuộc tính	Loại	Mục đích
# account_number	Public	Lưu số tài khoản
# _account_name	Protected	Lưu tên chủ tài khoản
# __balance	Private	Lưu số dư, không cho sửa trực tiếp
# Property
# Chỉ đọc số dư
# @property
# def balance(self):

# Cho phép:

# print(account.balance)

# Không cho phép:

# account.balance = 1000000

# Nhằm đảm bảo tính đóng gói dữ liệu.

# Quản lý tên tài khoản
# @property
# def account_name(self):

# và

# @account_name.setter
# def account_name(self, new_name):

# Chức năng:

# Xóa khoảng trắng dư thừa.
# Chuyển sang chữ in hoa.
# Không cho phép tên rỗng.

# Ví dụ:

# "   nguyen van an   "

# sẽ trở thành:

# "NGUYEN VAN AN"
# Phân biệt Method
# Static Method
# @staticmethod
# def validate_account_number(account_number):

# Lý do dùng @staticmethod:

# Chỉ kiểm tra dữ liệu đầu vào.
# Không sử dụng thuộc tính của class.
# Không sử dụng dữ liệu của object.

# Ví dụ:

# BankAccount.validate_account_number("1234567890")
# Class Method
# @classmethod
# def update_transaction_fee(cls, new_fee):

# Lý do dùng @classmethod:

# Cần cập nhật thuộc tính chung của class.

# Ví dụ:

# BankAccount.update_transaction_fee(5000)

# Sau đó tất cả tài khoản đều dùng phí mới:

# BankAccount.transaction_fee

class BankAccount:

    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, acc_num, acc_name):
        self.acc_num = acc_num
        self._acc_name = ""
        self.acc_name = acc_name
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @property
    def acc_name(self):
        return self._acc_name

    @acc_name.setter
    def acc_name(self, name):
        name = " ".join(name.strip().split())

        if name == "":
            print("Tên tài khoản không được để trống")
            return

        self._acc_name = name.upper()

    @staticmethod
    def validate_account_number(acc_num):
        return acc_num.isdigit() and len(acc_num) == 10

    @classmethod
    def update_transaction_fee(cls, fee):
        cls.transaction_fee = fee

    def deposit(self, money):
        if money <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += money
        return True

    def withdraw(self, money):
        if money <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total = money + BankAccount.transaction_fee

        if self.__balance < total:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False

        self.__balance -= total
        return True


    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print("Ngân hàng:", BankAccount.bank_name)
        print("Số tài khoản:", self.acc_num)
        print("Tên chủ tài khoản:", self.acc_name)
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


acc = None

while True:
    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")
    print("==========================================")

    choice = input("Chọn chức năng (1-6): ")

    # Chức năng 1
    if choice == "1":
        print("\n--- MỞ TÀI KHOẢN MỚI ---")

        while True:
            num = input("Nhập số tài khoản 10 chữ số: ")

            if BankAccount.validate_account_number(num):
                break

            print("Số tài khoản không hợp lệ!")
            print("Số tài khoản phải gồm đúng 10 chữ số.")

        name = input("Nhập tên chủ tài khoản: ")

        acc = BankAccount(num, name)

        print("\nMở tài khoản thành công!")
        print("Số tài khoản:", acc.acc_num)
        print("Tên chủ tài khoản:", acc.acc_name)


    elif choice == "2":
        if acc is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        else:
            acc.display_info()


    elif choice == "3":
        if acc is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        else:
            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            print("1. Nạp tiền")
            print("2. Rút tiền")

            choice2 = input("Chọn loại giao dịch (1-2): ")

            try:
                money = int(input("Nhập số tiền giao dịch: "))
            except ValueError:
                print("Số tiền không hợp lệ")
                continue

            if choice2 == "1":
                if acc.deposit(money):
                    print(f"Nạp tiền thành công: +{money:,} VND")
                    print(f"Số dư mới: {acc.balance:,} VND")

            elif choice2 == "2":
                if acc.withdraw(money):
                    print(f"Rút tiền thành công: -{money:,} VND")
                    print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
                    print(f"Số dư mới: {acc.balance:,} VND")
                else:
                    print(f"Số dư mới: {acc.balance:,} VND")

            else:
                print("Lựa chọn không hợp lệ")

    elif choice == "4":
        if acc is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        else:
            print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")

            name = input("Nhập tên mới: ")

            old = acc.acc_name

            acc.acc_name = name

            if old != acc.acc_name:
                print("Cập nhật thành công.")
                print("Tên mới:", acc.acc_name)

    elif choice == "5":
        print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
        print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")

        try:
            fee = int(input("Nhập phí giao dịch mới: "))

            if fee < 0:
                print("Phí giao dịch không được âm")
                print(f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND")
            else:
                BankAccount.update_transaction_fee(fee)
                print(
                    f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VND"
                )

        except ValueError:
            print("Phí giao dịch không hợp lệ")

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
        break

    else:
        print("Vui lòng chọn từ 1 đến 6")