# Viết chương trình kiểm tra trong list có bao nhiêu số nguyên tố, in ra màn hình

# input
lst_number = [20,81,97,63,72,11,20,15,33,15,41,20]
# output
lst_output = []
# process
import method
for num in lst_number:
    if method.kiem_tra_so_nt(num):
        lst_output.append(num)

print(f'Danh sách các số nguyên tố trong list: {lst_output}')