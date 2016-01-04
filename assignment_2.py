#!/usr/bin/env python

def get_input(name):
    """ Receive a crisp set as user input.
    """
    
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
    """ Receive a fuzzy set as user input.
    
    Calls get_input() and checks for correctness.
    Correct sets are as long as the corresponding crisp sets and contain values between 0 and 1.
    """
    
    while True:
        set_2 = get_input(name)

        if __check_for_fuzzy(set_2) and __check_length(set_1, set_2):
            return set_2

def __check_for_fuzzy(set_1):
    """ Check for values outside of [0,1] within a given set.
    """
    
    for element in set_1:
        if element < 0 or element > 1:
            print "Your fuzzy input contains elements outside of [0,1]. Please change that."
            print element
            return False
        
    return True

def __check_length(set_1, set_2):
    """ Compare the length of two sets. Only the same length is allowed.
    """
    
    if len(set_1) != len(set_2):
        print "Your fuzzy input is of different length than its associated set. Please change that."
        return False
    
    return True

def calc_goedel(x,y,mu,v):
    """ Find the greatest solution for mu*phi = v with goedels relation.   
    """ 
    g_matrix = [[0 for j in range(len(y))] for i in range(len(x))] 
    for x_index in range(len(x)):
        for y_index in range(len(y)):
            if(mu[x_index] <= v[y_index]):
                g_matrix[x_index][y_index] = 1
            else:
                g_matrix[x_index][y_index] = v[y_index];
        
    return g_matrix

def output_solution(set_X, set_Y, relations):
    """ Output the result of goedels relation.
    """
    
    print "result:"
    print "     ",
    print set_Y
    print "-------------------------------"
    for x_size in range(len(relations)):
        # for y_size in range(len(relations[1])):
            print set_X[x_size], 
            print " | ",
            print relations[x_size]
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

mat = calc_goedel(set_X, set_Y, mu, v)

output_solution(set_X, set_Y, mat)

