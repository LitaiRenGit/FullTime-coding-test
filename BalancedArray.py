# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:12:57 2020

@author: renli
"""
def pivotIndex(nums) -> int:
    if not nums: return -1
    cumsum_nums=[0]*len(nums)
    prev_cumsum=0
    for i,num in enumerate(nums):
        cumsum_nums[i]=prev_cumsum+nums[i]
        prev_cumsum=cumsum_nums[i]
    sum_nums=sum(nums)
    if 0==(sum_nums-nums[0])/2:
        return 0
    for i,(cumsum,num) in enumerate(zip(cumsum_nums[:-1],nums[1:])):
        if cumsum==(sum_nums-num)/2:
            return i+1
    return -1