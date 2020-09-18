# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:02:08 2020

@author: renli
"""
def changingScore(arr):
    changed=True
    while changed:
        changed=False
        for i,score in enumerate(arr):
            if (i==0) or (i==len(arr)-1):
                continue
            else:
                if (score<arr[i-1]) and (score<arr[i+1]):
                    arr[i]+=1
                    changed=True
                elif (score>arr[i-1]) and (score>arr[i+1]):
                    arr[i]-=1
                    changed=True
    return arr

if __name__=="__main__":
    res=changingScore([1,6,3,4,3,5])