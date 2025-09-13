str=('a','b','c','d','a','c')

def string(s):
    return set(s)

print(string(str))


def duplicatr(s):
    dup=set([char for char in s if s.count(char)>1])
    return dup
print(duplicatr(str))