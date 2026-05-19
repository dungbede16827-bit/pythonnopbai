# tuôi rlowns hơn 18 , tiền lớn hơn 10 triệu 
# thì in ra là true còn một trong 2 sai thì ra là false

age = 18
money = 10_000_0000

if (age > 18 and money > 10000000) :
    print('True')
else :
    print('false')

if age > 16 :
    print("tôi lớn rồi") # đoạn code nằm trong if 
else :
    print("tôi còn nhỏ")

a = 10 # đây là hết câu đk if (ngoài câu điều kiện if)

# điểm từ 8 -> 10 in ra sinh viên xuất sắc
# điểm từ 6- 8 sinh viên vừa vừa 
# còn lại thì sinh viên cần nỗ lực

diem = int(input("Mời bạn nhập điểm"))

if diem > 8 and diem <= 10 :
    print(" sinh viên xuất sắc")
elif diem > 6 and diem <= 8 :
    print("sinh vien vua vua")
else : 
    print("sinh viên cần nỗ lực")

level = input("CHỌN LEVEL (easy / hard)")

match level.lower(): 
    case "easy" :
        print("level dễ ")
    case "hard" :
        print("level khó hơn")
