def isPrime(n):
    '''
    INPUT:
        n: an integer
    OUTPUT:
        boolean: True when n is a prime, False otherwise.
    '''
    if type(n) == int:
        if n == 0:
            return False
        if n < 0:
            n *= -1
        for i in range(2, n):
            if not n%i:
                return False
        return True
    return False
