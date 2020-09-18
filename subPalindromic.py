# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:03:21 2020

@author: renli
"""
#with duplicates
# def countSubstrings(s) -> int:
#     def count_from_center(idx):
#         if idx==int(idx):
#             li=ri=int(idx)
#         else:
#             li=int(idx-0.5)
#             ri=int(idx+0.5)
#         cnt=0
#         while (li>=0) and (ri<len(s)):
#             substr=s[li:ri+1]
#             if substr==substr[::-1]:
#                 cnt+=1
#             else:
#                 break
#             li-=1
#             ri+=1
#         return cnt
#     return sum((count_from_center(idx/2) for idx in range(0,2*len(s))))

#without duplicates
def countSubstrings(s) -> int:
    record=set()
    def count_from_center(idx):
        if idx==int(idx):
            li=ri=int(idx)
        else:
            li=int(idx-0.5)
            ri=int(idx+0.5)
        res=[]
        while (li>=0) and (ri<len(s)):
            substr=s[li:ri+1]
            if substr==substr[::-1]:
                res.append(substr)
            else:
                break
            li-=1
            ri+=1
        return res
    for idx in range(2*len(s)):
        record.update(count_from_center(idx/2))
    return len(record)

if __name__=="__main__":
    res=countSubstrings("aaa")