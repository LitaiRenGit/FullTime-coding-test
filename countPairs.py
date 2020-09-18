# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:46:44 2020

@author: renli
"""
def countPairs(k,nums):
    from collections import Counter
    res=set()
    nums_Counter=Counter(nums)
    for num in nums_Counter:
        if (num+k) in nums_Counter:
            if (num+k)==num:
                if nums_Counter[num]<2: continue
            res.add(tuple(sorted([num,num+k])))
    return len(res)

if __name__=="__main__":
    res=countPairs(1,[1,1,1,2])