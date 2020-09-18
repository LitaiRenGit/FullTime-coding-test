# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:10:59 2020

@author: renli
"""
def maxApple(capacity,apple_list):
    #it's faster to input a descending ordered apple_list
    def recursive(capacity,start,num):
        if start>=len(apple_list):
            if capacity>=0:
                return num
            else:
                return num-1
        else:
            if capacity==0:
                return num
            elif capacity<0:
                return num-1
            else:
                res=0
                for i in range(start,len(apple_list)):
                    res=max(res,recursive(capacity-apple_list[i],i+1,num+1))
                return res
    return recursive(capacity,0,0)

def maxApple(capacity,apple_list):
    #dp
    num_item = len(apple_list)
    dp = [[0 for _ in range(capacity+1)] for _ in range(num_item)]
    #每一格表示假设只有前i个item,max weight为capacity时，最优解
    for i in range(0,capacity+1):
        if i>=apple_list[0]:
            dp[0][i]=apple_list[0]
    for i in range(1,num_item):
        for j in range(1,capacity+1):
            if j>=dp[i-1][j]+apple_list[i]:
                dp[i][j] = dp[i-1][j]+apple_list[i]  # 还有容量就直接装
            else:
                # 容量不够，要么不装，要么卸一个再装
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-apple_list[i]]+apple_list[i])
    return dp[-1][-1]

if __name__ == "__main__":
    res=maxApple(5,[3,1])