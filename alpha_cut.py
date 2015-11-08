#!/usr/bin/env python


class Alpha_Cut:
    """
    Represents one alpha cut, defined by his membership degree and a list of sets on this levels.
    """


    
    def __init__(self, level):
        self.__level = level
        self.__intervals = []

    def add_intervals(self, inter_list):
        """
        Store a list of tuples within this alpha cut. They represent different subsets of membership on this degree.
        """
        
        for i in inter_list:
            self.__intervals.append(i)
                
    def print_level(self):
        print "alpha cut at: ",self.__level

    def print_cut(self):
        print self.__level
        for i in self.__intervals:
            print i[0], ",", i[1]
            
    def check_consistency(self, tuple_list):
        """
        Check for a given list of tuples, if they lie within the boundaries of your own intervals.
        """
        
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
        
    def membership(self,x):
        """
        Check for a given value x, if lies within the boundaries of the subsets in this alpha cut.
        """
        
        for i in self.__intervals:
            # if x is smaller than lower boundary
            if i[0] > x:
                return -1
            # if x is smaller than upper boundary
            if  i[1] >= x:
                return self.__level
        # if x is bigger than last upper boundary
        return -1
          
                        