"""One away:
There are 3 types of edits; insertion, deletion, replacement.
write a function that given 2 strings returns true if they are 1 edit apart"""

import math

#given 2 strings of equal length return the number of chars different
def charsDifferent(s1, s2):
    if len(s1) != len(s2):
        return -1
    cdiff = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            cdiff == 1
    return cdiff

def oneAway(s1, s2):
    #check for replacement
    if len(s1) == len(s2):
        if charsDifferent(s1, s2) <= 1:
            return True
        return False
    #if more than 1 char length different, then can't be 1 edit away
    if math.pow(len(s1)-len(s2), 2) != 1:
        return False

    else:
        cdiff = -1
        #use indexOfError to find where the shift occured
        indexOfError = 0
        while(s1[indexOfError] == s2[indexOfError]):
            indexOfError += 1

        #compare substrings after shift to see if equal
        if len(s1) > len(s2):
            cdiff = charsDifferent(s1[indexOfError + 1:], s2[indexOfError:])
        else:
            cdiff = charsDifferent(s2[indexOfError + 1:], s1[indexOfError:])

        if cdiff == 0:
            return True
    return False

print(str(oneAway("abcd", "")))
print(str(oneAway("abcd", "abcd")))
print(str(oneAway("abcd", "abcb")))
print(str(oneAway("abcd", "acd")))
print(str(oneAway("abcd", "abbcd")))
