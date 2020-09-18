# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 08:58:25 2020

@author: renli
"""
def basketball_scores(rounds, max_score):
    dp=[[0 for _ in range(max_score+1)] for _ in range(rounds+1)]
    #set the initial condition
    dp[1][1]=1
    dp[2][1]=1
    #dynamic programming
    for i in range(3,rounds+1):
        for j in range(max_score+1):
            dp[i][j]=(j-1)/(i-1)*dp[i-1][j-1]+(1-j/(i-1))*dp[i-1][j]
    return dp[rounds][max_score]

if __name__=='__main__':
    res=basketball_scores(100,50)