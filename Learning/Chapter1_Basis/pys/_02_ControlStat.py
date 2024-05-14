import copy


# input from keyboard
a = int(input("please input one integer:"))

# if statments
if a < 100:
    print('less than 100')
elif a < 200:
    print('less than 200, greater than 100')
else:
    print('greater than 200')

# for statement

users = {'Joe': 'Aptean', 'Tom': 'Siemens', 'August': 'BMW'}
users_copy = copy.deepcopy(users)
for user, company in users.items():
    if user == 'August':
        users_copy[user][1] = 'BBA'

print(users_copy)
print(users)

# range -> generate Equivalent sequence(等差数列)
colleagues = ['Frank', 'Jerry', 'Light', 'Hulk']
for i in range(len(colleagues)):
    print(i, colleagues[i])

# enumerate -> 迭代器
colleagues_enum = list(enumerate(colleagues))
for colleague in colleagues_enum:
    print(colleague)

print(colleagues_enum)

# for, while, continue & break
for colleague in colleagues:
    if colleague == 'Light':
        break
    else:
        print(colleague)

for colleague in colleagues:
    print(colleague)
else:
    print('all colleagues listed already')

wh=0
while wh < 10:
    print(wh)
    wh+=1
else:
    print('number >= 10')

# Match
cities=['NJ','BJ','SH','SZ']
match cities[3]:
    case 'NJ':
        print('Nanjing')
    case 'BJ':
        print('Beijing')
    case 'SH':
        print('Shanghai')
    case _:
        print('other city')

# define function
def find_city(cityname):
    """"
    Doc string, which could be seen in Developer mode, and can be used to generate online print-doc
    """
    match cityname:
        case 'NJ':
            print('Nanjing')
        case 'BJ':
            print('Beijing')
        case 'SH':
            print('Shanghai')
        case _:
            print('other city')


find_city('SH')

f_city = find_city
f_city('NY')
# will return None in this case
print(f_city('aa'))

def find_city1(cityname, slogan='Make city better'):
    """"
    Doc string, which could be seen in Developer mode, and can be used to generate online print-doc
    """
    match cityname:
        case 'NJ':
            print('Nanjing')
        case 'BJ':
            print('Beijing')
        case 'SH':
            print('Shanghai')
        case _:
            print('other city')
    print(slogan)

find_city1('NJ')
find_city1('Tokyo', 'Make city boom')

#even it's param, list is a kind of default value, which will extend under following case
def sum(a, sum=[]):
    sum.append(a)
    return sum

def sum1(a, sum=None):
    if sum==None:
        sum = []
    sum.append(a)
    return sum

print(sum(1))
print(sum(2))
print(sum1(1))
print(sum1(2))

# Params
def f(a,*b,**c):
    print(a)
    for B in b:
        print(B)
    for key,value in c.items():
        print(key, value)

# a - 1
# b - 2 , 'a', 3
# c - d=4, f=5, e='6'
# * - positional param, ** - keyword param
f(1,2,'a',3,d=4,f=5, e='6')

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
def param_f(pos,/,std,*,key):
    print(pos,std,key)

#param_f(1,2,3)# wrong, no key-param defined here
param_f(1,std=2,key=3)

# unpack value from list - *
# unpack value from dict - **
args=[3,6]
# range need 2 parms- start and stop
print(list(range(*args)))
# create one function with 3 key param
args={'a':1,'b':2,'c':3}
def args_f(a,b=1,c=2):
    print(a,b,c)

args_f(**args)

# Lambda expression
def return_lam(n):
    return lambda f: n + f
f = return_lam(100)
print(f(1))