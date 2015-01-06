# -*- coding: utf-8 -*-
"""

Brainteaser for Data Science
DC General Assembly
@author: Laura Egerdal

"""

# LOOK AT FACTORING ?? Built in to check efficiency of code

# LOOK AT Gapminder

# the function is_prime() uses math.sqrt()
import math

# list to hold the prime factors
prime_factors = []

# function to check if a number is prime, returns True or False
def is_prime(n):
    # 1 and 2 are prime
    if (n == 1 or n == 2):  
        prime = True
    else:
        # besides 2, even numbers are not prime
        if (n % 2 == 0):   
            prime = False
        else:
            i = 3
            prime = True
            # we only need to check up to the square root of n
            stop_at = math.sqrt(n) + 1
            while (i < stop_at):
                if (n % i == 0):
                    prime = False
                    i = stop_at
                else:
                    prime = True
                    # no need to check the even numbers
                    i = i + 2  
    return prime

# function finds prime factors and appends to prime_factors list
def all_prime_factors(n):
    all_factors_prime = False
    while(all_factors_prime == False):
        if (n % 2 == 0):
            factor = 2
        else:
            factor = 3
            is_factor = False
            while (is_factor == False):
                if (n % factor == 0):
                    is_factor = True
                else:
                    next_prime = False
                    while (next_prime == False):
                        factor = factor + 2
                        next_prime = is_prime(factor)
        prime_factors.append(factor)
        other_factor = n / factor
        if (is_prime(other_factor)):
            all_factors_prime = True
            prime_factors.append(other_factor)
            print 'The prime factors are:', prime_factors
            print 'The largest prime factor is:', max(prime_factors)
        else:
            n = other_factor

all_prime_factors(600851475143)
