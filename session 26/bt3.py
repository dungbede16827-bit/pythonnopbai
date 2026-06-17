from abc import ABC, abstractmethod


class Champion(ABC):

    def __init__(self, champion_id, name, base_hp, base_atk):

        self.champion_id = champion_id
        self.name = name

        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):

        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()

        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other

        return NotImplemented

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()

    def display_info(self):
        print(
            f"{self.champion_id:<8}"
            f"{self.name:<20}"
            f"{self.get_he():<10}"
            f"{self.base_hp:<8}"
            f"{self.base_atk:<8}"
            f"{self.get_special_info():<20}"
            f"{self.get_combat_power():.0f}"
        )

class Warrior(Champion):
    def __init__(self,champion_id,name,base_hp,base_atk,shield_bonus):
        super().__init__(champion_id,name,base_hp,base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus

    def get_he(self):
        return "Warrior"

    def get_special_info(self):
        return f"Armor: {self.shield_bonus}"
    
class Mage(Champion):

    def __init__(self,champion_id,name,base_hp,base_atk,ability_power):
        super().__init__(champion_id,name,base_hp,base_atk )
        self.ability_power = ability_power
    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power

    def get_he(self):
        return "Mage"

    def get_special_info(self):
        return f"Mana: {self.ability_power}"
    
champion_pool = [
Warrior("WAR01","Rikkei Knight", 1200, 300, 150 ),

Warrior( "WAR02", "Steel Guardian", 1500, 250, 200 ),

Mage("MAG01","Rikkei Wizard", 800, 500, 2.0 )
]

def show_champions():
    print("\n--- DANH SÁCH QUÂN CỜ ---")
    print(
        f"{'Mã':<8}"
        f"{'Tên tướng':<20}"
        f"{'Hệ':<10}"
        f"{'HP':<8}"
        f"{'ATK':<8}"
        f"{'Chỉ số riêng':<20}"
        f"{'Chiến lực'}"
    )
    print("-" * 90)

    for champ in champion_pool:
        champ.display_info()

def compare_champions():
    id1 = input("Nhập mã tướng thứ nhất: ")
    id2 = input("Nhập mã tướng thứ hai: ")
    c1 = None
    c2 = None
    for champ in champion_pool:
        if champ.champion_id == id1:
            c1 = champ
        if champ.champion_id == id2:
            c2 = champ
    if c1 is None or c2 is None:
        print("Mã tướng không hợp lệ!")
        return
    if c1 > c2:
        print(f"{c1.name} mạnh hơn {c2.name}" )
    else:
     print( f"{c2.name} mạnh hơn {c1.name}")

def team_power():
    ds = input( "Nhập mã tướng (cách nhau bằng dấu phẩy): ")
    ids = ds.split(",")
    total = 0

    for ma in ids:
        ma = ma.strip()
        found = False
        for champ in champion_pool:
            if champ.champion_id == ma:
                total = champ + total
                found = True
        if not found:
            print(f"Mã tướng {ma} không hợp lệ, bỏ qua!")

    print(f"Tổng chiến lực đội hình: {total:.0f}")


def main():

    while True:

        print("\n===== RIKKEI RPG =====")
        print("1. Hiển thị tướng")
        print("2. So sánh tướng")
        print("3. Tính chiến lực đội hình")
        print("4. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            show_champions()

        elif choice == "2":
            compare_champions()

        elif choice == "3":
            team_power()

        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()