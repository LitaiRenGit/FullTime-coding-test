# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 08:29:50 2020

@author: renli
"""
def dfs(idx,M,searched):
    if idx in searched:
        return []
    searched.add(idx)
    visited={idx}
    for f_idx,friend in enumerate(M[idx]):
        if friend:
            visited.update(dfs(f_idx,M,searched))
    return visited

def findCircleNum(M):
    if not M:
        return 0
    elif not M[0]:
        return 0
    searched=set()
    group_num=0
    groups=[]
    for idx in range(len(M)):
        if idx in searched:
            continue
        friends=dfs(idx,M,searched)
        group_num+=1
        groups.append(friends)
    return group_num,groups

if __name__=="__main__":
    M=[[1,1,0],
       [1,1,0],
       [0,0,1]]
    res=findCircleNum(M)