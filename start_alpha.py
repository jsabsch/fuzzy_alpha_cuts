#!/usr/bin/env python

import alpha_cut



def check_consistency():
    pass

try:
    eingabe = input("Insert a list of alpha cuts: ")
    
    cuts = []
    for e in eingabe:
        if e >= 0 and e <= 1:
            cuts.append(alpha_cut.Alpha_Cut(e))
    
    cuts[0].add_interval(1,2)
    cuts[0].add_interval(3,4)
    
    for c in cuts:
        c.print_cut()
        
except NameError:
    print "wrong input."
except TypeError:
    print "please insert more than one alpha cuts."

