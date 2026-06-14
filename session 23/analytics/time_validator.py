from datetime import datetime


def parse_and_inspect_date(
    date_str
):
    """
    Kiểm tra ngày upload
    """

    try:
        return datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )

    except ValueError:
        print(
            f"[ERROR] Định dạng ngày upload "
            f"'{date_str}' không tồn tại"
        )
        return None