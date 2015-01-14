'''
Author: Laura Egerdal
Date: 01-14-2015
Brainteaser: What is the largest prime factor of 600851475143?

VERSION 2 (takes 0.74 miliseconds)

'''

# the function is_prime() uses math.sqrt()
import math

# timing my script
import time

# function prints a list of the prime factors and the largest prime factor
def get_prime_factors(n):
    
    # empty list to hold prime factors
    prime_factors = []
    
    # timing my code as a measure of efficiency
    start_time = time.time()
    
    # we will start dividing n by 2
    x = 2
    
    # this loop checks if n is evenly divisible by factors from 2 through sqrt(n)
    # once we've checked factors through the sqrt(n), we know n is the final prime factor
    while (x < math.sqrt(n)):
        # if n divides evenly by x, we know that x is a factor
        if (n % x == 0):
            # add x to the list of factors
            prime_factors.append(x)
            # we need to check the remainder - is it prime?
            # set the value of n to the remainder
            n = n / x
            # set the value of x to start at 2
            x = 2
        else:
            # n does not divide evenly by x, so we'll continue checking for factors
            x = x + 1;
            
    # add the remainder to the list (the last prime factor)
    prime_factors.append(n)

    
    print 'The prime factors are:', prime_factors
    print 'The largest prime factor is:', max(prime_factors)
    
    # print the time script takes to run
    miliseconds = round(((time.time() - start_time) * 1000),2)
    print 'It took', miliseconds, 'miliseconds to solve.'

get_prime_factors(600851475143)


