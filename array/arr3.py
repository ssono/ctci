"""Urlify: takes a string and its length and returns a string where all spaces have been replaced with %20"""

def urlify(s, length):
    result = ""
    for i in range(0, length):
        if s[i] != ' ':
            result += s[i]
        else:
            result += "%20"
    return result
a = "uygdwld woidhjew dn d didowijd  donwdoi"
print(urlify(a, len(a)))
