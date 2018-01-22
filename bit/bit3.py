"""flip it to win it:
you have an int and you hac flip exactly one 0 to a 1.
write code to find the longest sequence of 1's you can make

Strat: create a list of the sections (0or1, number of that bit)
loop through list finding max given 1 flip"""

def getbit(num, i):
    return((num & (1 << i)) != 0)

def flip2win(num):
    sections = []
    current_sect = 0
    if getbit(num, 0):
        current_sect = 1
    count = 0
    for i in range(num.bit_length()):
        if ((getbit(num, i) and current_sect == 1) or (not getbit(num, i) and current_sect == 0)):
            count += 1
            if i == num.bit_length() - 1:
                sections.append((current_sect, count))
        else:
            sections.append((current_sect, count))
            count = 1
            current_sect ^= 1
    print(sections)
    maximum = 1
    for i in range(len(sections)):
        if sections[i][0] == 1 and sections[i][1] >= maximum:
            maximum = sections[i][1]
            if i != 0:
                maximum += 1
        elif sections[i][0] == 0 and sections[i][1] == 1 and i != 0:
            t = sections[i-1][1] + sections[i+1][1]
            if t >= maximum:
                maximum = t + 1
    return maximum

print(str(flip2win(883)))
