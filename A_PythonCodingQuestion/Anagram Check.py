from collections import Counter


# Sorted
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("epam", "pame"))       # True


# collections.Counter

def coll(s1,s2):
    return Counter(s1)==Counter(s2)

print(coll('race','care'))
print(coll('gayatri','iigatyar'))


# Ignore spaces and case

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

print(is_anagram("Dormitory", "Dirty room"))

