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
