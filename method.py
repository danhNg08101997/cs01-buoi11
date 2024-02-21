# Tìm số nhỏ nhất
def find_min_num(arr_num):
    min_num = arr_num[0]
    # Duyệt 1 chiều
    # for num in arr_num:
    #     if num < min_num:
    #         min_num = num
    
    # index = 0
    # while index < len(arr_num):
    #     if arr_num[index] < min_num:
    #         min_num = arr_num[index]
    #     index += 1
    
    # index = len(arr_num) - 1
    # while index > 0:
    #     if arr_num[index] < min_num:
    #         min_num = arr_num[index]
    #     index -= 1
    
    # Duyệt 2 chiều (tối ưu)
    index_left = 0
    index_right = len(arr_num) - 1
    while index_left <= index_right:
        if arr_num[index_left] < min_num:
            min_num = arr_num[index_left]
        if arr_num[index_right] < min_num:
            min_num = arr_num[index_right]
        index_left += 1
        index_right -= 1
    return min_num
# --------------------------------------------------------------------
# Tìm tần suất của số
def tim_tan_suat_cua_so_hon_2(arr_num):
    output = []
    for num_item in arr_num:
        tan_suat = tim_tan_suat_so(num_item, arr_num)
        if tan_suat >= 2:
            output.append(num_item)
    return set(output)
def tim_tan_suat_so(num, arr_num):
    output = 0
    for num_item in arr_num:
        if num == num_item:
            output += 1
    return output
# Tối ưu
def tim_tan_suat_hon_2_dict(lst_num):
    output = []
    dict_num = {}
    for num_item in lst_num:
        if num_item in dict_num:
            dict_num[num_item] += 1
        else:
            dict_num[num_item] = 1
    for key in dict_num:
        if dict_num[key] >= 2:
            output.append(key)
    return output
# --------------------------------------------------------------------------
# Tìm vị trí phần tử có trong mảng
def find_index(num,lst_number):
    index_output = []
    for index, value in enumerate(lst_number):
        if value == num:
            index_output.append(index)
    if index_output:
        return f'index của {num} là {index_output}'
    else:
        return f'Không tìm thấy {num} trong list'
# ------------------------------------------------------------------------
# Xóa các phần tử trong mảng (mảng sẽ thay đổi thứ tự index => ta sẽ xóa ngược thay vì xóa xuôi)
def delete_item_in_list(num_del, lst_number):
    index = len(lst_number) - 1
    if num_del in lst_number:
        while index >= 0:
            if num_del == lst_number[index]:
                lst_number.pop(index)
            index -= 1
        return lst_number
    else:
        return f'Không có giá trị {num_del} trong {lst_number}' 
# -----------------------------------------------------------------------------
# Kiểm tra số nguyên tố
import math
def kiem_tra_so_nt(num):
    output = True
    if num < 2:
        output = False
        return output
    uoc = 2
    while uoc <= math.sqrt(num):
        if num % uoc == 0:
            output = False
            break
        uoc += 1
    return output