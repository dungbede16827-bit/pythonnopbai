# cho một list [100,200,300,101,103]
# tạo một list khác chỉ chứa các số lẻ

list_number = [100,200,300,101,103]

list_number2 = [100,200,300,101,103]
list_number.append(list_number2)
new_list = list()
for i,n in enumerate(list_number,start=0) :
    if n % 2 == 1 :
        new_list.append(n)
print(new_list)

lst = [1, 2, 3]
print(lst + [4])
print(lst)
a = [1, 2]
b = a
a += [3]
print(b)