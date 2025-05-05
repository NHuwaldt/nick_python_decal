import numpy as np
import math

##Problem 1
#use 6k+1 method!
def prime_finder(a):
    if a==2 or a==3:
        return True
    if a<2 or a%2==0 or a%3==0:
        return False
    lim=int(math.sqrt(a))
    i=5
    while i<=lim:
        if a%i==0 or a%(i+2)==0:
            return False
        i+=6
    return True

#now define the rows with primes
def prime_rows(n):
    n = np.atleast_2d(n)
    return np.array([j for j in n if any(prime_finder(x) for x in row)])



##Problem 2
def matrix_maker(rows, cols, fill=0):
    return np.full((rows, cols), fill)

def checker(rows, cols):
    checker = (np.indices((rows, cols)).sum(axis=0) % 2) #note: setting axis=0 collapses the addition of indices vertically!
    checker[1::2] = 0  #alternating step for setting row to zero, first entry being either 1 or zero determines odd or even row assignment
    return checker

def checker_maker(rows, cols):
    return (np.indices((rows, cols)).sum(axis=0) % 2)

def checker_maker_v2(rows, cols):
    return ((np.indices((rows, cols)).sum(axis=0)+1) % 2) #changes starting digit between 1 and 0



##Problem 3
def string_spacer(string, spaces):
    space = ' ' * spaces
    return np.array([space.join(let) for let in string])



##Problem 4
def second_dimmest(data):
    sort_data = np.sort(data, axis=0) #axis=0 sorts along columns!
    return sort_data[-2]