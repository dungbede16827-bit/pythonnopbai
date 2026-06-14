import os


def create_folder():

    print(
        "\n----- KHỞI TẠO THƯ MỤC -----"
    )

    if not os.path.exists(
        "aviation_logs"
    ):

        os.mkdir("aviation_logs")

        print("Tạo thư mục thành công!")

    else:

        print(
            "Thư mục đã tồn tại, "
            "bỏ qua bước khởi tạo"
        )