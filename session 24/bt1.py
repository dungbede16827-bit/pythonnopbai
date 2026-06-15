# Việc gán trực tiếp:

# order_table1.total_amount = 0

# đang vi phạm tính chất:

# Encapsulation (Đóng gói)

# Vì thuộc tính total_amount đang là thuộc tính public nên bất kỳ ai cũng có thể truy cập và thay đổi giá trị từ bên ngoài class

# Để kích hoạt cơ chế Name Mangling trong Python, cần đổi:

# total_amount

# thành:

# __total_amount
# Nếu muốn các phần khác của chương trình chỉ được xem tổng tiền mà không được sửa trực tiếp, ta dùng:

# @property

# Ví dụ:

# @property
# def total_amount(self):
#     return self.__total_amount

# def update_vat_rate(self, new_rate):
#     self.vat_rate = new_rate

# Python không sửa biến lớp (Class Attribute) mà tạo ra một biến instance mới cho riêng đối tượng hiện tại.
# Để thay đổi VAT cho toàn bộ hệ thống, cần sử dụng:

# @classmethod

# và thay tham số:

# self

# bằng:

# cls

class CoffeeOrder:
    vat_rate = 0.1

    def __init__(self, so_ban):
        self.so_ban = so_ban
        self.__tong_tien = 0

    @property
    def tong_tien(self):
        return self.__tong_tien

    def add_item(self, gia):
        if gia > 0:
            self.__tong_tien += gia

    def tinh_hoa_don(self):
        return self.__tong_tien * (1 + CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, vat_moi):
        if 0 <= vat_moi <= 1:
            cls.vat_rate = vat_moi



ban_1 = CoffeeOrder("Bàn 1")
ban_2 = CoffeeOrder("Bàn 2")

ban_1.add_item(50000)
ban_2.add_item(30000)

print("TRƯỚC KHI ĐỔI VAT ===")
print("Tiền bàn 1:", ban_1.tong_tien)
print("Tiền bàn 2:", ban_2.tong_tien)
print("VAT:", CoffeeOrder.vat_rate)

ban_1.__tong_tien = 0

print("\n=== SAU KHI GIAN LẬN ===")
print("Tiền thực tế bàn 1:", ban_1.tong_tien)

CoffeeOrder.update_vat_rate(0.08)

print("\n=== SAU KHI ĐỔI VAT ===")
print("VAT bàn 1:", ban_1.vat_rate)
print("VAT bàn 2:", ban_2.vat_rate)

print(
    "Hóa đơn bàn 1:",
    ban_1.tinh_hoa_don(),
    "VNĐ"
)

print(
    "Hóa đơn bàn 2:",
    ban_2.tinh_hoa_don(),
    "VNĐ"
)