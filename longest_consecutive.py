'''
Longest Consecutive
nums = [100, 4, 200, 1, 3, 2, 9, 10, 15, 14, 13, 12, 11]
Mô tả: chuỗi con liên tục dài nhất trong mảng là [10, 11, 12, 13, 14, 15]. Lưu ý chuỗi này ko xuất hiện theo thứ tự trong mảng
Ví dụ:
Input: nums = [100, 4, 200, 1, 2, 3]
Output: độ dài chuỗi liên tục dài nhất là 4
Giải thích: chuỗi con liên tục dài nhất trong mảng là [1, 2, 3, 4]. Lưu ý rằng chuỗi này có thể không xuất hiện theo thứ tự trong mảng.
'''
# Process
def longest_consecutive(arr_num):
    output = []
    # Sắp xếp chuỗi
    arr_num_sorted = sorted(arr_num)
    for index, num in enumerate(arr_num_sorted):
        print(str(index) + " " + str(num))
    # return output

# Input
nums = [100, 4, 200, 1, 3, 2, 9, 10, 15, 14, 13, 12, 11]
# Output
print(longest_consecutive(nums))