str='Gayatri'


def reverse_string(s):
    return s[::-1]

print(reverse_string(str))


def find_vowels(word):
    vowels = "aeiouAEIOU"  # include uppercase vowels too
    found_vowels = [ch for ch in word if ch in vowels]
    return found_vowels

word = "rupun"
vowels_in_word = find_vowels(word)

print("Word:", word)
print("Vowels found:", vowels_in_word)
print("Number of vowels:", len(vowels_in_word))