
# - Input:
#    Du lieu nguoi dung nhap tu ban phim luon co kieu chuoi (str) Can ep kieu ve int de kiem tra co phai so nguyen hay khong Neu gia tri <= 0 thi khong hop le va phai nhap lai.
# - Output:Neu nhap sai: in thong bao loi va tiep tuc yeu cau nhap.Neu nhap dung so nguyen duong: in "Ghi nhan thanh cong".
# | Tieu chi | while True + break | while voi bien dieu kien |
# | Do ngan gon cua code | Ngan gon hon | Dai hon vi can bien trang thai |
# | Muc do de hieu | Gan voi y tuong: lap vo han den khi dung thi break | De theo doi trang thai, nhung nhieu bien hon |
# Chon giai phap while True + break vi yeu cau nghiep vu la "bat nhap lai cho den khi dung".
# Cach nay ngan gon, ro rang va phu hop voi validation loop trong CLI.
        

while True:
    so_luong_nhan_su_moi = int(input("Vui long nhap so luong nhan su moi trong thang nay: "))

    if(so_luong_nhan_su_moi) <= 0 :
        print("Loi: So luong nhan su moi phai la so nguyen lon hon 0. Vui long nhap lai.")
    else :
        print("Ghi nhan thanh cong")
        break






