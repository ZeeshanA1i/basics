def isListOfLists(L):
    if type(L) != list:
        return False
    for l in L:
        if type(l)==list:
            return True
    return False

print (isListOfLists(2),
      isListOfLists([2]),
      isListOfLists([[2]]))

def Append(arr, c):
    if type(arr) == list and type(c) == int:
        if isListOfLists(arr) == False:
            arr.append(c)
            return
        for a in arr:
            Append(a, c)
    elif type(arr) == list and type(c) == list:    
        if isListOfLists(c) == False:
            arr.append(c)
            return
        for cc in c:
            Append(arr, cc)

def change(N):
    if N == 1:
        return [1]
    LIST = [[N]]
    for c in range(1, N):
        cList = change(N-c)
        Append(cList, c)
        Append(LIST, cList)
    return LIST

print (change(3))

def minPalC(s):
    minIndex = len(s)
    # pos is the list of all the possible sets of split indices
    # E.g. change(3) = [[3], [2, 1], [1, 1, 1], [1, 2]]
    pos = (change(len(s)))[1:]
    for r in pos: # r is a set of split indices
        index = 0
        # check if all the substrings are Palindrome
        check = True
        for rr in range(len(r)):
            if isPalindrome(s[index:index+r[rr]]) == False:
                check = False
                break
            index += r[rr]
        if check == True:
            if len(r) < minIndex:
                minIndex = len(r)
    return minIndex

print (minPalC("dadofanna"))
