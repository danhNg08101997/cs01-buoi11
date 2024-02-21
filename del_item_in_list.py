# Viết chương trình cho người dùng nhập vào 1 giá trị cần xóa, nếu không có giá trị đó trong mảng thì in ra thông báo không tìm thấy phần tử đó nên không thể xóa

# Process
import method
# Input
lst_number = [20,81,97,63,72,11,20,15,33,15,41,20]
num_del = int(input('Nhập vào số cần xóa: '))
# Output
print(method.delete_item_in_list(num_del, lst_number))