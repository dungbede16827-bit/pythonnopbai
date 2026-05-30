# ictionary có 4 key:

# employee_id
# full_name
# department
# status
# employee_id = employee[0]

# Dictionary không truy cập bằng index như list.

# 0 không phải key của dictionary.

# Nên gây lỗi:
# Dictionary truy cập bằng:

# key

# không phải index.
# full_name = employee["name"]

# Trong dictionary không có key "name".

# Nên gây:

# KeyError


employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}


employee_id = employee["employee_id"]


full_name = employee["full_name"]


employee["status"] = "official"

employee["base_salary"] = 15000000


del employee["department"]

print("Mã nhân viên:", employee_id)

print("Họ tên nhân viên:", full_name)

print(
    "Thông tin nhân viên sau xử lý:",
    employee
)