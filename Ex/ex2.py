# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
# 超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
I = int(input("请输入利润："))
J = 0
if I <= 100000:
    J = I * 0.1
if 100000 < I <= 200000:
    J = 100000 * 0.1 + (I - 100000) * 0.075
if 200000 < I <= 400000:
    J = 100000 * 0.1 + (200000 - 100000) * 0.075 + (I - 200000) * 0.05
if 400000 < I <= 600000:
    J = 100000 * 0.1 + (200000 - 100000) * 0.075 + (400000 - 200000) * 0.05 + (I - 400000) * 0.03
if 600000 < I <= 1000000:
    J = 100000 * 0.1 + (200000 - 100000) * 0.075 + (400000 - 200000) * 0.05 + (600000 - 400000) * 0.03 + (
                I - 600000) * 0.015
if I > 1000000:
    J = 100000 * 0.1 + (200000 - 100000) * 0.075 + (400000 - 200000) * 0.05 + (600000 - 400000) * 0.03 + \
        (1000000 - 600000) * 0.015 + (I - 1000000) * 0.01
print(J)
r = [1000000, 600000, 400000, 200000, 100000, 0]
i = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
j = 0
for x in range(len(r)):
    if I > r[x]:
        j = j + (I - r[x]) * i[x]
        I = r[x]
print(j)
