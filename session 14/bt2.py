# Bên trong hàm:

# def add_reward_points(points_earned):
#     total_points = total_points + points_earned

# Python nhìn thấy phép gán:

# total_points = ...

# nên tự động hiểu rằng total_points là biến cục bộ (local) của hàm.

# Nhưng ở vế phải:

# total_points + points_earned

# Python phải đọc giá trị total_points trước.

# Vấn đề là biến local này chưa được gán giá trị nào.

# Nó giống như:

# def test():
#     x = x + 1

# Python hiểu:

# tạo biến local x
# nhưng lại dùng x trước khi khởi tạo.

# → gây lỗi UnboundLocalError.
# Keyword cần dùng:

# global

# Hàm cộng điểm thưởng
def add_reward_points(current_points, points_earned):
    total = current_points + points_earned
    return total

# Tổng điểm hiện tại
total_points = 100

# Khách được thưởng 50 điểm
total_points = add_reward_points(total_points, 50)

print("Đã cộng thêm 50 điểm.")
print("Tổng điểm hiện tại của khách hàng:", total_points)