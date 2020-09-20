import os

tables = ['table1.txt', 'table2', 'hi']
att = ['extract','delivery','status']
files = ['table1.txt','table2.txt','table3.txt']
output = { x : {att[0]:'', att[1]:'', att[2]:'',} for x in tables }

for i in tables:
        output[i]['status'] = 'available' if i in files else 'missing'
        #print('available', i, f)

matching = []
for i in tables:
    match = [f for f in files if i in f]
    #print(match)
    matching.append(match)
print(matching)



