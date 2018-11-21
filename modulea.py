# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:23:22 2018

@author: zmimam
"""

class A:
    
    def __init__(self):
        print('Class A initialized')
    
    def display_from_a(self):
        print('Display message A')
        
    def display_from_b(self):
        print('Display message B')
    
    def display_from_c(self):
        print('Display message C')

a = A()
a.display_from_a()
a.display_from_b()
a.display_from_c()