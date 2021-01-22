import csv
import matplotlib.pyplot as plt
f = open('daegu2000.csv', encoding='cp949')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '': #값이 존재한다면
        if row[0].split('.')[1] == '4' and row[0].split('.')[2] == '18':
            result.append(float(row[-1]))

plt.plot(result, 'hotpink')
plt.show()