'''chose = 0
while chose != 'нет':
    chose = input('Введите автора и цитату')
    if chose == 'нет':
        break
    else:
        lister = chose.split('->')
        with open('quotes.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n\n{lister[0]}')
            file.write(f'\n({lister[1]})')
file = open('quotes.txt', 'r', encoding='utf-8')
lister = file.readlines()
for i in lister:
    if '(' in i:
        print(i.lstrip('(').rstrip(')'))
file.close()'''

grades = []
with open('.venv/pupils.txt', 'r', encoding='utf-8') as file:
    for line in file:
        multiple = line.split()
        grades.append(int(multiple[2]))
        '''if '5' in multiple[2]:
            print(multiple[0])'''
total = sum(grades)/len(grades)
print(round(total, 2))