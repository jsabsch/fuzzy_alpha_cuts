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