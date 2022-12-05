"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i=1
    if number_of_primes <= 0:
        raise ValueError('Number must be greater than 1')
    if number_of_primes>=0:
        while len(list)<number_of_primes:
            factors = []
            for n in range(1, i+1):
                if i%n == 0: 
                    factors.append(n)
                elif len(factors) > 2:
                    break

            if len(factors) == 2:
                list.append(i)
            i += 1
        return list
    
