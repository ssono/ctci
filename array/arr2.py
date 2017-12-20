"""Check permutations. write a method to determine if one string is a permutation of another"""
#Time O(N) Space O(N)
#could use bit vector in place of dict
def isPerm(s1, s2):
    if len(s1) != len(s2):
        return False

    freqs1 = {}
    freqs2 = {}

    for char in s1:
        if char in freqs1.keys():
            freqs1[char] += 1
        else:
            freqs1[char] = 1

    for char in s2:
        if char in freqs2.keys():
            freqs2[char] += 1
        else:
            freqs2[char] = 1

    for char in freqs1.keys():
        if char not in freqs2.keys():
            return False

        if freqs1[char] != freqs2[char]:
            return False

    return True

a = "asdsf"
b = "dssfa"
c = "qwert"
d = "d"

print(str(isPerm(a, b)))
print(str(isPerm(a, c)))
print(str(isPerm(a, d)))
