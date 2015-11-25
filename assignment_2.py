#!/usr/bin/env python

def get_input(name):
    set_1 = []
    
    while len(set_1) == 0:
        try:
            eingabe = input("Insert a list of elements for set " + name + ": ")
            
            for e in eingabe:
                set_1.append(e)
        except NameError:
            print "wrong input."
        except TypeError:
            print "please insert a correct python list"

    return set_1

def get_fuzzy_input(name, set_1):
    while True:
        set_2 = get_input(name)

        if __check_for_fuzzy(set_2) and __check_length(set_1, set_2):
            return set_2

def __check_for_fuzzy(set_1):
    for element in set_1:
        if element < 0 or element > 1:
            print "Your fuzzy input contains elements outside of [0,1]. Please change that."
            print element
            return False
        
    return True

def __check_length(set_1, set_2):
    if len(set_1) != len(set_2):
        print "Your fuzzy input is of different length than its associated set. Please change that."
        return False
    
    return True

def calc_goedel(x,y,mu,v):
    # TODO: calculations!
    return 0

def output_solution(relations):
    pass
    # TODO print output


"""
---------------
---> MAIN: <---
---------------
"""

set_X = get_input('X')
set_Y = get_input('Y')

mu = get_fuzzy_input("mu", set_X)
v = get_fuzzy_input("v", set_Y)

output_solution(calc_goedel(set_X, set_Y, mu, v))

