#!/usr/bin/env python

import alpha_cut



def check_consistency():
    pass

def get_membership(cuts,x):
    for cut in cuts:
        m = cut.membership(x)
        if m > -1:
            return m
    return 0

try:
    eingabe = input("Insert a list of alpha cuts: ")
    
    cuts = []
    for e in eingabe:
        if e >= 0 and e <= 1:
            cuts.append(alpha_cut.Alpha_Cut(e))
    
    cuts[0].add_interval(1,2)
    cuts[0].add_interval(3,4)
    
    cuts[1].add_interval(2,3)
    cuts[2].add_interval(4,5)
    
    cuts[1].add_interval(5,6)
    
    for c in cuts:
        c.print_cut()
        
    print get_membership(cuts, 3.5)
    
except NameError:
    print "wrong input."
except TypeError:
    print "please insert more than one alpha cuts."

