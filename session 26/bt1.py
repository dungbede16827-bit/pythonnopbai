# # # Code lỗi:

# # # class Warrior(Character):
# # #     def __init__(self, name, hp, attack_power, bonus_armor):
# # #         self.bonus_armor = bonus_armor

# # Khi tạo:

# # w1 = Warrior("Arthur", 1000, 150, 50)

# # Python chỉ chạy:

# # self.bonus_armor = 50

# # và dừng.

# # Lúc này object chỉ có:

# # bonus_armor

# # không có:

# # name
# # hp
# # attack_power
# Sau đó chương trình chạy:

# print(w1.name)

# Python đi tìm:

# name

# nhưng không tồn tại

# sửa lại

# class Warrior(Character):
#     def __init__(self, name, hp, attack_power, bonus_armor):
#         super().__init__(name, hp, attack_power)
#         self.bonus_armor = bonus_armor


# lỗi thứ hai khi dùng dấu >

# Giả sử đã sửa lỗi đầu tiên.

# Chương trình chạy đến:

# if w1 > w2:

# Python sẽ báo:

# TypeError
# Python không biết phải so sánh cái gì.

# Phải nạp chồng toán tử.

# Magic Method cần dùng là:

# __gt__()

# (gt = greater than)

# Hàm nhận 2 tham số:

# def __gt__(self, other):

# Trong đó:

# self = đối tượng bên trái
# other = đối tượng bên phải

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor
    
    def __gt__(self, other):
        return self.get_total_power() > other.get_total_power()
    
w1 = Warrior("Arthur", 1000, 150, 50)
w2 = Warrior("Lancelot", 900, 180, 10)

print(f"Chiến binh {w1.name} xuất trận!")

if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")