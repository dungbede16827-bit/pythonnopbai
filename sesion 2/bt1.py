# lỗi red bị bỏ qua là điều kiện đầu tiên phải là lớn hơn 120 là đỏ là điều kiện lớn nhất thì 
# phải xếp lên đầu nhưng lại cho vàng lên đầu thì mặc định chỉ cần lớn hơn 100 là vàng ngay nên dữ liệu bị sai sửa lại

# Hệ thống phân loại ưu tiên
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate >= 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")