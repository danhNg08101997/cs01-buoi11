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
    
    # Duyệt 2 chiều
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