# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:27:50 2020

@author: renli
"""

# recursive
def getUmbrellas(V, deno):
    from functools import lru_cache
    deno=tuple(deno)
    @lru_cache(maxsize=None)
    def f(requirement,size):
        if requirement==0:
            return 0
        elif requirement<0:
            return float('inf')
        if not size:
            return float('inf')
        res=min(
            (f(requirement-ele,size) for ele in size)
            )+1
        return res
    
    res=f(V,deno)
    return res if res!=float('inf') else -1

#dynamic programming
def getUmbrellas(V, deno):
    dp=[float('inf')]*(V+1)
    dp[0]=0
    for i,ele in enumerate(dp[1:]):
        i=i+1
        min_res=float('inf')
        for size in deno:
            if i-size>=0:
                min_res=min(min_res,dp[i-size])
        dp[i]=min_res+1
    return dp[-1] if dp[-1]!=float('inf') else -1
        

if __name__=="__main__":
    res=getUmbrellas(7,[3,5])