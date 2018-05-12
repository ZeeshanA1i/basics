def minPalC(s, Dict = {'': 0}):
    '''
    INPUT:
        s: string
        Dict: a dictionary storing values as min number
        of palindromes constituting corresponding keys
    OUTPUT:
        int: minimum number of palindromes constituting 's'
    TEST CASES:
        
    '''
    # Dynamic programing is used with the help of a dict.

    # Base case1 of the recursive relation when PalComp(s) is already known
    if s in Dict:
        return Dict[s]
    # Base case1 of the recursive relation when 's' itself is a Palindrome
    elif isPalindrome(s):
        Dict[s] = 1
        return Dict[s]
    # recursing part of the recursive function
    else:
        # As a worst case scenario, the min number of palindromes that constitute the 's' is equal to the size of 's'
        array = [len(s)]
        # For each possible size of a window traverse the string.
        for i in range(len(s)-1, 0, -1): # length of a window
            # For a certain window of certain size traverse all possible positions
            for start in range(len(s)-i): # shift window
                # if the sub-string in the current window is Palindrome
                if isPalindrome(s[start:start+i]):
                    # count it (as 1)
                    Dict[s[start:start+i]] = 1
                    # recursively call PalComp for the sub-strings to the left and right of the current string
                    Dict[s[:start]] = minPalC(s[:start], Dict)
                    Dict[s[start+i:]] = minPalC(s[start+i:], Dict)
                    # Append this one of the possible results to "array"
                    array.append(1+Dict[s[:start]]+Dict[s[start+i:]])
        # Store the best possible result for 's' to the Dict for future use
        Dict[s] = min(array)
        # Return Dict[s] as the min number of palindromes that constitute the 's'
        return Dict[s]
