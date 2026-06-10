import logging
from unittest import case

logging.basicConfig(
    filename="arena_tickets.log"__
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"


)
"""
DEBUG

INFO: CHAY BINH THUONG
WARNING : CANH BAO NHUNG CHUONG TRINH VAN CHAY
ERROR: BAO LOI CHUONG TRINH
CRITICAL: GAY LOI NANG VS CHUONG TRINH
asctime : tgian thuc
level name

"""

ticket_db = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
]

def display_tickets(tickets) :
    if len(tickets) == 0 :
        print("danh sách vé trống !")
    print("========================================================================================================================================================")
    print(f" {'Mã vé :':<10} | {'Tên người mua :':<30} |{'Giá vé :':<15} | {'Trạng thái :':<15} |{'Chỗ ngồi :':<15}  ")
    for i in tickets :
        try :
            seat_info = f"{i['seat'][0]}-{i['seat'][1]}"
            status = i["status"]
            if status == "Booked" :
                status = "Đã đặt"
            elif status == "Cancelled" :
                status = "Đã hủy"
                print(f" {i['ticket_id']:<10} | {i['buyer_name']:<30} |{i['price']:<15} | {status:<15} |{seat_info:<15}  ")
        except KeyError as e :
            print("lỗi: một vé đang bị thiếu dữ liệu vui hòng ktra lại :")
            logging.error(f"ERROR - Missing key while displaying ticket: - {e}")
            return
    logging.info("User viewed ticket list.")

def book_ticket(tickets) :
    new_ma = input("mời bạn nhập vào mã vé :").strip().upper()
    is_flag = 0
    for i in tickets :
        if i["ticket_id"] == new_ma :
            print("mã vé đã tồn tại !")
            is_flag = 1
            break
        if is_flag == 1 :
            print("mời bạn nhập lại mã vé !")
            logging.warning(f"User attempted to book an existing ticket.")
            return
        new_name = input("mời bạn nhập vào tên người mua :").strip()
        while True :
            try :
                new_price = float(input("mời bạn nhập vào giá vé :"))
                if new_price <= 0 :
                    print("giá vé phải lớn hơn 0 !")
                    continue
                break
            except ValueError :
                print("giá vé phải là một số hợp lệ !")
                logging.warning(f"User entered invalid price while booking a ticket.")

        new_area = input("mời bạn nhập vào khu vực chỗ ngồi (A/B/C) :").strip().upper()
        while True :
            try :
                new_seat_number = int(input("mời bạn nhập vào số ghế :"))
                if new_seat_number <= 0 :
                    print("số ghế phải lớn hơn 0 !")
                    continue
                break
            except ValueError :
                print("số ghế phải là một số hợp lệ !")
                logging.warning(f"User entered invalid seat number while booking a ticket.")

        ticket_db.append({
            "ticket_id": new_ma,
            "buyer_name": new_name,
            "price": int(new_price),
            "status": "Booked",
            "seat": (new_area, new_seat_number)
        })
        logging.info(f"User booked a new ticket with ID: {new_ma}")
        print("đặt vé thành công !")


while True:
        print("""===========================    
    === HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===
1. Xem danh sách vé đã bán
2. Đặt vé mới
3. Đổi chỗ ngồi (Cập nhật vé)
4. Hủy vé
5. Báo cáo doanh thu
6. Thoát chương trình
======================================== 
Chọn chức năng (1-6):
""")
        choice = input("Mời bạn lựa chọn chức năng (1-6): ")
        match choice:   
             case "1":
                display_tickets(ticket_db)
             case "2":
                book_ticket(ticket_db)
             case "3":
                update_ticket(ticket_db)

