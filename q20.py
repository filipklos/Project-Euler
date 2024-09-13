number=100
final_num=number
for i in range(number-1,0,-1):
    final_num=final_num*i

digits_sum=0
while final_num > 0:
    r = final_num % 10
    final_num = final_num // 10
    digits_sum += r

print(digits_sum)