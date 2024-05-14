# list -> reverse, cut
a, b = 0, 1
count = 0
fib = []
while count < 10:
    a, b = b, a + b
    fib.append(a)
    count+=1

print(fib)
print(fib[-8:-4].reverse())
print('length: ' + str(len(fib)))