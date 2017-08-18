import sys

# ensure proper usage
if len(sys.argv) != 2:
    print("Usage: python unique.py key")
    exit(1)

# ensure key is a non-negative integer
s = sys.argv[1]
def unique(s):
    chars = []
    for c in s:
        for char in chars:
            if c == char:
                return False
        chars.append(c)
    return True
print "returned {}".format(unique(s))
