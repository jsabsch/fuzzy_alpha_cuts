#!/usr/bin/env python

import alpha_cut


def insert_alpha_cuts():
    try:
        eingabe = input("Insert a list of alpha cuts: ")
        
        for e in eingabe:
            if e > 0 and e <= 1:
                cuts.append(alpha_cut.Alpha_Cut(e))
                
    except NameError:
        print "wrong input."
    except TypeError:
        print "please insert more than one alpha cut."
        # TODO more than one legit alpha cut!
        # TODO sort alpha cuts!
        
    return cuts
        

def insert_intervals():
    lower_cut = 0
    
    for c in cuts:
        c.print_level()
        #TODO type check
        input2 = input("Please insert intervals for this alpha cut as a list of tupels: ")
        if not check_input(input2, lower_cut):
            return False
        
        lower_cut = c
        c.add_intervals(input2)

def check_input(intervals, lower_cut):
    if type(intervals) is not tuple:
        print "wrong input type! (1)"
        return False
        
    #sort
    tuple_list = []
    try:
        sort_intervals(intervals, tuple_list)
    except TypeError as e:
        print "wrong input type! (2)"
        return False
    
    #overlapping
    try:
        overlaps(tuple_list)
    except ValueError:
        print "intervals overlap!"
        return False
    
    return check_consistency(tuple_list, lower_cut)
    
def check_consistency(tuple_list, lower_cut):
    if lower_cut == 0:
        return True
    
    return lower_cut.check_consistency(tuple_list)
        

def sort_intervals(intervals, tuple_list):
    for i in intervals:
        if type(i) is not tuple:
            raise TypeError('wrong input type')
        tuple_list.append(i)
    
    tuple_list.sort()
    return True
    
def overlaps(tuple_list):    
    last = tuple_list[0][0] - 1
    for t in tuple_list:
        if t[0] <= last:
            raise ValueError('Intervals overlap. Abort calculations.')
        last = t[1]

def get_membership(cuts,x):
    for cut in reversed(cuts):
        m = cut.membership(x)
        if m > -1:
            return m
    return 0


cuts = []
while not cuts:
    insert_alpha_cuts()
    
insert_intervals()

print get_membership(cuts, 3.5)
