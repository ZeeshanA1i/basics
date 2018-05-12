# A palindrome is a string that when revered turns out to be the same.
# For example; aba, babab, aa, zeez, eve and adada are all palindromes.

def isPalindrome(s): # Complxty O(n/2)
    '''
    INPUT:
        s: string
    OUTPUT:
        True: if s is a palindrome
        False: if s is not a palindrome
    '''
    s = str(s)
    for i in range(len(s)//2):
        if s[i] is not s[-1-i]:
            return False
    return True
