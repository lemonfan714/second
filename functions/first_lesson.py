"""#10*14
def draw_box(width:int, heigh:int):
    for i in range(heigh):
        if i==0 or i==heigh-1:
            print(width*'*')
        else:
            print('*' + (width-2)*' ' + '*')
draw_box(15, 20)"""

"""#star_triangle
def draw_triangle(filler:str, heigh:int):
    for i in range(heigh//2+1):
        print((i+1)*filler)
    for i in range(heigh//2+1,0,-1):
        print((i + 1) * filler)
draw_triangle('p', 10)"""

"""#familia
def name_print(name:str, familia:str, patrenomic:str):
    return familia[0] + name[0] + patrenomic[0]
print(ne_print('opa', 'privet', 'euka'))"""

"""#km=>miles
#0.6214

def converter(kilometers:int):
    return kilometers*0.6214
print(converter(int(input('chislo'))))"""

"""def output_days(month_num:int):
    if month_num <=7:
        if month_num==2:
            return 28
        elif month_num%2==0:
            return 30
        else:
            return 31
    else:
        if month_num%2==0:
            return 31
        else:
            return 30
print(output_days(6))
print(output_days(11))"""

#deliteli
def del_finder(num:int):

    return len([i for i in range(1, num+1) if num%i==0])

"""string = '01011100000101010'
lst = [i for i in string if i=='1']
print(lst)"""

"""def is_valid_triangle(a:int, b:int, c:int):
    if a+b>c and a+c>b and c+b>a:
        return True
    else:
        return False"""

def is_prime(num:int):
    if del_finder(num)==2:
        return True
    return False

def new_prime(num:int):
    num = num+1
    while not is_prime(num):
        num+=1
    return num
print(new_prime(13))