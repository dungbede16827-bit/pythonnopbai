class Drink:
    def __init__(self,code,name,price):
        self.code = code
        self.name = name
        self.__price = price
        self.available = True


    @property
    def price(self) :
        return self.__price
    
    def chuyen_doi_co_san(self) :
        self.available = not self.available

    def get_status(self) :
        return "Đang bán" if self.is_available else "Ngừng bán"

menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

def show_menu():
    print("\n--- DANH SÁCH ĐỒ UỐNG ---")
    print(f"{'Mã món':<8} | {'Tên món':<20} | {'Giá bán':<10} | Trạng thái")
    print("-" * 65)

    for drink in menu:
        print(
            f"{drink.code:<8} | "
            f"{drink.name:<20} | "
            f"{drink.price:<10} | "
            f"{drink.get_status()}"
        )

def add_drink():
    code = input("Nhập mã món: ").strip()

    for drink in menu:
        if drink.code == code:
            print("Mã món đã tồn tại trong hệ thống!")
            return

    name = input("Nhập tên món: ").strip()

    try:
        price = float(input("Nhập giá bán: "))

        if price <= 0:
            print("Giá bán không hợp lệ!")
            return

    except ValueError:
        print("Giá bán không hợp lệ!")
        return

    new_drink = Drink(code, name, price)
    menu.append(new_drink)

    print(f"Thành công: Đã thêm món {name} vào thực đơn!")

def update_status():
    code = input("Nhập mã món cần cập nhật: ").strip()

    for drink in menu:
        if drink.code == code:
            drink.toggle_available()

            print(f"Đã cập nhật trạng thái món {code}.")
            print(f"Trạng thái hiện tại: {drink.get_status()}")
            return

    print("Không tìm thấy món có mã này!")


while True:
    choice = input("""
=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===

1. Xem danh sách đồ uống
2. Thêm đồ uống mới
3. Cập nhật trạng thái kinh doanh
4. Thoát chương trình

==============================================
Chọn chức năng (1-4):

""")
    
    match choice:
        case "1":
            show_menu()

        case "2":
            add_drink()

        case "3":
            update_status()

        case "4":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")