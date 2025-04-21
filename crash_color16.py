"""Посчитать 1/3 + 3/7 + 5/11 + ... + n+2/m+4
n = int(input('N:'))
m = int(input('M:'))
temp = 0
for up, down in zip(range(1, n+1, 2), range(3, m+1, 4)):
    temp += up/down
print(temp)"""
#Два списка на вход, в 1 прилаг, 1 сущ, сделать пары слов
prilag = [input('Прилаги:') for i in range(5)]
nouns = input('Сущи(5):').split()
total_lst = []
for first, second in zip(prilag, nouns):
    total_lst.append(' '.join([first, second]))
print(*total_lst ,sep='\n')