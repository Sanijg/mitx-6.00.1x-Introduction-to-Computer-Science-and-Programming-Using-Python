# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:43:20 2019

@author: Sanij
"""

def genPrimes():
 n=1
 while 1:
   n+=1
   count=0
   for j in range(1,n+1):
       if n%j ==0:
          count+=1
   if count==2:
     yield n