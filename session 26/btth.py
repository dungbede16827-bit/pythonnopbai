from abc import ABC ,abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name 

    def display_info (self) :
        print(f"Ma NV : {self.employee_id} | HO VA TEN : {self.name} | LOAI : {self.get_loai()}")

    @abstractmethod
    def calculate_salary(self):
        pass
    @abstractmethod
    def get_loai(self):
        pass



class FullTimeEmployee(Employee) :
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__( employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus
    def calculate_salary(self) :
        return self.base_salary + self.bonus
    def get_loai(self) :
        return "FUll - Time"
        
class PartTimeEmployee(Employee) :
    def __init__(self, employee_id, name,working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours =working_hours
        self.hourly_rate = hourly_rate
    def calculate_salary(self) :
        return self.working_hours*self.hourly_rate
    def get_loai(self):
        return "Fart-time"
    
class InternEmployee(Employee) : 
    def __init__(self, employee_id, name,allowance):
        super().__init__(employee_id, name)
        self.allowance=allowance
    def calculate_salary(self):
        return self.allowance
    def get_loai(self):
        return "Intern"

def salary_emp (employee) :
    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")  
    total = 0 
    for emp in employee :
        salary = emp.calculate_salary()
        total += salary
        print(f"{emp.employee_id} |{emp.name} | {emp.get_loai()}|{salary:,} VND")
    print(f"TONG QUY LUONG : {total:,} VND")


employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]





while True :
    chosse = input("""
=== EMPLOYEE SALARY MANAGER ===
1. Xem danh sách nhân viên
2. Tính lương toàn bộ nhân viên
3. Thoát chương trình
================================
Chọn chức năng (1-3):
""")
    
    match chosse:
        case "1" :
            print("\nDANH SACH NHAN VIEN")
            for emp in employees:
                emp.display_info()
        case "2":
            salary_emp(employees)

                
            
        case "3":
            print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
            break
            
            
            

            
