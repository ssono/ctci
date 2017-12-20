#Log(N) if issorted
#returns index of item
def binsearch(items [], lo, hi, item):
    if sorted(items) = items:
        if(hi == lo):
            if(items[lo] == item):
                return lo
            return -1
        index = (lo + hi) // 2
        if(item < items[index]):
            return binsearch(items, lo, index - 1, item)
        elif(item > items[index]):
            return binsearch(items, index + 1, hi, item)
        else:
            return index
