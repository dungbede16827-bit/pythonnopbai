tong_doanh_thu = 0
so_ngay_dat_muc_tieu = 0

for ngay in range(1, 8):
    doanh_thu = int(input(f"Nhập doanh thu Ngày {ngay}: "))
    
 
    tong_doanh_thu += doanh_thu
   
    if doanh_thu >= 5000000:
        so_ngay_dat_muc_tieu += 1


trung_binh = tong_doanh_thu / 7


print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print("Tổng doanh thu cả tuần:", tong_doanh_thu, "VND")
print("Doanh thu trung bình mỗi ngày:", int(trung_binh), "VND")
print("Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND):", so_ngay_dat_muc_tieu, "ngày")