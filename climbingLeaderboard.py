# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:21:19 2020

@author: renli
"""
def sorted_unique(l):
    ptr=0
    for i in range(1,len(l)):
        if l[i]!=l[ptr]:
            l[ptr+1]=l[i]
            ptr+=1
    return l[:ptr+1]
        
def climbingLeaderboard(ranked, player):
    # Write your code here
    import bisect
    ranked=list(map(lambda x:-x,ranked))
    player=list(map(lambda x:-x,player))
    ranked=sorted_unique(ranked)
    res=[]
    for score in player:
        index=bisect.bisect_left(ranked,score)
        res.append(index+1)
        ranked=ranked[:index+1]
    return res

if __name__ == "__main__":
    ranked=[100,100,50,40,40,20,10]
    player=[5,25,50,120]
    res=climbingLeaderboard(ranked, player)
    # res=sorted_unique(ranked)