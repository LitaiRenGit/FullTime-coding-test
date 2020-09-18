# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:36:07 2020

@author: renli
"""
def generateParenthesis(m,n):
    from collections import deque
    parathesis_dict={
        ')':'(',
        ']':'['
        }
    res=[]
    def recursive(s,stack,open1,close1,open2,close2):
        if open1==close1==open2==close2==0:
            res.append(s)
            return
        if open1>0:
            new_stack=list(stack)
            new_stack.append('(')
            new_stack=tuple(new_stack)
            recursive(s+'(',new_stack,open1-1,close1,open2,close2)
        if close1>0:
            if len(stack)>0:
                if stack[-1]==parathesis_dict[')']:
                    new_stack=list(stack)
                    new_stack.pop()
                    new_stack=tuple(new_stack)
                    recursive(s+')',new_stack,open1,close1-1,open2,close2)
        if open2>0:
            new_stack=list(stack)
            new_stack.append('[')
            new_stack=tuple(new_stack)
            recursive(s+'[',new_stack,open1,close1,open2-1,close2)
        if close2>0:
            if len(stack)>0:
                if stack[-1]==parathesis_dict[']']:
                    new_stack=list(stack)
                    new_stack.pop()
                    new_stack=tuple(new_stack)
                    recursive(s+']',new_stack,open1,close1,open2,close2-1)
    recursive("",tuple(),m,m,n,n)
    return res

if __name__=="__main__":
    res=generateParenthesis(1,1)