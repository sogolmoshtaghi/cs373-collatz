#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------



def collatz_read (r, a) :
    """
reads two ints into a[0] and a[1]
r is a reader
a is an array on int
return true if that succeeds, false otherwise
"""
    
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

table = [0] * 1000000
table[1] = 1


def collatz_eval (i, j) :
    """
i is the beginning of the range, inclusive
j is the end of the range, inclusive
return the max cycle length in the range [i, j]
"""
    assert i > 0
    assert j > 0
    # <your code>
    if i > j:
        return collatz_eval(j, i)
    v = 1
    temp=i
    while temp <= j :
		cycle = eval_cycle (temp)
		if cycle > v:
			v = cycle 
		table[temp] = cycle
		temp = temp + 1
    assert v > 0
    return v

def eval_cycle(n):
    """
n is the number that we want to find the cycle length of
return the cycle length of n recursively 
"""
    if n == 1:
        return 1
    if table[n] != 0 :
        return table[n]
    if  n%2 == 0 :
        table[n] = 1+eval_cycle(n/2)
        return table[n]
    else:
        table[n] = 1+eval_cycle(3*n+1)
        return table[n]
        
         
        
    
          
    
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
prints the values of i, j, and v
w is a writer
i is the beginning of the range, inclusive
j is the end of the range, inclusive
v is the max cycle length
"""
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
read, eval, print loop
r is a reader
w is a writer
"""
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
