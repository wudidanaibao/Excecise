# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/2 16:53'

"""
计算数字k在0到n中的出现的次数，k可能是0~9的一个值
样例
例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)
"""


class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        s = ''.join([str(i) for i in range(n+1)])
        return s.count(str(k))