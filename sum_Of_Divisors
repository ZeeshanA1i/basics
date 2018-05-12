def S(n):
    '''
    INPUT:
        n: natual number
    OUTPUT:
        Sum: sum of all the complete-devisors of 'n'
    '''
    Sum = n
    for i in range(1, n//2+1):
        if n%i == 0:
            Sum += i
    return Sum

# Find the smallest natual number such that S(n) = 2018 (mod n)
for n in range(999, 9999):
    if S(n)%n == 2018:
        print ("S(", n ,") =", S(n), '=', 2018, "(mod", n, ')')
        break
        
# Output: S( 3382 ) = 5400 = 2018 (mod 3382 )
