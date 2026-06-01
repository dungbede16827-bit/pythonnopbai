saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True :
    print("""

===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình

""")
    
    choice = input("Nhập lựa chọn : ").strip()

    if choice == "1" :
        if len(saving_accounts) == 0 :
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else :
            print("\n Danh sách sổ tiết kiệm : ")

            for index, account in enumerate(saving_accounts,start=1) :
                print(
                    f"{index}."
                    f"Mã số : {account['account_id']} |"
                    f"Khách hàng: {account['customer_name']} |"
                    f"Số tiền gửi: {account['balance']} |"
                    f"Thời hạn: {account['term_months']} tháng |"
                    f"Lãi suất: {account['interest_rate']}%/ năm |"
                    f"Trạng thái: {account['status']}"
                )
    elif choice == "2" :
        account_id = input("Nhập mã sổ tiết kiệm: ").upper().strip()
        customer_name = input("Nhập tên khách hàng: ").strip()
        balance_input = input("Nhập số tiền gửi: ").strip()
        term_input = input("Nhập thời hạn (tháng): ").strip()
        interest_input = input("Nhập lãi suất (%/năm): ").strip()

        if customer_name == "" :
            print("Tên khách hàng không được để trống")
            
        else :

            duplicate = False

            for account in saving_accounts :
                if account['account_id'] == account_id :
                    duplicate = True
                    break
            if duplicate :
                print("Mã sổ tiết kiệm đã tồn tại, vui lòng chọn mã khác")

            elif (not (balance_input.isdigit()) or not (term_input.isdigit()) or int(balance_input) <= 0 or int(term_input) <= 0 ):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ ")

            elif  not (interest_input.replace('.','',1).isdigit()) or float(interest_input) <= 0 :
                print("Lãi suất không hợp lệ")
            else :
                new_account = {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": int(balance_input),
                    "term_months": int(term_input),
                    "interest_rate": float(interest_input),
                    "status": "active"
                }
                saving_accounts.append(new_account)
                print("Mở sổ tiết kiệm thành công !")
    elif choice == "3" :
        input_id = input("NHập mã sổ tiết kiệm cần cập nhật: ").upper().strip()

        found = False 
        for account in saving_accounts :

            if account["account_id"] == input_id : 
                found = True 
                if account["status"] == "closed" :
                    print("không thể cập nhật sổ tiết kiệm đã tất toán!")
                    break

                customer_name = input("Nhập tên khách hàng mới : ").strip()
                balance_input = input("nhập số tiền gửi mới : ").strip()
                term_input = input("Lập lãi suất mới mới : ").strip()

                if customer_name == "" :
                    print("Tên khách hàng không được để trống")

                elif (not (balance_input.isdigit()) or not (term_input.isdigit()) or int(balance_input) <= 0 or int(term_input) <= 0 ):
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ ")

                elif  not (interest_input.replace('.','',1).isdigit()) or float(interest_input) <= 0 :
                    print("Lãi suất không hợp lệ")
                
                else :
                    account["customer_name"] = customer_name
                    account["balance"] = int(balance_input)
                    account["term_months"] = int(term_input)
                    account["interest_rate"] = float(term_input)

                    print("Cập nhập thành công ! ")

                break
        if found == False :
            print("Không tìm thấy mã số tiết kiệm !")

    elif choice == "4" :
        input_id = input(" nhập mã sổ tiết kiệm cần tất toán : ").upper().strip()

        found = False

        for account in saving_accounts :

            if account["account_id"] == input_id:
                found = True 
                account["status"] = "closed"
                print("tất toán thành công !")
                break 
        if found == False :
            print("Không tìm thấy mã số tiết  tiết kiệm ")
    elif choice == "5":

        input_id = input(
            "Nhập mã sổ tiết kiệm cần tính lãi: "
        ).upper().strip()

        found = False

        for account in saving_accounts:

            if account["account_id"] == input_id:

                found = True

                if account["status"] == "closed":

                    print(
                        "Không thể thao tác với sổ tiết kiệm đã tất toán"
                    )

                    break

                interest = (
                    account["balance"]
                    * account["interest_rate"]
                    / 100
                    * account["term_months"]
                    / 12
                )

                total = account["balance"] + interest

                print("Tiền lãi dự kiến:", interest)

                print("Tổng tiền nhận:", total)

                break

        if found == False:
            print("Không tìm thấy mã sổ tiết kiệm")
    elif choice == "6":

        input_id = input(
            "Nhập mã sổ tiết kiệm cần kiểm tra: "
        ).upper().strip()

        real_month = input(
            "Nhập số tháng thực gửi: "
        ).strip()

        if not real_month.isdigit() or int(real_month) <= 0:

            print("Số tháng thực gửi không hợp lệ!")

        else:

            real_month = int(real_month)

            found = False

            for account in saving_accounts:

                if account["account_id"] == input_id:

                    found = True

                    if account["status"] == "closed":

                        print(
                            "Không thể thao tác với sổ tiết kiệm đã tất toán"
                        )

                        break

                    if real_month < account["term_months"]:

                        rate = 0.5

                        print("Khách hàng rút trước hạn!")

                    else:

                        rate = account["interest_rate"]

                        print(
                            "Khách hàng đủ điều kiện hưởng lãi đúng hạn!"
                        )

                    interest = (
                        account["balance"]
                        * rate
                        / 100
                        * real_month
                        / 12
                    )

                    total = account["balance"] + interest

                    print("Tiền lãi thực nhận:", interest)

                    print("Tổng tiền thực nhận:", total)

                    break

            if found == False:
                print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == "7":

        print("Thoát chương trình!")

        break

    else:

        print("Lựa chọn không hợp lệ, vui lòng nhập lại")


        

                

