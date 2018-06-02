# S calculates the number of ways in which we get n by multiplying two or more numbers
def S(n, D = {}):
    if n in D:
        return D[n]
    SUM = 0
    for i in range(2, n//2+1):
        if not n%i:
            if isPrime(n//i):
                SUM += 1
            else:
                SUM += 1+S(n//i)
    D[n] = SUM
    return D[n]

S(999999999) == 367
S(20) == 7
S(18) == 7
