# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:37:29 2020

@author: renli
"""
# =============================================================================
# Given a sorted array of positive integers. Your task is to rearrange the array elements alternatively 
# i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.
# Constraints:
# Array Contains Duplicate Values.
# =============================================================================
def rearrange(nums):
    res=[]
    li,ri=0,len(nums)-1
    while li<ri:
        res.append(nums[ri])
        res.append(nums[li])
        li+=1
        ri-=1
    if li==ri:
        res.append(nums[li])
    return res
        
if __name__=="__main__":
    import numpy as np
    nums=np.random.randint(1,100,(100,))
    nums=sorted(nums)
    res=rearrange(nums)