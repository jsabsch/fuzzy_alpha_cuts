#!/usr/bin/env python

class Alpha_Cut:
    
    def __init__(self, level):
        self.__level = level
        self.__intervals = []

    def add_intervals(self, inter_list):
        
        for i in inter_list:
            self.__intervals.append(i)
            
        return False
    
    def print_level(self):
        print "alpha cut at: ",self.__level

    def print_cut(self):
        print self.__level
        for i in self.__intervals:
            print i[0], ",", i[1]
            
    def check_consistency(self, tuple_list):
        
        for t in tuple_list:
            is_consistent = False
            
            for interval in self.__intervals:
                if t[0] >= interval[0] and t[1] <= interval[1]:
                    is_consistent = True
                    break   # good
            
            if not is_consistent:
                print "Intervals not consistent."
                return False
            
        return True
        
        