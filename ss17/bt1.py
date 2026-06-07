raw_logs = []
processed_logs = []


def clean_logs(raw_text):
    """
    Làm sạch dữ liệu log.
    Xóa các ký tự đặc biệt ! @ # $
    Sau đó tách các log bằng dấu ;
    Args:
        raw_text (str): Chuỗi log thô.
    Returns:
        list: Danh sách log đã làm sạch.
    """

    table = str.maketrans("", "", "!@#$")

    cleaned_text = raw_text.translate(table)

    logs = [log.strip() for log in cleaned_text.split(";") if log.strip()]

    return logs


def load_logs():
    """
    Nhập dữ liệu log từ bàn phím
    và lưu vào biến toàn cục raw_logs.
    """

    global raw_logs

    print("\n--- NẠP DỮ LIỆU LOG ---")

    raw_text = input(
        "Nhập chuỗi log thô (cách nhau bởi dấu ;): "
    )

    raw_logs = clean_logs(raw_text)

    print(
        f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống."
    )


def filter_danger_logs():
    """
    Lọc các log chứa ERROR hoặc CRITICAL.

    Sử dụng List Comprehension.

    Returns:
        list: Danh sách log nguy hiểm.
    """

    global processed_logs

    if not raw_logs:
        print(
            "Chưa có dữ liệu log, vui lòng thực hiện chức năng 1"
        )
        return

    processed_logs = [
        log
        for log in raw_logs
        if "ERROR" in log.upper()
        or "CRITICAL" in log.upper()
    ]

    print("\n--- LỌC CẢNH BÁO ---")

    if not processed_logs:
        print("Không tìm thấy cảnh báo nguy hiểm.")
        return

    print(
        f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:"
    )

    for log in processed_logs:
        print("-", log)


def mask_ip_address():
    """
    Mã hóa IP trong các log nguy hiểm.

    Ví dụ:
    192.168.1.1
    =>
    192.168.*.*

    Returns:
        list: Danh sách log đã mã hóa IP.
    """

    if not raw_logs:
        print(
            "Chưa có dữ liệu log, vui lòng thực hiện chức năng 1"
        )
        return

    if not processed_logs:
        print(
            "Chưa có dữ liệu cảnh báo, vui lòng thực hiện chức năng 2"
        )
        return

    masked_logs = []

    for log in processed_logs:

        words = log.split()

        for index, word in enumerate(words):

            if "." in word:

                ip_parts = word.split(".")

                if len(ip_parts) == 4:

                    masked_ip = ".".join(
                        ip_parts[:2] + ["*", "*"]
                    )

                    words[index] = masked_ip

        masked_logs.append(" ".join(words))

    print("\n--- MÃ HÓA IP ---")
    print("Báo cáo log an toàn:")

    for index, log in enumerate(masked_logs, start=1):
        print(f"{index}. {log}")

    return masked_logs


def main():
    """
    Hàm điều khiển chương trình.
    """

    while True:

        print("""
============= SECURITY LOG ANALYZER =============
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
=================================================
""")

        choice = input(
            "Chọn chức năng (1-4): "
        ).strip()

        if choice == "1":
            load_logs()

        elif choice == "2":
            filter_danger_logs()

        elif choice == "3":
            mask_ip_address()

        elif choice == "4":
            print(
                "\nĐóng hệ thống. Tạm biệt!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ!"
            )


main()