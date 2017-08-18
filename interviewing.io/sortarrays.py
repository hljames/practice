a1 = [4,5,6,7]
a2 = [1,7,8,9,10,11]

b1 = [1,3,3,3]
b2 = [2]

def sortarrays(a1, a2):
    i = j = 0
    new = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            if len(new) == 0 or a1[i] != new[len(new) - 1]:
                new.append(a1[i])
            i += 1
        else:
            if len(new) == 0 or a1[i] != new[len(new) - 1]:
                new.append(a2[j])
            j += 1
    while i < len(a1):
        if len(new) == 0 or a1[i] != new[len(new) - 1]:
            new.append(a1[i])
        i += 1
    while j < len(a2):
        if len(new) == 0 or a2[j] != new[len(new) - 1]:
            new.append(a2[j])
        j += 1
    return new

print (sortarrays(a1,a2))

print (sortarrays(b1,b2))
