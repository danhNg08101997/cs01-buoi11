# Viết chương trình in ra tất cả các số chẵn và số lẻ hiển thị ra màn hình

# Input
lst_number = [20,81,97,63,72,11,20,15,33,15,41,20]
# Process
lst_so_chan = [num for num in lst_number if num % 2 == 0]
lst_so_le = [num for num in lst_number if num % 2 != 0]
# Output
print(f'lst so chan: {lst_so_chan}')
print(f'lst so le: {lst_so_le}')