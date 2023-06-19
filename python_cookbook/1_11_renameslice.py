
# Naming a slice

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost) # 51325.0   

SHARES = slice(20,23)   
PRICE = slice(31,37)
cost = int(record[SHARES]) * float(record[PRICE])   
print(cost) # 51325.0

s = 'HelloWorld'
a = slice(5,10,2)
print(a.indices(len(s))) # (5, 10, 2)
for i in range(*a.indices(len(s))): 
    print(s[i]) # W r d