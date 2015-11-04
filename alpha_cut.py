#!/usr/bin/env python

class Alpha_Cut:
    
    def __init__(self, level):
        self.__level = level
        self.__intervals = []

    def add_interval(self, min_b, max_b):
        self.__intervals.append((min_b,max_b))


    def print_cut(self):
        print self.__level
        for i in self.__intervals:
            print i[0], ",", i[1]
            
    def check_consistency(self):
        pass
        
    def membership(self,x):
        for i in self.__intervals:
            # if x is smaller than lower boundary
            if i[0] > x:
                return -1
            # if x is smaller than upper boundary
            if  i[1] >= x:
                return self.__level
        # if x is bigger than last upper boundary
        return -1
          
                
            