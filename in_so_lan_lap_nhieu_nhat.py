import method
lst_number = [20,81,97,63,72,11,20,15,33,15,41,20]
output = None
tan_suat_toi_da = 0
num_max = None
for num in lst_number:
    tan_suat = method.tim_tan_suat_so(num, lst_number)
    if tan_suat > tan_suat_toi_da:
        tan_suat_toi_da = tan_suat
        num_max = num
print((num_max, tan_suat))