# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:08:50 2020

@author: renli
"""
def hexspreakConvert(s):
    s=hex(int(s))[2:]
    table=str.maketrans('01','OI')
    s=s.translate(table).upper()
    res= not (set(s)-set('ABCDEFIO'))
    return s if res else 'ERROR'

if __name__ == "__main__":
    res=hexspreakConvert('257')