# Input
# Hệ thống yêu cầu nhập 3 thông tin:
# age	Tuổi bệnh nhân	int
# blood_pressure	Huyết áp tâm thu int
# blood_sugar	Đường huyết	int
# Điều kiện đạt chuẩn phẫu thuật
# Bệnh nhân phải thỏa mãn đồng thời:
# Tuổi < 75
# Huyết áp từ 90 → 140
# Đường huyết < 150
# Output
# Nếu hợp lệ:
# ĐỦ ĐIỀU KIỆN PHẪU THUẬT
# Nếu không đạt:
# TỪ CHỐI PHẪU THUẬT
# Nếu dữ liệu âm:
# Dữ liệu nhập vào không hợp lệ
# Đề xuất giải pháp
# Giải pháp 1 — Gộp điều kiện 
# Ý tưởng:
# Dùng một câu if lớn
# Kết hợp nhiều điều kiện bằng and
# Ưu điểm
# Code ngắn gọn
# Dễ viết
# Ít thụt lề
# Nhược điểm
# Khó mở rộng
# Không biết bệnh nhân trượt ở tiêu chí nào
# Thông báo còn chung chung
# Giải pháp 2 — Điều kiện lồng nhau 
# Ý tưởng:
# Kiểm tra từng điều kiện riêng
# Nếu sai thì báo lý do cụ thể
# Ưu điểm
# Thông báo chi tiết
# Giá trị y khoa tốt hơn
# Dễ kiểm tra nguyên nhân
# Nhược điểm
# Code dài hơn
# Nhiều thụt lề hơ
# Giải pháp 1 — Gộp điều kiện (Flat Logic)
# Giải pháp này viết ngắn gọn hơn vì tất cả điều kiện được gộp vào một câu if duy nhất bằng toán tử and. Code ít dòng, ít thụt lề nên dễ nhìn khi bài toán đơn giản. Tuy nhiên, nhược điểm là hệ thống chỉ biết bệnh nhân “đạt” hoặc “không đạt” mà không cho biết nguyên nhân cụ thể. Trong môi trường y tế, điều này làm giảm khả năng hỗ trợ điều dưỡng xử lý tình huống nhanh chóng.
# Giải pháp 2 — Điều kiện lồng nhau (Nested If)
# Giải pháp này kiểm tra từng điều kiện riêng biệt bằng nhiều câu if-elif-else. Code sẽ dài hơn và có nhiều cấp thụt lề hơn, nhưng đổi lại hệ thống có thể thông báo chính xác bệnh nhân bị từ chối vì lý do nào như:
# tuổi vượt giới hạn
# huyết áp không an toàn
# đường huyết quá cao
# Điều này giúp điều dưỡng dễ theo dõi và mang giá trị thực tế cao hơn trong hệ thống y khoa.
# Kết luận
# Nếu ưu tiên code ngắn gọn -> chọn Flat Logic
# Kết luận
# Nếu ưu tiên code ngắn gọn -> chọn Flat Logic

print("HỆ THỐNG SÀNG LỌC TIỀN PHẪU THUẬT ")

age = int(input("Nhập tuổi bệnh nhân: "))
blood_pressure = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập đường huyết (mg/dL): "))

if age < 0 or blood_pressure < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
else:
    if age >= 75:
        print("TỪ CHỐI PHẪU THUẬT")
        print("Lý do: Tuổi vượt giới hạn cho phép.")
    elif blood_pressure < 90 or blood_pressure > 140:
        print("TỪ CHỐI PHẪU THUẬT")
        print("Lý do: Huyết áp không nằm trong ngưỡng an toàn.")
    elif blood_sugar >= 150:
        print("TỪ CHỐI PHẪU THUẬT")
        print("Lý do: Đường huyết quá cao.")
    else:
        print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")