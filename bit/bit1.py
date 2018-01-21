"""Insertion
You are given 2 32-bit ints n and m and 2 bit positions i and j.
insert m into n so that m starts at i and ends at j"""

def getbit(num, i):
    return((num & (1 << i)) != 0)

def setbit(num, i):
    return num | (1 << i)

def clearbit (num, i):
    return num & (~(1 << i))

def insert(n, m, i, j):
    mpos = 0
    print("n:\t" + bin(n))
    print("m:\t" + bin(m))
    for bitpos in range(i, j + 1):
        if getbit(m, mpos):
            n = setbit(n, bitpos)
        else:
            n = clearbit(n, bitpos)
        mpos += 1
    print(bin(n))
    return n

insert(1024, 19, 2, 6)
