import json
# # output format
# import datetime
#
# year='2012'
# month='May'
# print(f'today is {year}, {month}')
#
# num1=123415.21341232
# percentage=0.45969213
# print('{:-9}, {:2.3%}'.format(num1,percentage))
#
# # alignment format
# p={'Joe':12,'Aug':20,'Tt':9}
# for k,v in p.items():
#     print(f'{k:10}, {v:10d}')
#
# # formula -> text + formula result
# a = 'test'
# b = 1
# c = False
# print(f'{a=},{b=}, {c=}')
#
# print('today is {date}, and next month is {0}'.format('May',date=datetime.datetime.now()))

# read file
with open('../temp/input.txt', 'r+', encoding='utf-8') as f:
    # read_data = f.read()
    read_line1 = f.readline()
    read_line2 = f.readline()

# print(read_data)
print(read_line1)
print(read_line2)

"""
mode
r: readonly
w: write-only, current text will be covered
a: extend current content from the end
r+: read and write, cover current content
"""
f = open('../temp/input.txt', 'a')
f.write('\nadd one more line\n')

# f.close()


str1 = "{'name':'Joe','age':12,'city':'NJ'}"
x = [1, 'simple', 'list']
data = json.loads(str1)
json_text = json.dumps(data)

with open('../temp/output.txt', 'w') as f:
    f.write(json_text)
