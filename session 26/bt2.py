# Lỗi của code cũ

# Lớp cha:

# class Hero:
#     def use_ultimate(self):
#         raise NotImplementedError(
#             "Lớp con bắt buộc phải có chiêu cuối!"
#         )

# Ý tưởng là:

# Nếu lớp con quên viết use_ultimate()
# thì báo lỗi.

# Nhưng Assassin lại viết:

# class Assassin(Hero):
#     def stealth_kill(self):
#         print("Ám sát")

#         Quên viết

# use_ultimate()

# Tự tạo

# stealth_kill()

# Khi chạy:

# Assassin()

# Python chỉ tạo object.

# Nó chưa hề gọi:

# use_ultimate()
# Do đó:

# team = [Mage(), Assassin()]

# vẫn chạy bình thường.

# Console:

# Tải trận đấu thành công!

# Lỗi chỉ xuất hiện khi:

# for hero in team:
#     hero.use_ultimate()

# đến lượt Assassin.

# Python tìm:

# Assassin.use_ultimate()

# không thấy.

# Nó sẽ chạy lên lớp cha:

# Hero.use_ultimate()

# và gặp:

# raise NotImplementedError

# nên chương trình sập.

from abc import ABC , abstractmethod

class Hero(ABC) :
    @abstractmethod
    def use_ultimate(self) :
        pass

class Mage(Hero) :
    def use_ultimate(self):
        print("Pháp sư tung chiêu : Mưa sao Băng !")
    
class Assassin(Hero) :
    def use_ultimate(self):
        print("Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")
    
print("--- LOADING TRẬN ĐẤU ---")

team_heroes = [Mage(), Assassin()]

print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")

for hero in team_heroes:
    hero.use_ultimate()