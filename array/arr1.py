"Is Unique: Implement an algo to determine if a string is composed of unqiue characters. What if you dont have any additional datastructures"

# time=O(N*N) Space=O(1)
def isUnique(s):
    startLength = len(s)
    s += " "
    for i in range(0, startLength):
        if s[i] in s[startLength:]:
            return False
        s += s[i]
    return True

"""#Time = O(NlogN) Space = O(N)
def dsIsUnique(s):
    stringAsList = []
    for letter in s:
        stringAsList.append(letter)
    stringAsList.sort()
    #error: stringAsList = stringAsList.sort()
    for i in range(0, len(stringAsList) - 2):
        if stringAsList[i] == stringAsList[i + 1]:
            return False
    return True"""

#time O(N) Space O(N)
def dsIsUnique(s):
    if len(s) > 128:
        return False
    charSeen = []
    for letter in s:
        if charSeen[ord(letter)] == True:
            return False
        charSeen[ord(letter)] = True
    return True


a = "qwertyuiop"
b = "acflkssanfposoiufvn"
c = "c"
d = "dddddddddd"

print(a +"\t" + str(isUnique(a)))
print(b + "\t" + str(isUnique(b)))
print(c +"\t" + str(isUnique(c)))
print(d + "\t" + str(isUnique(d)))

print("With Data structure")

print(a +"\t" + str(dsIsUnique(a)))
print(b + "\t" + str(dsIsUnique(b)))
print(c +"\t" + str(dsIsUnique(c)))
print(d + "\t" + str(dsIsUnique(d)))
