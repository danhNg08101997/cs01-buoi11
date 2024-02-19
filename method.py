# Tìm số nhỏ nhất
def find_min_num(arr_num):
    min_num = arr_num[0]
    for num in arr_num:
        if num < min_num:
            min_num = num
    return min_num