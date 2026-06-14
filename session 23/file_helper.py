import os


def create_log_dir(dir_name: str) -> bool:
    """
    Tạo thư mục lưu log nếu chưa tồn tại
    """

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    return True