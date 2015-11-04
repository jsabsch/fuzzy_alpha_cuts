#!/usr/bin/env python

import alpha_cut

try:
    eingabe = input("Insert a list of alpha cuts: ")
    
    cuts = []
    for e in eingabe:
        cuts.append(alpha_cut.Alpha_Cut(e))
    
    for c in cuts:
        c.print_level()
        
except NameError:
    print "wrong input."

