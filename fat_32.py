#Список со словами через инпут, отфильтровать слова на букву т

"""words = [input() for i in range(5)]
def t_must_die(word):
    return word.lower()[-1] != 'т'
print(list(filter(t_must_die, words)))"""


"""#Посчитать произведение списка чисел из 10 эл-тов
digits = [int(input()) for i in range(10)]
def multiply(x, y):
    return x*y
print(reduce(multiply, digits, 1))"""


"""floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
#В квадрат и круг до 0,1
def sqr_rnd(x):
    return round(x**2, 1)
print(list(map(sqr_rnd, floats)))

print(list(map(lambda x: round(x**2, 1), floats)))"""


"""words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
print(list(filter(lambda word: word==word[::-1] and len(word) >=4, words)))"""


"""numbers = [4, 6, 9, 23, 5]
print(reduce(lambda x, y: x+y, numbers))"""


data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]
#Вернуть крупные
"""def is_wanted(words):
    return words[2]=='primary' and words[1] > 10000000
primaries = list(filter(is_wanted, data))
primaries = sorted(primaries)
cities_names = [el[0] for el in primaries]
print(f'Cites: {', '.join(cities_names)}')"""



"""print('Cities:', *[el[0]+',' for el in sorted(list(filter(lambda town_list: town_list[2]=='primary' and town_list[1] > 10000000, data)))])"""

