# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:13:01 2020

@author: renli
"""
def compress(chars) -> int:
    if not chars: return 0
    char_ptr=chars[0]
    write_index=0
    char_counter=0
    chars.append(None)
    for i,char in enumerate(chars):
        if char==char_ptr:
            char_counter+=1
        else:
            chars[write_index]=char_ptr
            if char_counter>1:
                str_char_counter=str(char_counter)
                for char_char_counter in str_char_counter:
                    write_index+=1
                    chars[write_index]=char_char_counter
            char_ptr=char
            write_index+=1
            char_counter=1
    del chars[write_index:]
    return write_index

if __name__=="__main__":
    string=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    res=compress(string)