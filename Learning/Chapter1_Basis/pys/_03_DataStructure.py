import copy

# List
li = [1, 2, 3, 4, 5]

print(li)

li2 = [6, 7, 8]
li.extend(li2)
print(li)

li.insert(0, 100)
print(li)

li.remove(8)
"""
remove item whose value = 8
"""
print(li)
"""
remove item with index 5
"""
del li[5]
print(li)

print(li.pop(2))

print(li.index(3, 0, 4))

li.count(2)

li3 = copy.deepcopy(li)
print(li3)

li3.sort()
print(li3)
li3.reverse()
print(li3)

# List formula
list4 = [(x, y) for x in range(5) for y in [1, 2, 3, 7, 8, 9] if x < y]
print(list4)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]]
list5 = [[row[i] for row in matrix] for i in range(3)]
print(list5)

# tuple
t1 = 1, '2', 3
print(t1[0])

t2 = t1, (4, '5,6', 7)
print(t2)

"""
tuple could not be modified
"""
# t1[0] = 4

"""
singleton tuple, end with ,
"""
t3 = 1,
print(t3)

# Sets
s1 = set()
s2 = {1, 2, 3}
print(1 in s2)

s3 = {2, 5, 6, 7}
print(s2 & s3)
print(s2 | s3)
print(s2 - s3)

s4 = {x for x in s3 if x > 5}
print(s4)

# dict
d1= {'a':1,'b':2,'c':3}
d1['d']=4
print(d1)

del d1['a']

print(list(d1))
print(sorted(d1))
print('b' in d1)

d3={x: x**2 for x in (2, 4, 6)}

for k,v in d3.items():
    print(k,v)

for i,v in enumerate([4,5,6]):
    print(i,v)

#zip
q=['a','b','c']
a=[1,2,3]
for qi,ai in zip(q,a):
    print(qi,ai)

for i in reversed(range(1,20,5)):
    print(i)

m=[1,4,5,2,5,1,6,9,0]
for i in sorted(set(m)):
    print(i)

# operator
a,b,c=1,2,1
print(a < b == c)
print(a == c < b)
a,b,c=True,False,True
print(a and not b or c) # = (a and not b) or c
print(a and b and c)

