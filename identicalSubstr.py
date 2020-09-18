# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:24:37 2020

@author: renli
"""
#method 1
def identicalSubstr(s):
    def recursive(s):
        if len(s)==1: return 1
        res=recursive(s[1:])
        for ch in s:
            if ch==s[0]:
                res+=1
            else:
                break
        return res
    return recursive(s)

#method 2 (faster)
def identicalSubstr(s):
    def dp(s):
        res=0
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if s[i]==s[j]:
                    res+=1
                else:
                    break
        return res
    return dp(s)

if __name__ == "__main__":
    res=identicalSubstr('zzzyz')