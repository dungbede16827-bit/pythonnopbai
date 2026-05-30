list_user = ["an","nam","hùng"]

# tuple () 
list_user_fix = (1,2,3,4,5)

list_user_fix_v2 = 1,2,3,4,5 
print(type(list_user_fix_v2))

# bất biến 
# list_user_fix_v2[1] = 3 # lỗi 

list_user_fix_v2 = (2,3,4)
print((list_user_fix_v2))

tuple_age = (1,) # chỉ nguyên 1 thì là int thêm , là tuple 
print(type(tuple_age))


# dict {}

dict_formation  = {
    "id_user" : 1,
    "name" :  "Cao Nguyễn Anh Dương",
    "age"  :  18,
    "address" : "BA VI , HA NOI" ,
    "is_status" : True
}

# print(f"quê của đối tượng ở {dict_formation.get("que","Hà Nội")}") # nếu không có que thì giá trị mặc định là Hà Nội dùng get mà key kh có mà kh có giá trị truyền mặc định thì in none

# print(f"Quê của đối tượng ở {dict_formation.get("address").get("address_name")}") truy cập thêm vào biến trong

# dict["key"]

print(f"tuổi của đối tượng {dict_formation["age"]}")


# update 
dict_formation["is_status"] = False

print(dict_formation)

dict_formation.update({"is_status" : True} )
print(dict_formation)

# Create 
dict_formation["Sex"] = "Nữ"
print(dict_formation)

# # Delete pop("key")
# sex_info = dict_formation.pop("sex")
# print(sex_info)


# duyệt qua key 
for key in dict_formation.keys():
    print(F" Các key : {key}")

#duyệt qua value 
for value in dict_formation.values() :
    print(f" các value {value}")

# duyêt qua key , value 
for key,value in dict_formation.items() :   
    print(f"{key} . {value}")

d = {'A':1, 'A':2}


t = (a,) * 3,
print(t)
a,b = (1,2,3)


# ktra mã sản phẩm có tồn tại hay kh 

id_user = 1

is_status 
if (id_user in list_id ) :

while id_user not in list_id :
    print("ID Không tồn tại ")


