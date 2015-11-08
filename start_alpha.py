#!/usr/bin/env python

import alpha_cut


def insert_alpha_cuts():
    """
    Let the user insert some alpha cut levels. Please insert a correct python list in ascending order.
    Alpha cuts can only take values between 0 and 1, so every other value will be ignored.
    """
    
    try:
        eingabe = input("Insert a list of alpha cuts in ascending order: ")
        
        for e in eingabe:
            if e > 0 and e <= 1:
                cuts.append(alpha_cut.Alpha_Cut(e))
    except NameError:
        print "wrong input."
    except TypeError:
        print "please insert a correct python list"
        
    return cuts
        
def insert_intervals():
    """
    Insert a list subsets of the current alpha cut. Please use a correct python list of tuples.
    Tuples will be sorted automatically. If an input is logically impossible (because of overlaps or 
    inconsistency with other alpha cuts), you will be notified.
    """
    
    lower_cut = 0
    
    for c in cuts:
        correct = False
        
        while not correct:
            c.print_level()
            try:
                input2 = input("Please insert intervals for this alpha cut as a list of tuples: ")
            
                if check_input(input2, lower_cut):
                    correct = True
            except TypeError:
                print "Please use a list of tuples as input."
            except NameError:
                print "wrong input type!"
            
        lower_cut = c
        c.add_intervals(input2)

def get_output():
    """
    Ask for the membership value of a specific element.
    """
    while True:
        try:
            query = input("For which element do you want to check the membership degree? ")
            print "f(", query, ") =", get_membership(query)
        except TypeError:
            print "wrong input type."
        except NameError:
            print "wrong input type."


def check_input(intervals, lower_cut):
    """
    Checks the user input of intervals for inconsistencies or errors. Also sorts the tuples in ascending order.
    """
    
    if type(intervals) is not tuple:
        print "wrong input type!"
        return False
        
    #sort
    tuple_list = []
    try:
        sort_intervals(intervals, tuple_list)
    except TypeError:
        print "wrong input type!"
        return False
    
    #overlapping
    try:
        overlaps(tuple_list)
    except ValueError:
        print "intervals overlap!"
        return False
    
    return check_consistency(tuple_list, lower_cut)
    
def check_consistency(tuple_list, lower_cut):
    """
    Checks for inconsistencies in the interval input.
    Intervals in one alpha cut have to be subsets of the level below to make logical sense.
    """
    
    if lower_cut == 0:
        return True
    
    return lower_cut.check_consistency(tuple_list)
        
def sort_intervals(intervals, tuple_list):
    """
    Sort the list of tuples in ascending order (and convert from tuple of tuples to list of tuples).
    """
    
    for i in intervals:
        if type(i) is not tuple:
            raise TypeError('wrong input type')
        tuple_list.append(i)
    
    tuple_list.sort()
    return True
    
def overlaps(tuple_list):
    """
    Check for overlapping intervals.
    """
    
    last = tuple_list[0][0] - 1
    for t in tuple_list:
        if t[0] <= last:
            raise ValueError('Intervals overlap. Abort calculations.')
        last = t[1]

def get_membership(x):
    """
    Searches for the highest alpha cut, where the value lies within the intervals.
    """
    
    for cut in reversed(cuts):
        m = cut.membership(x)
        if m > -1:
            return m
    return 0


"""

START OF THE PROGRAM

"""

cuts = []
while not cuts:
    insert_alpha_cuts()
    
insert_intervals()

get_output()
