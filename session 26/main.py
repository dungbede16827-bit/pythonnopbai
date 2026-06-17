# Role play game 
from abc import ABC ,abstractmethod

# thuộc tính : tên , hp , mana, ky_nang
class NhanVat :

    def __init__(self,id : int, ten :str, hp :float, mana :float,sat_thuong_gay_ra : float):
        self.__id = id
        self.ten = ten
        self.hp = hp
        self.mana = mana
        self.sat_thuong_gay_ra = sat_thuong_gay_ra
    def gioi_thieu_nhan_vat(self) :
        print(f"Ta là {self.ten} : ta có kỹ năng ")
    @abstractmethod
    def hanh_dong_chien_dau(self) :
        print("Ta sẽ chém ngươi bằng kỹ năng đẳng cấp của ta")
    

chien_binh = NhanVat(1,"THiếu Lâm" , 10_000 ,8_000,200)
chien_binh = NhanVat(1,"Cái Bang" , 6_000 ,10_000,350)

# tính kế thừa : trong game thì sẽ dùng để có thể chai các bang phái cụ thể 
# Bang Kim : lớp con , NhanVat : Lớp cha
class BangPhaiKim(NhanVat) :
    def __init__(self, id, ten, hp, mana, sat_thuong_gay_ra,sat_thuong_chuan = 100):
        super().__init__(id, ten, hp, mana, sat_thuong_gay_ra)
        self.sat_thuong_chuan = sat_thuong_chuan
    
    def thuc_hien_an_chay(self) :
        print(f"Tôi là {self.ten} bang kim : Hôm nay tôi sẻ ăn chhay ")
    
    def hanh_dong_chien_dau(self) :
        print("Ta sẽ chém ngươi bằng kỹ năng đẳng cấp của ta")
    # is
    def __add__(self, other):
        if isinstance(other,TrangBi):
            self.hp += other.hp_tang
            self.mana += other.mana_tang
            print(f"đã trang bị đồ thành công chỉ số mới của bạn là {self.hp} , {self.mana}")

class BangPhaiMoc(NhanVat) :
    def __init__(self, id, ten, hp, mana, sat_thuong_gay_ra,chi_so_danh_bay = 200):
        super().__init__(id, ten, hp, mana, sat_thuong_gay_ra)
        self.chi_so_danh_bay = chi_so_danh_bay

    def hanh_vi_chat_cay(self) :
        print(f"Ta là {self.ten} , bây giờ ta sẽ chặt cây")
    def hanh_dong_chien_dau(self) :
        print("Ta sẽ đấm ngươi bằng sức mạnh của ta")

class BangPhaiCute(NhanVat) :
    def __init__(self, id, ten, hp, mana, sat_thuong_gay_ra,chi_so_danh_bay = 200):
        super().__init__(id, ten, hp, mana, sat_thuong_gay_ra)
        self.chi_so_danh_bay = chi_so_danh_bay

    def hanh_vi_Cute(self) :
        print(f"Ta là {self.ten} , bây giờ ta sẽ cute")
    def hanh_dong_chien_dau(self) :
        print(f"Ta là {self.ten} ta sẽ đánh ngươi bằng sự đáng yêu của ta")
    
duc_lop_truong = BangPhaiMoc(2,"Chien binh bé bỏng",1_000,100_000,0,-1)
thi_lop_pho = BangPhaiKim(3,"Thi cute" , 2_000 , 500 ,-20)
duong_bi_thu_lop = BangPhaiCute(4,"DƯơng ngủ gât",1,2,100)
print(duc_lop_truong)
duc_lop_truong.gioi_thieu_nhan_vat()
duc_lop_truong.hanh_vi_chat_cay()
duc_lop_truong.hanh_dong_chien_dau()

thi_lop_pho.hanh_dong_chien_dau()


# tính đa hình
# nhân vật đều phải đánh nhau
# Bang mộc : Đấm tay 
# Bang kim : chém nhau


# khi lắp đồ cho nhân vật thì phải tăng chỉ số nhân vật 
class TrangBi :
    def __init__(self,ten_trang_bi,hp_tang,mana_tang):
        self.ten_trang_bi = ten_trang_bi
        self.hp_tang = hp_tang
        self.mana_tang = mana_tang

vu_khi_co_ban = TrangBi("Dép lào",1_000,2_000)

mac_do_cho_nhan_vat = thi_lop_pho + vu_khi_co_ban

# tính trừ tượng

