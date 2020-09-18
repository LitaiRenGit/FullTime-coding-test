# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:19:53 2020

@author: renli
"""
def heightChecker(heights) -> int:
    ordered_heights=sorted(heights)
    return sum(map(lambda x,y:1 if x!=y else 0,heights,ordered_heights))

if __name__=="__main__":
    res=heightChecker([1,1,4,2,1,3])