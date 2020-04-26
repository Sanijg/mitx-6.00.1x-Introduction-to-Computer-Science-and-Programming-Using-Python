# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:24:47 2019

@author: Sanij
"""

s = 'vglcoxfeznjerjdhpbiyv'
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print("Longest substring in alphabetical order is:", longest)