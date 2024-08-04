import random as r


coin = ['H', 'T']
results = []
for i in range (10000): #starts at 0, ends at 9999
    row = []
    for i in range(10):
        row.append(coin[r.randint(0, 1)])
    results.append(row)

for i in range(len(results)):
    for j in range(len(results[i])):
        

print(results)