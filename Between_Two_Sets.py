# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:10:53 2020

@author: renli
"""
#Between Two Sets
#1. The elements of the first array are all factors of the integer being considered
#2. The integer being considered is a factor of all elements of the second array
def cumprod(nums):
    from functools import reduce
    return reduce(lambda x,y: x*y,nums,1)
    
def primeDecompose(num:int):
    from collections import Counter
    prime=Counter()
    for factor in range(2,int(num**1/2)+1):
        while num%factor==0:
            prime[factor]=prime.get(factor,0)+1
            num//=factor
    if num!=1:
        prime[num]=prime.get(num,0)+1
        num//=num
    return prime

def lcm_prime(nums):
    #least common multiple
    from functools import reduce
    # nums[0]=primeDecompose(nums[0])
    return reduce(lambda x,y:x|primeDecompose(y),nums,primeDecompose(nums[0]))

def gcd_prime(nums):
    #greatest common divisor
    from functools import reduce
    # nums[0]=primeDecompose(nums[0])
    return reduce(lambda x,y:x&primeDecompose(y),nums,primeDecompose(nums[0]))

def unique_subset(counter):
    from collections import Counter
    from collections import deque
    counter=counter.copy()
    queue=deque([counter])
    res=1 #empty counts for 1
    while queue:
        cur_counter=queue.popleft()
        for key in cur_counter.keys():
            res+=1
            cur_choose=Counter([key])
            queue.append(cur_counter-cur_choose)
            cur_counter[key]=0
    return res

def getTotalX(a, b):
    # Write your code here
    lcm_a=lcm_prime(a)
    gcd_b=gcd_prime(b)
    if lcm_a-gcd_b:
        return 0
    else:
        return unique_subset(gcd_b-lcm_a)
        
if __name__ == "__main__":
    a=[2,4]
    b=[16,32,96]
    res=getTotalX(a,b)