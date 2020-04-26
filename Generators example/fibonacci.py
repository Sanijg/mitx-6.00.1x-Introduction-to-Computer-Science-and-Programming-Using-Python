# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:49:30 2019

@author: Sanij
"""

def genFib():
      f1=1
      f0=0
      while True:
          n=f1+f0
          yield n
          f0=f1
          f1=n