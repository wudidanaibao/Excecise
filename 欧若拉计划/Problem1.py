# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# 3的倍数和5的倍数
# 如果我们列出10以内所有3或5的倍数，我们将得到3、5、6和9，这些数的和是23。
#
# 求1000以内所有3或5的倍数的和。
li = []
for n in range(1, 1000):
    if n % 3 == 0:
        li.append(n)
    if n % 5 == 0 and n not in li:
        li.append(n)
print(li)
print(sum(li))