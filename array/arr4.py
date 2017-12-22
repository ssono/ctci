"""palindrome permutation: Given a string, write a function to check if it is a permutation of a palindrome
Questions: spaces, caps"""

#Time: O(N) Space: O(N)
def paliPerm(s):
    charCount = {}

    #count the number of occurences for chars
    for letter in s:
        if letter in charCount.keys():
            charCount[letter] += 1
        else:
            charCount[letter] = 1
    #track the number of times a character
    odds = 0

    for key in charCount.keys():
        if charCount[key] % 2 != 0:
            odds += 1
    #if even and any odd occurences, then it cant be a palindrome
        if(odds > 0 and len(s) % 2 == 0):
            return False

        elif(odds > 1):
            return False

    return True

print(str(paliPerm("tacocat")))
print(str(paliPerm("d")))
print(str(paliPerm("")))
print(str(paliPerm("oisudgnpa")))
