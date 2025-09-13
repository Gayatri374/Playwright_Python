# from collections import Counter
#
# def fre(f):
#     return dict(Counter(f))
#
# print(fre('gayatriBalkrishnapotadar'))
#
# var='MADAMMA'
# def fe(s):
#     return dict(Counter(s))
#
# print(fe(var))


from collections import Counter


def fre(s):
    return dict(Counter(s))

print(fre('GAYATRI'))


text = "epam python interview python epam test"
words = text.split()
freq = dict(Counter(words))
print(freq)  # Counter({'epam': 2, 'python': 2, 'interview': 1, 'test': 1})