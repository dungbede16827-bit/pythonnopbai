# để xây dựng một đối tượng cụ thể thì trước tiên phải xây dựng class

# class : Bản thiết kế về tài khoản ngân hàng
# THuộc tính : id , Ten_nguoi_dung , mat_khau , so_du, dia_chi,
class BankAccount :
    def __init__(self,id,ten_nguoi_dung,mat_khau,so_du,dia_chi = "Hà Nội"):
        self.id = id
        self.ten_nguoi_dung = ten_nguoi_dung
        self.mat_khau = mat_khau
        self.__so_du = so_du
        self.dia_chi = dia_chi
    def hien_thi_thong_tin_the (self) :
        print(f"ID : {self.id[0]} | Tên Thẻ : {self.ten_nguoi_dung[0]}")

    @staticmethod
    def kiem_tra_tinh_hop_le(type_money) :
        list_type = ["VND" , "ERUP","Yên"]
        if type_money in list_type :
            print("Hợp lệ có thể chuyển tiền ")
        else :
            print("Ngân hàng không dùng tiền tệ này quy đổi")
    # tinh đóng gói : để lấy các thuộc tính private
    # get : lấy 

    @property
    def lay_so_du (self):
        return self.__so_du
    
    # thuoctinh.setter
    @so_du.setter
    def thanh_toan_tien(self , tien_thanh_toan) :
        if(self.__so_du[0] < tien_thanh_toan) :
            print("số dư không đủ thanh toán ")
        else :
            self.__so_du[0] -= tien_thanh_toan
            print("Đã thanh toán hóa đơn")
    


account_01 = BankAccount(1,"PhongGay","12345",123456,"Ninh Bình")
print(account_01.id,account_01.ten_nguoi_dung)

account_01.hien_thi_thong_tin_the()
account_01.kiem_tra_tinh_hop_le("USD")

BankAccount.kiem_tra_tinh_hop_le("USD")

print(account_01.lay_so_du())

print(account_01.lay_so_du[0])
account_01.thanh_toan_tien(100_000)

    
