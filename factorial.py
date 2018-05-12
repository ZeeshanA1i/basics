def factorial(n):
    '''
    INPUT:
        n: a non-negative integer
    OUTPUT:
        n!: factorial of 'n'
    '''
    if type(n) is not int or n < 0:
        return -1
    factn = 1
    while(n):
        factn *= n
        n -= 1
    return factn
