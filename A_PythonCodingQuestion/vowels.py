vow='Gayatri'

def count_vowel(vow):
    return sum(1 for char in vow.lower() if char in 'aeiou')

print(count_vowel(vow))