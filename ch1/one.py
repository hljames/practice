def one(s1, s2):
    if len(s1) == len(s2):
        return replace(s1,s2)
    elif (len(s1) + 1) == len(s2):
        return insert(s2, s1)
    elif len(s1) == (len(s2) + 1):
        return insert(s1, s2)
    else: return False

def replace(s1,s2):
    edited = False
    for a,b in zip(s1, s2):
        if a != b:
            if edited == True:
                return False
            edited = True
    return True
    
def insert(s1, s2):
    edited = False
    i = 0
    j = 0
    while j < len(s2):
        if s1[i] != s2[j]:
            if edited == True:
                return False
            else:
                j += 1
                edited = True
        i += 1
        j += 1
    return True
