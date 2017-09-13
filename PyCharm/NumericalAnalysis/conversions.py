
from __future__ import division

million = 1000000.0
percentage = 100.0

def tom(a):
    return a * million

def per(a,b):
    return (a/percentage) * b

def wper(a,b):
    return str((a* percentage)/b) + " %"


def perp(a,b):
    return b + ( per(a,b) )

def perm(a,b):
    return b - (per(a,b) )


