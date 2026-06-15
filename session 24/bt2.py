# Nếu để points là thuộc tính public:

# card1.points = -50
# card1.points = "mot tram"

# thì dữ liệu sẽ bị sai lệch.

# Hậu quả:

# Điểm tích lũy có thể bị âm.
# Điểm có thể bị gán thành chuỗi ký tự.
# Các phép cộng trừ điểm sau này dễ bị lỗi hoặc crash chương trình.
# Dữ liệu khách hàng không còn chính xác.
# Để kiểm tra dữ liệu trước khi cho phép gán giá trị mới cho __points, ta dùng:

# @points.setter
# def is_eligible_for_voucher(self, bill_amount):
#     return bill_amount >= 200000

# không sử dụng:

# self.customer_name
# self.points

# hay bất kỳ dữ liệu nào của đối tượng.

# Nó chỉ kiểm tra:

# bill_amount >= 200000

# nên việc truyền self là dư thừa.

# Đây không phải hành vi của một đối tượng cụ thể mà là một hàm tiện ích dùng chung cho toàn hệ thống.
# Để gọi được:

# MemberCard.is_eligible_for_voucher(250000)

# ta dùng:

# @staticmethod

# Khác nhau giữa @staticmethod và @classmethod
# Static Method	Class Method
# Không có self	Không có self
# Không có cls	Có cls
# Không truy cập dữ liệu class	Có thể truy cập dữ liệu class
# Chỉ là hàm tiện ích	Thao tác với thuộc tính lớp

class MemberCard:
    def __init__(self, ten_khach, points=0):
        self.customer_name = ten_khach
        self.__points = 0
        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, diem_moi):

        if isinstance(diem_moi, int) and diem_moi >= 0: # isinstance kiểm tra nhập dl
            self.__points = diem_moi
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, diem_cong):
        if diem_cong > 0:
            self.__points += diem_cong

    @staticmethod
    def is_eligible_for_voucher(tien_hoa_don):
        return tien_hoa_don >= 200000